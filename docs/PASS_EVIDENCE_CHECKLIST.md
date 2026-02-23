# PASS_EVIDENCE_CHECKLIST

Every SSIL demo PASS must include deterministic replay evidence.

Conformance is binary.

There is no partial PASS.

---

# 1. Canonical Profile (If Claiming Official Conformance)

Canonical fingerprint claims are valid only under the locked canonical profile defined in the `README`.

## Locked Parameter Surface

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

---

# 2. Required Replay Condition

Two independent executions under identical inputs and identical parameters must produce:

`B_A = B_B`

Meaning:

`SHA256(run1.csv) == SHA256(run2.csv)`

Byte identity is mandatory.  
No tolerance is permitted.  
No approximate equality is permitted.

If replay identity fails, PASS is invalid.

---

# 3. Verification Paths

SSIL provides two authoritative verification paths.

Both require replay identity.

---

## A. Cross-Platform Verification (Preferred for CI / All OS)

From repository root:

`python verify.py`

Expected final line:

`SSIL_VERIFY_RESULT: PASS`

`verify.py` enforces:

- Two-run replay identity per case  
- Canonical fingerprint match (`baseline`, `edgezero`, `recovery3`)  
- Canonical parameter lock  
- Deterministic artifact comparison  
- Isolation from frozen reference outputs  

Outputs written to:

`OUT_VERIFY/`

`reference_outputs/` remains unchanged.

If replay identity or fingerprint match fails:

`SSIL_VERIFY_RESULT: FAIL`

No partial success is possible.

---

## B. Capsule Verification (Windows Official Batch Path)

From repository root:

`VERIFY_CAPSULE\RUN_VERIFY.bat`

Expected final line:

`VERIFY_CAPSULE_RESULT: PASS`

The capsule verifies:

- Replay identity  
- Canonical parameter lock  
- Canonical fingerprint match  
- Environment normalization  
- Deterministic profile immutability  

If replay identity fails:

`VERIFY_CAPSULE_RESULT: FAIL`

No partial success is possible.

---

# 4. Manual Replay Path (Non-Automated)

If performing manual replay outside `verify.py` or capsule, evidence must include:

Two independent output files:

- `run1.csv`
- `run2.csv`

Binary comparison result showing:

`no differences encountered`

SHA-256 hashes for both outputs.

Proof that:

`SHA256(run1.csv) == SHA256(run2.csv)`

If claiming canonical profile verification, also record:

`CANONICAL_SHA256(run1.csv) = <official_hash>`

Canonical hashes are defined only for:

- `baseline`
- `edgezero`
- `recovery3`

under the locked canonical profile.

---

# 5. Trace-Level Coverage (Demo Scope)

The `ssil-demo` repository includes three deterministic canonical cases:

**Baseline case**  
Input: `traces/trace_demo.csv`

**EdgeZero case**  
Input: `traces/trace_edgezero.csv`

**Recovery window case**  
Input: `traces/trace_recovery3.csv`

Each case must independently satisfy:

`B_A = B_B`

Replay identity must hold per case.

Failure in any single case invalidates overall PASS.

---

# 6. Reference Outputs (Frozen Evidence)

Frozen canonical artifacts exist under:

`reference_outputs/`

**Baseline**
- `baseline_run1.csv`
- `baseline_run2.csv`

**EdgeZero**
- `edgezero_run1.csv`
- `edgezero_run2.csv`

**Recovery**
- `recovery3_run.csv`

Each has corresponding SHA-256 seal files.

These artifacts:

- Define canonical fingerprints  
- Serve as audit references  
- Do not replace independent replay verification  

Canonical authority resides only in frozen artifacts under `reference_outputs/`.

Runtime folders (`OUT/`, `OUT_VERIFY/`) do not define canonical authority.

---

# 7. Structural Requirements (Non-Negotiable)

All PASS claims must satisfy:

Finite irreversibility grammar:

`R = {R0, E0, I1, I2, C}`

Conservative invariant:

`phi((m,a,s,r)) = m`

Bounded horizon:

`W_H(t) = {t-H+1, ..., t}`

Deterministic continuation mapping:

`IRR_ADM(t) ∈ {CONTINUE, ABSTAIN}`

Replay identity:

`B_A = B_B`

If any invariant is violated, PASS is invalid.

---

# 8. Deterministic Discipline

All PASS claims require:

- No randomness  
- No probabilistic inference  
- No adaptive thresholds  
- No timestamp embedding  
- No environment-dependent mutation  
- No formatting drift  
- No hidden artifact mutation  

If any of the above occur, PASS is invalid.

---

# 9. Binary Conformance Rule

SSIL conformance is defined strictly by:

`B_A = B_B`

Replay equivalence is structural proof.

If replay identity holds and canonical fingerprint matches (when claiming canonical profile), PASS is valid.

Otherwise:

FAIL.

There is no partial compliance.

---

**End of checklist.**
