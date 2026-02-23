#!/usr/bin/env python3
"""
SSIL Demo Cross-Platform Verifier (CI-ready)

Verifies:
- Two-run byte identity per case (B_A = B_B)
- Canonical SHA-256 per case under locked canonical profile
- Deterministic execution using only CPython + stdlib

Exit codes:
0 = PASS
1 = FAIL
"""

from __future__ import annotations

import argparse
import hashlib
import os
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


# -----------------------------
# Canonical profile (locked)
# -----------------------------
CANON = {
    "H": "8",
    "delta_max": "0.15",
    "s_max": "10.0",
    "beta": "0.5",
    "gamma": "0.5",
    "wA": "0.6",
    "wB": "0.2",
    "wS": "0.2",
    "eta": "0.25",
    "rho": "1.0",
}

CANON_SHA256: Dict[str, str] = {
    "baseline": "b3a7d70e085b5a7289a1c033b83c95dc3c8c8713b301c7401fc1ff07bbb8b839",
    "edgezero": "23596beb23014c492e4746156485989b1146cf21ba328f99bc948d2b8111a52e",
    "recovery3": "14a5c61508b845a2bc503a3151fba8857973d0a75564fae880c0bcb15753168e",
}

TRACE_BY_CASE: Dict[str, str] = {
    "baseline": "traces/trace_demo.csv",
    "edgezero": "traces/trace_edgezero.csv",
    "recovery3": "traces/trace_recovery3.csv",
}


@dataclass
class RunResult:
    case: str
    out1: Path
    out2: Path
    sha1: str
    sha2: str
    byte_identical: bool
    canonical_ok: bool


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_bytes(p: Path) -> bytes:
    return p.read_bytes()


def ensure_repo_layout(root: Path) -> None:
    required = [
        root / "engine" / "ssil_engine_v1_2.py",
        root / "traces",
        root / "reference_outputs",
        root / "docs",
    ]
    for r in required:
        if not r.exists():
            raise FileNotFoundError(f"Missing required path: {r}")


def normalized_env() -> Dict[str, str]:
    # Deterministic env normalization
    env = dict(os.environ)
    env["PYTHONHASHSEED"] = "0"
    env["TZ"] = "UTC"
    env["LC_ALL"] = "C"
    env["LANG"] = "C"
    return env


def run_engine(
    root: Path,
    trace: Path,
    out_csv: Path,
    python_exec: str,
    env: Dict[str, str],
) -> None:
    engine = root / "engine" / "ssil_engine_v1_2.py"
    cmd = [
        python_exec,
        str(engine),
        "--in",
        str(trace),
        "--out",
        str(out_csv),
        "--H",
        CANON["H"],
        "--delta-max",
        CANON["delta_max"],
        "--s-max",
        CANON["s_max"],
        "--beta",
        CANON["beta"],
        "--gamma",
        CANON["gamma"],
        "--wA",
        CANON["wA"],
        "--wB",
        CANON["wB"],
        "--wS",
        CANON["wS"],
        "--eta",
        CANON["eta"],
        "--rho",
        CANON["rho"],
    ]
    p = subprocess.run(cmd, cwd=str(root), env=env, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(
            "Engine run failed.\n"
            f"CMD: {' '.join(cmd)}\n"
            f"STDOUT:\n{p.stdout}\n"
            f"STDERR:\n{p.stderr}\n"
        )


def run_case(root: Path, case: str, outdir: Path, python_exec: str) -> RunResult:
    env = normalized_env()
    trace_rel = TRACE_BY_CASE[case]
    trace = root / trace_rel

    out1 = outdir / f"{case}_run1.csv"
    out2 = outdir / f"{case}_run2.csv"

    # Ensure clean
    for p in (out1, out2):
        if p.exists():
            p.unlink()

    run_engine(root, trace, out1, python_exec, env)
    run_engine(root, trace, out2, python_exec, env)

    b1 = read_bytes(out1)
    b2 = read_bytes(out2)
    byte_identical = (b1 == b2)

    sha1 = sha256_file(out1)
    sha2 = sha256_file(out2)

    canonical_ok = (sha1 == sha2 == CANON_SHA256[case])

    return RunResult(
        case=case,
        out1=out1,
        out2=out2,
        sha1=sha1,
        sha2=sha2,
        byte_identical=byte_identical,
        canonical_ok=canonical_ok,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--outdir",
        default="OUT_VERIFY",
        help="Output directory for verification runs (created if missing).",
    )
    ap.add_argument(
        "--python",
        default=sys.executable,
        help="Python executable to use (default: current interpreter).",
    )
    ap.add_argument(
        "--cases",
        default="baseline,edgezero,recovery3",
        help="Comma-separated cases to run.",
    )
    args = ap.parse_args()

    root = Path(__file__).resolve().parent
    ensure_repo_layout(root)

    outdir = root / args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    cases = [c.strip() for c in args.cases.split(",") if c.strip()]
    for c in cases:
        if c not in TRACE_BY_CASE:
            print(f"FAIL: Unknown case '{c}'. Valid: {', '.join(TRACE_BY_CASE.keys())}")
            return 1

    print("========================================")
    print("SSIL CROSS-PLATFORM VERIFY (verify.py)")
    print("========================================")
    print(f"Root: {root}")
    print(f"OS: {platform.platform()}")
    print(f"Python: {args.python}")
    print(f"Outdir: {outdir}")
    print("----------------------------------------")
    print("Locked canonical profile:")
    print(
        f"H={CANON['H']} delta-max={CANON['delta_max']} s-max={CANON['s_max']} "
        f"beta={CANON['beta']} gamma={CANON['gamma']} wA={CANON['wA']} wB={CANON['wB']} "
        f"wS={CANON['wS']} eta={CANON['eta']} rho={CANON['rho']}"
    )
    print("----------------------------------------")

    all_ok = True
    results: List[RunResult] = []

    for case in cases:
        print(f"Running case: {case}")
        try:
            rr = run_case(root, case, outdir, args.python)
        except Exception as e:
            print("FAIL: Engine execution error")
            print(str(e))
            return 1

        results.append(rr)

        if not rr.byte_identical:
            all_ok = False
            print(f"  B_A = B_B: FAIL (bytes differ)")
        else:
            print(f"  B_A = B_B: PASS")

        print(f"  SHA256(run1): {rr.sha1}")
        print(f"  SHA256(run2): {rr.sha2}")

        if rr.canonical_ok:
            print(f"  CANONICAL_FINGERPRINT: PASS")
        else:
            all_ok = False
            print(f"  CANONICAL_FINGERPRINT: FAIL")
            print(f"  Expected: {CANON_SHA256[case]}")
        print("")

    print("========================================")
    if all_ok:
        print("SSIL_VERIFY_RESULT: PASS")
        return 0
    else:
        print("SSIL_VERIFY_RESULT: FAIL")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())