⭐ SSIL Reference Outputs (Frozen Conformance Evidence)

This folder contains frozen conformance artifacts produced by executing
the Shunyaya Structural Irreversibility Layer (SSIL) engine
under declared deterministic parameters.

These artifacts demonstrate deterministic irreversibility classification
under bounded-horizon structural discipline.

They are provided for audit transparency and inspection only.

They are not required to execute SSIL,
and they do not replace independent verification.

What These Reference Outputs Prove

The included bundles demonstrate SSIL’s conformance-critical property:

B_A = B_B

Meaning:

Two independent executions
under identical declared inputs and locked parameters
produce byte-identical artifacts.

Replay determinism is enforced at the artifact level
via SHA-256 sealed output files.

Each conformance case enforces:

Finite irreversibility regime set
R = {R0, E0, I1, I2, C}

Bounded-horizon irreversibility logic

W_H(t) = {t-H+1, ..., t}

Deterministic Recovery predicate

Recovery_H(t) ∈ {TRUE, FALSE}

Deterministic EdgeZero_H(t) predicate

EdgeZero_H(t) ∈ {TRUE, FALSE}

Structural envelope comparison

A(t) > E_rev(t)

This is deterministic irreversibility classification
by replay evidence — not interpretation.

What These Reference Outputs Contain

This folder includes:

Baseline case outputs

baseline_run1.csv

baseline_run2.csv

Corresponding SHA-256 files

EdgeZero case outputs

edgezero_run1.csv

edgezero_run2.csv

Corresponding SHA-256 files

Recovery window case

recovery3_run.csv

recovery3_run.csv.sha256

Together, these demonstrate:

Deterministic asymmetry accumulation

Deterministic reversibility envelope evolution

Deterministic Recovery predicate evaluation

Deterministic EdgeZero_H(t) onset detection

Byte-level artifact sealing

No probabilistic processes are used.
No adaptive thresholds are permitted.
No timestamps are embedded.
No external proprietary datasets are redistributed.

All traces included are deterministic control traces
or publicly reproducible structural test inputs.

What These Reference Outputs Do NOT Claim

These artifacts do not:

Perform prediction

Modify domain equations

Replace physical law

Inject control authority

Guarantee safety

Provide medical, seismic, financial, or engineering advice

Certify real-world risk mitigation

SSIL operates strictly at the structural irreversibility governance layer.

How to Reproduce (Manual Demonstration)

From project root (ssil-demo):

Canonical profile:

H = 8
delta-max = 0.15
s-max = 10.0
rho = 1.0

Example replay test (Baseline case):

Windows:

python engine\ssil_engine_v1_2.py --in traces\trace_demo.csv --out run1.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 1.0
python engine\ssil_engine_v1_2.py --in traces\trace_demo.csv --out run2.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 1.0

fc /b run1.csv run2.csv

Expected:

no differences encountered

This reproduces:

B_A = B_B

Byte identity is mandatory.
There is no tolerance layer.

Authoritative Verification Method

The authoritative verification path is the included capsule:

VERIFY_CAPSULE\RUN_VERIFY.bat

Expected result:

SSIL_CAPSULE_RESULT: PASS

The capsule verifies:

Replay identity

Canonical parameter lock

Canonical fingerprint match

Environment normalization

Deterministic profile immutability

Fixed hyperparameter disclosure compliance

The capsule result is binary:

PASS or FAIL.

No partial success is possible.

Deterministic Claim Level

SSIL satisfies deterministic discipline at two independent layers:

Core irreversibility replay identity

B_A = B_B

Sealed artifact integrity
(SHA-256 fingerprint lock)

The frozen reference bundle exists to:

Provide audit transparency

Demonstrate deterministic execution

Allow artifact inspection

Prove byte-level reproducibility

It does not replace independent replay verification.

SSIL operates as an execution-first deterministic irreversibility governance layer under strict replay discipline.

Conformance is binary.