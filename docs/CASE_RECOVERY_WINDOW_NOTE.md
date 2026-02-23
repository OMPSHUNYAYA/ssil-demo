# CASE_RECOVERY_WINDOW_NOTE

---

## **Purpose**

Record a demo case where **EdgeZero triggers**, and later a **Recovery window becomes TRUE**, while continuation remains gated.

---

## **Trace File**

`traces\trace_recovery3.csv`

---

## **Run Output**

`OUT\recovery3_run.csv`

---

## **Locked Hyperparameters**

- `H = 8`
- `delta_max = 0.15`
- `s_max = 10.0`
- `beta = 0.5`
- `gamma = 0.5`
- `wA = 0.6`
- `wB = 0.2`
- `wS = 0.2`
- `eta = 0.25`
- `rho = 1.0`

Derived parameter:

- `alpha = 1 / H`

---

## **Observed Events**

### **Boundary Trigger**

`t = 6..8` shows:

- `r(t) = E0`
- `IRR_ADM(t) = ABSTAIN`

---

### **Recovery Window**

`t = 13..16` shows:

- `Recovery_H = TRUE`

---

## **Continuation Outcome**

No `CONTINUE` occurs after the boundary in this case.

This demonstrates that a **recovery window signal does not automatically imply continuation permission**.

Continuation remains governed by deterministic irreversibility classification.

---

## **Non-Claims**

- No prediction  
- No optimization  
- No equation modification  

This is a **structural governance demonstration only**.

---

**End of note.**
