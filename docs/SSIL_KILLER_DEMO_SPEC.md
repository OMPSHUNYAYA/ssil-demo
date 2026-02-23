# SSIL_KILLER_DEMO_SPEC

## **Purpose**

Define the minimum “killer demo” requirements for `ssil-demo`.

This demo must prove, deterministically:

- Structural irreversibility onset can be detected as `E0`
- Continuation governance can issue `ABSTAIN` at onset
- Results are replay-verifiable under `B_A = B_B`
- Classical magnitude is not modified

`phi((m,a,s,r)) = m`

---

## **Core Invariants (Non-Negotiable)**

- `r(t) ∈ {R0, E0, I1, I2, C}`
- `IRR_ADM(t) ∈ {CONTINUE, ABSTAIN}`
- `W_H(t) = {t-H+1, ..., t}`

Replay rule:

- `B_A = B_B`

These must remain true under replay.

---

## **Canonical Demo Profile**

Canonical fingerprints are defined only under the locked canonical profile defined in `README`:

- `H = 8`
- `delta-max = 0.15`
- `s-max = 10.0`
- `rho = 1.0`

Derived:

- `alpha = 1 / H`

Only this profile produces canonical conformance fingerprints.

Other parameter selections remain deterministic but are considered illustration runs.

---

## **Minimum Demo Behavior (Must Occur at Least Once)**

### **A) EdgeZero Onset**

At some tick `t`, the demo output must include:

- `r(t) = E0`
- `IRR_ADM(t) = ABSTAIN`

This demonstrates deterministic irreversible boundary detection.

The provided trace:

- `traces/trace_edgezero.csv`

must produce at least one such onset under the canonical profile.

---

### **B) Deterministic Replay**

Two independent executions under identical inputs and parameters must produce byte-identical CSV outputs:

- `B_A = B_B`

Binary comparison must show:

- `no differences encountered`

SHA-256 hashes must match exactly.

---

### **C) Parameter Lock**

The demo must explicitly declare and lock the hyperparameter surface:

- `H`
- `delta_max`
- `s_max`
- `rho`

Derived:

- `alpha = 1 / H`

No adaptive tuning permitted.  
No runtime hyperparameter mutation permitted.

---

## **Mandatory Artifact Bundle**

Each killer demo verification must include:

- Input trace CSV (e.g., `traces/trace_edgezero.csv`)
- Output run A CSV
- Output run B CSV
- SHA-256 hash of each output
- Binary comparison result confirming identity
- Minimal run instructions (exact command used)

If claiming canonical conformance:

- Canonical fingerprint must match official reference

---

## **Deterministic Discipline Requirements**

The demo must satisfy:

- No randomness
- No adaptive thresholds
- No timestamp embedding
- No nondeterministic ordering
- No hidden environment dependencies

Environment normalization recommended:

- `PYTHONHASHSEED = 0`
- `TZ = UTC`
- `LC_ALL = C`
- `LANG = C`

---

## **Non-Claims**

This demo does **NOT**:

- Predict failure
- Guarantee safety
- Optimize outcomes
- Inject control logic
- Modify domain equations

It demonstrates deterministic continuation governance only.

---

## **Conformance Authority**

Conformance is defined strictly by:

- `B_A = B_B`

If replay identity fails, the demo fails.

There is no tolerance layer.

---

**End of specification.**
