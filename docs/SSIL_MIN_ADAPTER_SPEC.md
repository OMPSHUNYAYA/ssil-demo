# SSIL_MIN_ADAPTER_SPEC

## **Purpose**

Define the minimum deterministic adapter contract required to supply SSIL inputs.

An adapter prepares structural signals for SSIL.  
It does not implement SSIL logic.

---

## **Required SSIL Inputs**

At each tick `t`, the adapter MUST emit:

- `a(t) in [-1, +1]`
- `s(t) >= 0`

Optional passthrough:

- `m(t)` may be included as a read-only passthrough.  
  If included, it must remain unchanged.

SSIL does not modify `m(t)`:

- `phi((m,a,s,r)) = m`

---

## **Non-Claims**

Adapters do **NOT**:

- Modify domain equations
- Predict outcomes
- Classify irreversibility
- Implement SSIL logic
- Inject control logic
- Optimize behavior

Adapters only supply deterministic structural signals.

---

## **Deterministic Normalization Rules**

### **A) Alignment Lane**

Define a raw alignment signal `raw_a(t)` from the domain.

Normalization must be fixed and bounded:

- `a(t) = clamp(raw_a(t), -1, +1)`

No adaptive rescaling permitted.  
No dynamic normalization windows permitted.  
No data-dependent rescaling permitted.

The mapping from `raw_a(t)` to `a(t)` must be declared before execution.

---

### **B) Posture Accumulation**

Define a raw posture increment `raw_ds(t)` with:

- `raw_ds(t) >= 0`

Accumulate deterministically:

- `s(t) = s(t-1) + raw_ds(t)`

If clamping is used, `s_max` must be declared before execution:

- `s(t) = clamp(s(t), 0, s_max)`

`s_max` must remain fixed throughout the run.

No adaptive posture decay permitted.  
No hidden smoothing permitted.  
No probabilistic posture update permitted.

---

## **Canonical Demo Compatibility**

For compatibility with `ssil-demo` canonical profile:

- `H = 8`
- `delta-max = 0.15`
- `s-max = 10.0`
- `rho = 1.0`

Adapters must not mutate these values at runtime.

Derived parameter inside SSIL:

- `alpha = 1 / H`

Adapters do not compute `alpha`.

---

## **Determinism Requirements (Mandatory)**

Adapters must enforce:

- All constants declared prior to execution
- No randomness
- No time-dependent fields
- Fixed column ordering
- Fixed decimal formatting for outputs
- No nondeterministic iteration order
- No hidden state mutation

Trace generation must be reproducible.

Given identical raw inputs and identical constants,  
the adapter must produce identical output CSV.

---

## **Failure Mode**

If required domain fields are missing or malformed,  
the adapter MUST stop and report failure.

Adapters must not fabricate `a(t)` or `s(t)`.  
Adapters must not auto-correct malformed data silently.

Silent correction invalidates deterministic discipline.

---

## **Structural Boundary**

Adapters provide structural signals only.

SSIL performs:

- Irreversibility regime classification
- EdgeZero detection
- Recovery evaluation
- Continuation admissibility governance
- Replay verification

Adapters do not perform these operations.

---

**End of specification.**
