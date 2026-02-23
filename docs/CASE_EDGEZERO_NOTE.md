# CASE_EDGEZERO_NOTE

---

## **Purpose**

Record that the demo suite includes an **EdgeZero trigger case** where SSIL issues `ABSTAIN`.

---

## **Trace File**

`traces\trace_edgezero.csv`

---

## **Run Output**

`OUT\edgezero_run.csv`

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

## **Observed Killer Condition (Minimum)**

At ticks `t = 6..12`:

- `EdgeZero_H = TRUE`
- `r(t) = E0`
- `IRR_ADM(t) = ABSTAIN`

This demonstrates **deterministic EdgeZero boundary detection** and **continuation gating**.

---

## **Non-Claims**

- No prediction  
- No optimization  
- No equation modification  

This is a **structural governance demonstration only**.

---

**End of note.**
