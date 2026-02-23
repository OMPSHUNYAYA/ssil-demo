import argparse
import csv
import hashlib
import os
from decimal import Decimal, ROUND_HALF_UP

def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x

def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def q6(x):
    return Decimal(str(x)).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(1024 * 1024)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def read_trace_csv(path):
    rows = []
    with open(path, "r", newline="") as f:
        r = csv.DictReader(f)
        if r.fieldnames is None:
            raise ValueError("CSV has no header")
        fn = [x.strip() for x in r.fieldnames]
        has_t = "t" in fn
        if "a" not in fn or "s" not in fn:
            raise ValueError("CSV must have columns: a,s (optional: t)")
        for i, row in enumerate(r, start=1):
            a = float(row["a"])
            s = float(row["s"])
            t = int(row["t"]) if has_t and row.get("t") not in (None, "") else i
            rows.append((t, a, s))
    rows.sort(key=lambda x: x[0])
    return rows

def recovery_H(t_idx, H, dA_list, E_list):
    start = max(0, t_idx - H + 1)
    end = t_idx
    has_neg_dA = False
    for k in range(start, end + 1):
        if dA_list[k] < 0:
            has_neg_dA = True
            break
    if not has_neg_dA:
        return False
    if E_list[end] < E_list[start]:
        return False
    Emin = min(E_list[start:end+1])
    if Emin <= 0.0:
        return False
    return True

