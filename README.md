# ⭐ Shunyaya Structural Irreversibility Layer (SSIL) — Deterministic Demo

**Deterministic Structural Irreversibility Governance — Without Modifying Classical Systems**

![SSIL--Demo](https://img.shields.io/badge/SSIL--Demo-Deterministic%20Irreversibility%20Governance-blue)
![Verification](https://img.shields.io/badge/Verification-Replay%20Verified-purple)
![Deterministic](https://img.shields.io/badge/Deterministic-Yes-green)
![Replay--Verified](https://img.shields.io/badge/Replay--Verified-B_A%20%3D%20B_B-green)
![Finite--R5](https://img.shields.io/badge/Irreversibility%20Grammar-Finite%20(5)--State-green)
![Magnitude--Preserved](https://img.shields.io/badge/Magnitude-Unmodified%20(phi((m,a,s,r))%20%3D%20m)-green)
![Bounded--Horizon](https://img.shields.io/badge/Horizon-Fixed%20H-green)
![Admissibility--Governed](https://img.shields.io/badge/Admissibility-CONTINUE%20%7C%20ABSTAIN-green)
![Canonical--Profile](https://img.shields.io/badge/Profile-Canonical%20Locked-orange)
![Open--Standard](https://img.shields.io/badge/Standard-Open-blue)

**Replay-Verified • Finite Irreversibility Grammar • Conservative Magnitude Preservation • Open Standard**

---

## 📘 What Is This Repository?

This repository is a **minimal, self-contained deterministic demonstration** of the Shunyaya Structural Irreversibility Layer (SSIL).

It exists to prove — in executable form — that SSIL:

- Detects irreversible structural transitions  
- Governs continuation admissibility  
- Preserves classical magnitude  
- Produces byte-identical replay under fixed parameters  

This repository focuses strictly on:

- Deterministic verification  
- Minimal reproducibility  
- Canonical fingerprint validation  

If you are seeing SSIL for the first time:

**This demo is the fastest way to verify that SSIL is structurally real.**

---

## 🔗 Main SSIL Repository (Full Specification)

The complete SSIL specification, formal documentation, and extended material are available at:

https://github.com/OMPSHUNYAYA/Structural-Irreversibility-Layer

**Main repository one-line summary:**

SSIL introduces a deterministic finite irreversibility grammar `{R0, E0, I1, I2, C}` over system evolution, preserves classical magnitude via `phi((m,a,s,r)) = m`, governs continuation through `IRR_ADM(t)`, and defines conformance strictly by exact replay equivalence `B_A = B_B`.

This demo repository is the executable conformance proof layer.

---

## ⚖ Conformance Language Clarification (Demo Repository Scope)

The conformance language used in this demo repository may be stricter and more enforcement-oriented than the broader specification language in the main SSIL repository.

This is intentional.

The `ssil-demo` repository functions as a deterministic compliance harness and audit surface.  
Its specification language is optimized for:

- Binary verification  
- Canonical fingerprint enforcement  
- Replay discipline  

There is no functional divergence between repositories.

The mathematical kernel, irreversibility grammar, conservative invariant, bounded horizon discipline, and replay identity rule remain identical.

This repository strengthens clarity — it does not modify structure.

---

## 🔗 Quick Links

### 📘 Documentation (Demo Scope)

All documentation files are located under:

- [`docs/`](docs/)

**Core Model & Conformance**

- [SSIL-Structural-Irreversibility-Model.md](docs/SSIL-Structural-Irreversibility-Model.md)  
- [SSIL-Conformance-Specification.md](docs/SSIL-Conformance-Specification.md)  
- [SSIL_DEMO_EXECUTION_SPEC.md](docs/SSIL_DEMO_EXECUTION_SPEC.md)  
- [SSIL_KILLER_DEMO_SPEC.md](docs/SSIL_KILLER_DEMO_SPEC.md)  
- [SSIL_MIN_ADAPTER_SPEC.md](docs/SSIL_MIN_ADAPTER_SPEC.md)  

**Cases & Evidence Notes**

- [CASE_INDEX.md](docs/CASE_INDEX.md)  
- [CASE_EDGEZERO_NOTE.md](docs/CASE_EDGEZERO_NOTE.md)  
- [CASE_RECOVERY_WINDOW_NOTE.md](docs/CASE_RECOVERY_WINDOW_NOTE.md)  
- [PASS_EVIDENCE_CHECKLIST.md](docs/PASS_EVIDENCE_CHECKLIST.md)  

**User Guidance**

- [Quickstart.md](docs/Quickstart.md)  
- [FAQ.md](docs/FAQ.md)  

**Topology Diagram**

- [SSIL-Structural-Irreversibility-Topology-Diagram.png](docs/SSIL-Structural-Irreversibility-Topology-Diagram.png)

All `.txt` documentation files have been standardized to `.md` for GitHub publication.

The structural invariants remain unchanged:

- `phi((m,a,s,r)) = m`  
- `R = {R0, E0, I1, I2, C}`  
- `IRR_ADM(t) ∈ {CONTINUE, ABSTAIN}`  
- `B_A = B_B`

---

### ⚙ Deterministic Verification (Primary Entry Points)

Cross-platform verifier (recommended):

- [`verify.py`](verify.py)

Run from repository root:

python verify.py

Replay condition:

`B_A = B_B`

Byte identity is required.  
No tolerance.  
No statistical equivalence.

Core invariant preserved:

`phi((m,a,s,r)) = m`

Finite irreversibility grammar:

`R = {R0, E0, I1, I2, C}`

---

### 🧪 Deterministic Demo Runner

Windows:

- [`RUN_DEMO.bat`](RUN_DEMO.bat)  
- [`RUN_ALL.bat`](RUN_ALL.bat)

Linux / macOS:

- [`RUN_DEMO.sh`](RUN_DEMO.sh)

All runners enforce:

- Locked canonical profile  
- Two-run replay identity  
- SHA-256 verification  
- Byte comparison  

Determinism is mandatory.

---

### 🧪 Independent Verification Capsule (Authoritative Harness)

Verification capsule directory:

- [`VERIFY_CAPSULE/`](VERIFY_CAPSULE/)

Contents include:

- Canonical SHA-256 reference file  
- Windows batch runner  
- Shell runner  
- Capsule verification script  

Verification succeeds only if replay is byte-identical.

Capsule enforces:

- Fixed bounded horizon `H`  
- Deterministic Recovery predicate  
- Deterministic EdgeZero predicate  
- Deterministic continuation mapping `IRR_ADM(t)`  
- Canonical fingerprint verification  
- Replay identity `B_A = B_B`  

If replay identity fails, conformance fails.

---

### 📂 Replay Evidence Structure

**Runtime outputs (ephemeral — generated locally):**

- [`OUT/`](OUT/)  
- [`OUT_VERIFY/`](OUT_VERIFY/)

These are not authoritative and must not be treated as frozen conformance artifacts.

**Authoritative replay-verified reference bundle:**

- [`reference_outputs/`](reference_outputs/)

Conformance is defined by deterministic replay equivalence — not by pre-generated example files.

All replay runs must remain byte-identical under declared scope.

---

### 📜 License

- [`LICENSE`](LICENSE)

Shunyaya Structural Irreversibility Layer (SSIL) — Deterministic Demo is published under an **open license**.

Conformance is defined structurally by replay equivalence:

`B_A = B_B`

---

## 🧭 Why SSIL Exists (30-Second Overview)

Classical systems check correctness of magnitude.

SSIL checks permission to continue across irreversible boundaries.

Many system collapses occur not because equations fail —  
but because an irreversible transition was crossed without structural awareness.

SSIL introduces a deterministic irreversibility governance layer that evaluates reversibility posture before continuation.

It does not change equations.  
It governs structural permission.

---

## ✅ 60-Second Verification (Start Here)

SSIL is proven by exact replay — not interpretation.

Verification succeeds if and only if:

`B_A = B_B`

There is:

- No randomness  
- No tolerance  
- No approximate equality  
- No statistical equivalence  

Artifacts are either byte-identical — or the run is **NOT VERIFIED**.

---

## 🔁 Cross-Platform Verification (Recommended)

Works on Windows, Linux, and macOS.

From repository root:

```
python verify.py
```

Expected final line:

SSIL_VERIFY_RESULT: PASS

**PASS requires:**

- Two-run byte identity per case (`B_A = B_B`)
- Canonical SHA-256 fingerprints match for:
  - `baseline`
  - `edgezero`
  - `recovery3`

Outputs are written to:

OUT_VERIFY/

`reference_outputs/` remains unchanged.

---

## 🧪 Capsule Verification (Windows — Official Batch Path)

From repository root:

```
VERIFY_CAPSULE\RUN_VERIFY.bat
```

Expected final line:

VERIFY_CAPSULE_RESULT: PASS

The capsule enforces:

- Finite irreversibility regime `{R0, E0, I1, I2, C}`
- Conservative invariant `phi((m,a,s,r)) = m`
- Fixed bounded horizon `H`
- Deterministic Recovery predicate
- Deterministic EdgeZero predicate
- Deterministic continuation mapping `IRR_ADM(t)`
- Canonical fingerprint verification
- Independent replay comparison

If replay identity fails, SSIL fails.  
There is no partial success.

---

## ⚙ Canonical Verification Profile (Locked)

All official canonical fingerprints in this repository are defined only for the following cases:

- `baseline`
- `edgezero`
- `recovery3`

and only under the exact locked parameter surface below:

H = 8  
delta-max = 0.15  
s-max = 10.0  
rho = 1.0  
beta = 0.5  
gamma = 0.5  
wA = 0.6  
wB = 0.2  
wS = 0.2  
eta = 0.25  

Canonical fingerprints are valid **if and only if:**

- The above parameters are unchanged  
- The execution environment is deterministic  
- Byte-identical replay identity holds (`B_A = B_B`)  
- No formatting drift occurs  
- No mutation of artifacts occurs  

Any deviation — even if deterministic — invalidates canonical fingerprint claims.

All other parameter surfaces remain deterministic but are considered illustration profiles and do not carry canonical authority.

Runtime directories (`OUT/` and `OUT_VERIFY/`) do not define canonical artifacts.

Only frozen artifacts under `reference_outputs/` define canonical fingerprints.

---

## 📊 Deterministic Cases Included

| Case      | Trace File              | Demonstrates                                   | Replay Required |
|-----------|------------------------|-----------------------------------------------|----------------|
| Baseline  | `trace_demo.csv`       | Stable continuation regime                    | Yes            |
| EdgeZero  | `trace_edgezero.csv`   | Irreversible boundary crossing detection      | Yes            |
| Recovery  | `trace_recovery3.csv`  | Recovery window signaling                     | Yes            |

Each case includes frozen CSV outputs and SHA-256 seals in `reference_outputs/`.

---

## 🧮 Core Mathematical Contract

### **Conservative Invariant**

`phi((m,a,s,r)) = m`

Classical magnitude remains untouched.

SSIL never modifies:

- Physics  
- Equations  
- Domain models  
- Measured outputs  

It governs continuation admissibility only.

---

### **Finite Irreversibility Grammar**

`R = {R0, E0, I1, I2, C}`

Properties:

- Fixed size `|R| = 5`
- No runtime regime expansion
- Deterministic classification
- Closed under declared predicates

No additional regime is permitted.

---

### **Continuation Mapping**

`IRR_ADM(t) ∈ {CONTINUE, ABSTAIN}`

Default conservative rule:

- `R0 → CONTINUE`
- `{E0, I1, I2, C} → ABSTAIN`

SSIL governs permission to continue.  
It does not alter magnitude.

---

## 🔁 Replay Identity Requirement

Conformance is defined strictly by:

`B_A = B_B`

Replay equivalence requires identical:

- Irreversibility sequence `r(t)`
- Continuation decisions `IRR_ADM(t)`
- CSV artifacts
- SHA-256 digests

If replay identity fails, conformance fails.

No tolerance windows.  
No statistical equivalence.  
No probabilistic interpretation.

---

## 🛑 Scope Boundary

SSIL operates strictly at the level of:

- Irreversibility regime classification  
- Bounded horizon evaluation  
- Recovery detection  
- EdgeZero boundary detection  
- Continuation admissibility governance  
- Replay-verifiable determinism  

SSIL does **not**:

- Predict outcomes  
- Optimize systems  
- Modify physics  
- Inject control signals  
- Guarantee safety  

It governs structural continuation discipline only.

---

## 🌍 Open Standard

SSIL is published as an Open Standard.

- Independent implementations encouraged  
- Conformance defined structurally (`B_A = B_B`)  
- No institutional gatekeeping  
- Provided as-is, without warranty  

Optional attribution:

Recommended but not required:

“Implements Shunyaya Structural Irreversibility Layer (SSIL).”

---

## 🏷 Topics

Deterministic-Governance • Irreversibility-Grammar • Finite-Regime • Replay-Verification • Bounded-Horizon • Structural-Restraint • Open-Standard • Shunyaya

---

## One-Line Summary

Shunyaya Structural Irreversibility Layer (SSIL) introduces a deterministic finite irreversibility grammar `{R0, E0, I1, I2, C}` over system evolution, preserves classical magnitude via `phi((m,a,s,r)) = m`, governs continuation through `IRR_ADM(t)`, and requires exact replay equivalence `B_A = B_B` as the sole authority of conformance.
