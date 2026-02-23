# SSIL_DEMO_EXECUTION_SPEC

## **Purpose**

Define the deterministic execution protocol for `ssil-demo` runs.

---

## **Scope**

This demo proves deterministic irreversibility classification under fixed parameters.

It establishes replay-verifiable structural governance discipline.

---

## **Non-Claims**

This demo does **NOT** predict failure.  
This demo does **NOT** guarantee safety.  
This demo does **NOT** optimize or control a domain system.

This demo demonstrates deterministic structural governance only.

---

## **Core Invariants (Non-Negotiable)**

- `phi((m,a,s,r)) = m`
- `r(t) ∈ {R0, E0, I1, I2, C}`
- `IRR_ADM(t) ∈ {CONTINUE, ABSTAIN}`
- `W_H(t) = {t-H+1, ..., t}`

Replay rule:

- `B_A = B_B`

All must remain true under replay.

---

## **Input Requirements**

A deterministic trace file containing at least:

- `a in [-1, +1]`
- `s >= 0`

Optional column:

- `t` (if absent, row index is used)

Trace files included in this demo:

- `traces/trace_demo.csv`
- `traces/trace_edgezero.csv`
- `traces/trace_recovery3.csv`

---

## **Locked Hyperparameters**

Each run MUST explicitly declare and lock:

- `H`
- `delta_max`
- `s_max`
- `rho`

Derived parameter:

- `alpha = 1 / H`

Canonical demo profile:

- `H = 8`
- `delta-max = 0.15`
- `s-max = 10.0`
- `rho = 1.0`

Only this profile produces official canonical fingerprints.

Other parameter combinations remain deterministic but are considered illustration runs.

---

## **Deterministic Environment Normalization (Required)**

Before execution:

- `PYTHONHASHSEED = 0`
- `TZ = UTC`
- `LC_ALL = C`
- `LANG = C`

No timestamps allowed in output CSV.  
No nondeterministic ordering permitted.  
No hidden randomness permitted.

---

## **Execution Protocol (Mandatory)**

From repository root (`ssil-demo`):

### **Run execution A**

```
python engine\ssil_engine_v1_2.py --in traces\trace_demo.csv --out run1.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 1.0
```

Compute SHA-256 of `run1.csv`.

---

### **Run execution B (identical parameters)**

```
python engine\ssil_engine_v1_2.py --in traces\trace_demo.csv --out run2.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 1.0
```

Compute SHA-256 of `run2.csv`.

---

### **Binary compare**

```
fc /b run1.csv run2.csv
```

---

## **PASS Condition**

PASS if and only if:

- `SHA256(run1.csv) == SHA256(run2.csv)`
- file sizes match
- no runtime errors occurred

This establishes:

- `B_A = B_B`

Replay identity is authoritative proof of conformance.

---

## **FAIL Condition**

Any mismatch in bytes → FAIL.  
Any missing parameter disclosure → FAIL.  
Any adaptive tuning → FAIL.  
Any runtime time dependency → FAIL.  
Any nondeterministic artifact mutation → FAIL.

There is no tolerance layer.

---

## **Authoritative Verification Path**

The preferred verification method is:

`VERIFY_CAPSULE\RUN_VERIFY.bat`

Expected result:

`VERIFY_CAPSULE_RESULT: PASS`

The capsule verifies replay identity, canonical parameter lock, fingerprint integrity, and deterministic discipline.

---

**End of specification.**