def edgezero_H(t_idx, H, dA_list, dE_list, A_list, E_list, recH):
    start = max(0, t_idx - H + 1)
    end = t_idx
    for k in range(start, end + 1):
        if dA_list[k] < 0:
            return False
    for k in range(start, end + 1):
        if dE_list[k] > 0:
            return False
    if not (A_list[end] > E_list[end]):
        return False
    if recH:
        return False
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_csv", required=True)
    ap.add_argument("--out", dest="out_csv", default="ssil_out.csv")
    ap.add_argument("--H", type=int, default=8)
    ap.add_argument("--delta-max", type=float, default=0.15)
    ap.add_argument("--s-max", type=float, default=10.0)
    ap.add_argument("--beta", type=float, default=0.5)
    ap.add_argument("--gamma", type=float, default=0.5)
    ap.add_argument("--wA", type=float, default=0.6)
    ap.add_argument("--wB", type=float, default=0.2)
    ap.add_argument("--wS", type=float, default=0.2)
    ap.add_argument("--eta", type=float, default=0.25)
    ap.add_argument("--rho", type=float, default=1.0)
    args = ap.parse_args()

    H = max(1, args.H)
    alpha = 1.0 / float(H)
    delta_max = float(args.delta_max)
    s_max = float(args.s_max)

    trace = read_trace_csv(args.in_csv)
    if len(trace) < 2:
        raise ValueError("Need at least 2 rows to compute da(t)")

    A_list = []
    E_list = []
    dA_list = []
    dE_list = []
    D_list = []
    B_list = []
    S_list = []
    out_list = []
    run_out_list = []
    P_out_list = []
    dA_plus_list = []
    dA_relief_list = []
    rec_list = []
    ez_list = []
    r_list = []
    adm_list = []

    A_prev = 0.0
    E_prev = 1.0
    prev_a = clamp(float(trace[0][1]), -1.0, 1.0)
    prev_abs_a = abs(prev_a)
    prev_dir_out = 0
    run_out = 0

    for i, (t, a, s) in enumerate(trace):
        a = clamp(float(a), -1.0, 1.0)
        s = float(s)
        if s < 0.0:
            s = 0.0

        if i == 0:
            da = 0.0
        else:
            da = a - prev_a

        D = clamp(abs(da) / delta_max if delta_max > 0 else 0.0, 0.0, 1.0)
        B = clamp(abs(a), 0.0, 1.0)
        S = clamp(s / s_max if s_max > 0 else 0.0, 0.0, 1.0)

        abs_a = abs(a)
        out = 1 if abs_a > prev_abs_a else 0

        dir_out = sgn(abs_a - prev_abs_a)
        if out == 1 and dir_out == prev_dir_out and dir_out != 0:
            run_out = run_out + 1
        elif out == 1 and dir_out != 0:
            run_out = 1
        else:
            run_out = 0

        P_out = clamp(float(run_out) / float(H), 0.0, 1.0)

        D_out = D * float(out)

        dA_plus = alpha * clamp(D_out + float(args.beta) * P_out + float(args.gamma) * S * float(out), 0.0, 1.0)

        calm = 1.0 - D
        center = 1.0 - B
        ease = 1.0 - S
        dA_relief = float(args.rho) * alpha * clamp(calm * center * ease, 0.0, 1.0)

        A = clamp(A_prev + dA_plus - dA_relief, 0.0, 1.0)

        C = clamp(1.0 - (float(args.wA) * A + float(args.wB) * B + float(args.wS) * S), 0.0, 1.0)
        E = clamp((1.0 - float(args.eta)) * E_prev + float(args.eta) * C, 0.0, 1.0)

        if i == 0:
            dA = 0.0
            dE = 0.0
        else:
            dA = A - A_prev
            dE = E - E_prev

        A_list.append(A)
        E_list.append(E)
        dA_list.append(dA)
        dE_list.append(dE)
        D_list.append(D)
        B_list.append(B)
        S_list.append(S)
        out_list.append(out)
        run_out_list.append(run_out)
        P_out_list.append(P_out)
        dA_plus_list.append(dA_plus)
        dA_relief_list.append(dA_relief)

        A_prev = A
        E_prev = E
        prev_a = a
        prev_abs_a = abs_a
        prev_dir_out = dir_out if out == 1 else 0

    order = {"R0": 0, "E0": 1, "I1": 2, "I2": 3, "C": 4}
    by_order = ["R0", "E0", "I1", "I2", "C"]
    r_prev = "R0"

    for i in range(len(trace)):
        recH = recovery_H(i, H, dA_list, E_list)
        ezH = edgezero_H(i, H, dA_list, dE_list, A_list, E_list, recH)
        rec_list.append(recH)
        ez_list.append(ezH)

        A = A_list[i]
        Erev = E_list[i]
        gap = A - Erev

        if ezH:
            r_raw = "E0"
        else:
            if gap <= 0.0:
                r_raw = "R0"
            else:
                if (A < 0.85) and (gap < 0.20):
                    r_raw = "I1"
                elif (A < 0.97) and (gap < 0.35):
                    r_raw = "I2"
                else:
                    r_raw = "C"

        r = by_order[max(order[r_prev], order[r_raw])]
        r_prev = r

        adm = "ABSTAIN" if r in ("E0", "I1", "I2", "C") else "CONTINUE"
        r_list.append(r)
        adm_list.append(adm)

    out_path = args.out_csv
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "t","a","s",
            "da","D","B","S",
            "out","run_out","P_out",
            "dA_plus","dA_relief",
            "A","E_rev","dA","dE",
            "Recovery_H","EdgeZero_H",
            "r","IRR_ADM"
        ])
        for i, (t, a, s) in enumerate(trace):
            a0 = clamp(float(a), -1.0, 1.0)
            s0 = max(0.0, float(s))
            da = 0.0 if i == 0 else a0 - clamp(float(trace[i-1][1]), -1.0, 1.0)
            w.writerow([
                int(t),
                f"{q6(a0):+f}",
                f"{q6(s0):f}",
                f"{q6(da):+f}",
                f"{q6(D_list[i]):f}",
                f"{q6(B_list[i]):f}",
                f"{q6(S_list[i]):f}",
                int(out_list[i]),
                int(run_out_list[i]),
                f"{q6(P_out_list[i]):f}",
                f"{q6(dA_plus_list[i]):f}",
                f"{q6(dA_relief_list[i]):f}",
                f"{q6(A_list[i]):f}",
                f"{q6(E_list[i]):f}",
                f"{q6(dA_list[i]):+f}",
                f"{q6(dE_list[i]):+f}",
                "TRUE" if rec_list[i] else "FALSE",
                "TRUE" if ez_list[i] else "FALSE",
                r_list[i],
                adm_list[i]
            ])

    digest = sha256_file(out_path)
    with open(out_path + ".sha256", "w", newline="") as f:
        f.write(digest + "  " + os.path.basename(out_path) + "\n")

if __name__ == "__main__":
    main()