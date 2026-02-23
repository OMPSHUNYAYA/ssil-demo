#!/usr/bin/env bash
set -euo pipefail

# SSIL DEMO (Cross-platform)
# Deterministic replay proof: B_A = B_B

cd "$(dirname "$0")"

export PYTHONHASHSEED=0
export TZ=UTC
export LC_ALL=C
export LANG=C

ENGINE="engine/ssil_engine_v1_2.py"
OUTDIR="OUT"

H="8"
DELTA_MAX="0.15"
S_MAX="10.0"
BETA="0.5"
GAMMA="0.5"
WA="0.6"
WB="0.2"
WS="0.2"
ETA="0.25"
RHO="1.0"

CASE="${1:-baseline}"

if [[ "$CASE" == "baseline" ]]; then
  TRACE="traces/trace_demo.csv"
  OUT1="${OUTDIR}/baseline_run1.csv"
  OUT2="${OUTDIR}/baseline_run2.csv"
  LOG="${OUTDIR}/baseline_RUN_log.txt"
  H1="${OUTDIR}/baseline_run1.csv.sha256.txt"
  H2="${OUTDIR}/baseline_run2.csv.sha256.txt"
elif [[ "$CASE" == "edgezero" ]]; then
  TRACE="traces/trace_edgezero.csv"
  OUT1="${OUTDIR}/edgezero_run1.csv"
  OUT2="${OUTDIR}/edgezero_run2.csv"
  LOG="${OUTDIR}/edgezero_RUN_log.txt"
  H1="${OUTDIR}/edgezero_run1.csv.sha256.txt"
  H2="${OUTDIR}/edgezero_run2.csv.sha256.txt"
elif [[ "$CASE" == "recovery3" ]]; then
  TRACE="traces/trace_recovery3.csv"
  OUT1="${OUTDIR}/recovery3_run1.csv"
  OUT2="${OUTDIR}/recovery3_run2.csv"
  LOG="${OUTDIR}/recovery3_RUN_log.txt"
  H1="${OUTDIR}/recovery3_run1.csv.sha256.txt"
  H2="${OUTDIR}/recovery3_run2.csv.sha256.txt"
else
  echo "FAIL: Unknown case. Use: baseline | edgezero | recovery3"
  exit 1
fi

if [[ ! -f "$ENGINE" ]]; then
  echo "FAIL: Missing engine file: $ENGINE"
  exit 1
fi

if [[ ! -f "$TRACE" ]]; then
  echo "FAIL: Missing trace file: $TRACE"
  exit 1
fi

mkdir -p "$OUTDIR"

{
  echo "SSIL DEMO RUN START"
  echo "CASE: $CASE"
  echo "ENV: PYTHONHASHSEED=0 TZ=UTC LC_ALL=C LANG=C"
  echo "PARAMS: H=$H delta_max=$DELTA_MAX s_max=$S_MAX beta=$BETA gamma=$GAMMA wA=$WA wB=$WB wS=$WS eta=$ETA rho=$RHO"
  echo "TRACE: $TRACE"
  echo "ENGINE: $ENGINE"
} > "$LOG"

python "$ENGINE" \
  --in "$TRACE" --out "$OUT1" \
  --H "$H" --delta-max "$DELTA_MAX" --s-max "$S_MAX" \
  --beta "$BETA" --gamma "$GAMMA" --wA "$WA" --wB "$WB" --wS "$WS" --eta "$ETA" --rho "$RHO" \
  >> "$LOG" 2>&1

python "$ENGINE" \
  --in "$TRACE" --out "$OUT2" \
  --H "$H" --delta-max "$DELTA_MAX" --s-max "$S_MAX" \
  --beta "$BETA" --gamma "$GAMMA" --wA "$WA" --wB "$WB" --wS "$WS" --eta "$ETA" --rho "$RHO" \
  >> "$LOG" 2>&1

python -c "import hashlib,sys; p=sys.argv[1]; print(hashlib.sha256(open(p,'rb').read()).hexdigest())" "$OUT1" > "$H1"
python -c "import hashlib,sys; p=sys.argv[1]; print(hashlib.sha256(open(p,'rb').read()).hexdigest())" "$OUT2" > "$H2"

HASH1="$(cat "$H1" | tr -d '\r\n')"
HASH2="$(cat "$H2" | tr -d '\r\n')"

if [[ -z "$HASH1" || -z "$HASH2" ]]; then
  echo "SSIL_DEMO_RESULT: FAIL"
  echo "FAIL: Could not compute hash"
  exit 1
fi

# Byte identity check
if ! cmp -s "$OUT1" "$OUT2"; then
  {
    echo "SSIL_DEMO_RESULT: FAIL"
    echo "HASH1=$HASH1"
    echo "HASH2=$HASH2"
  } >> "$LOG"
  echo "SSIL_DEMO_RESULT: FAIL"
  exit 1
fi

# Hash equality check (redundant but explicit)
if [[ "$HASH1" != "$HASH2" ]]; then
  {
    echo "SSIL_DEMO_RESULT: FAIL"
    echo "HASH1=$HASH1"
    echo "HASH2=$HASH2"
  } >> "$LOG"
  echo "SSIL_DEMO_RESULT: FAIL"
  exit 1
fi

{
  echo "SSIL_DEMO_RESULT: PASS"
  echo "CANONICAL_SHA256=$HASH1"
} >> "$LOG"

echo "SSIL_DEMO_RESULT: PASS"
echo "CANONICAL_SHA256=$HASH1"
exit 0