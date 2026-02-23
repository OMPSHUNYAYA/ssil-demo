# CASE_INDEX

---

## **Purpose**

Index of deterministic SSIL demo cases and their canonical fingerprints.

This document defines the **only canonical fingerprints recognized in this repository**.

Canonical authority is defined jointly by:

- The locked parameter surface  
- Deterministic replay identity (`B_A = B_B`)  
- Frozen artifacts under `reference_outputs/`

See root `README` → **Canonical Verification Profile (Locked)** for authoritative profile definition.

---

## **Core Invariants (Non-Negotiable)**

**Conservative invariant:**

`phi((m,a,s,r)) = m`

**Finite irreversibility grammar:**

`r(t) ∈ {R0, E0, I1, I2, C}`

**Continuation mapping:**

`IRR_ADM(t) ∈ {CONTINUE, ABSTAIN}`

**Replay rule:**

`B_A = B_B`

Byte-identical replay is the **sole authority of conformance**.

---

## **Locked Canonical Profile**

### (Common to All Official Fingerprints)

Canonical fingerprints are defined **only** under the exact parameter surface below:

- `H = 8`
- `delta-max = 0.15`
- `s-max = 10.0`
- `rho = 1.0`
- `beta = 0.5`
- `gamma = 0.5`
- `wA = 0.6`
- `wB = 0.2`
- `wS = 0.2`
- `eta = 0.25`

Derived:

- `alpha = 1 / H`

Only this parameter surface produces official canonical fingerprints.

Any deviation — even if deterministic — invalidates canonical fingerprint claims.

Runtime folders (`OUT/`, `OUT_VERIFY/`) do **not** define canonical artifacts.

Only frozen artifacts under `reference_outputs/` define canonical fingerprints.

---

## **Canonical Cases**

The following three cases are the only canonical cases defined in this repository.

No additional traces carry canonical fingerprint authority.

---

### **Case A: Baseline**

**Trace:**

`traces\trace_demo.csv`

**Expected Behavior:**

- Reversible structural drift  
- No EdgeZero event  
- Continuation remains permitted  

**Official Canonical Fingerprint:**

`CANONICAL_SHA256 = b3a7d70e085b5a7289a1c033b83c95dc3c8c8713b301c7401fc1ff07bbb8b839`

Fingerprint applies only under locked canonical profile.

---

### **Case B: EdgeZero**

**Trace:**

`traces\trace_edgezero.csv`

**Expected Behavior:**

- EdgeZero detected  
- Continuation gated deterministically  

**Killer Condition (must occur at least once):**

- `r(t) = E0`
- `IRR_ADM(t) = ABSTAIN`

**Official Canonical Fingerprint:**

`CANONICAL_SHA256 = 23596beb23014c492e4746156485989b1146cf21ba328f99bc948d2b8111a52e`

Fingerprint applies only under locked canonical profile.

---

### **Case C: Recovery Window**

**Trace:**

`traces\trace_recovery3.csv`

**Expected Behavior:**

- Recovery window signaling under bounded horizon  
- Deterministic posture relaxation behavior  

Replay identity must hold:

`B_A = B_B`

**Official Canonical Fingerprint:**

`CANONICAL_SHA256 = 14a5c61508b845a2bc503a3151fba8857973d0a75564fae880c0bcb15753168e`

Fingerprint applies only under locked canonical profile.

---

## **Fingerprint Discipline**

Canonical fingerprint claims require:

- Exact canonical parameter surface  
- Deterministic environment normalization  
- Byte-identical replay  
- No formatting drift  
- No hidden mutation  
- No artifact regeneration outside canonical profile  

If any of the above are violated, canonical claim is invalid.

There is no partial canonical state.

---

## **Authority Boundary**

Canonical fingerprint authority in this repository is limited strictly to:

- `baseline`
- `edgezero`
- `recovery3`

under the locked canonical profile.

All other executions are deterministic illustration runs and do **not** carry canonical fingerprint authority.

---

**End of index.**
