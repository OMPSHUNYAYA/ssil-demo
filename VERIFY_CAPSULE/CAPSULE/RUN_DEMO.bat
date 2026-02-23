@echo off
setlocal EnableExtensions
cd /d "%~dp0"

set "PYTHONHASHSEED=0"
set "TZ=UTC"
set "LC_ALL=C"
set "LANG=C"

set "ENGINE=engine\ssil_engine_v1_2.py"
set "OUTDIR=OUT"

set "H=8"
set "DELTA_MAX=0.15"
set "S_MAX=10.0"
set "BETA=0.5"
set "GAMMA=0.5"
set "WA=0.6"
set "WB=0.2"
set "WS=0.2"
set "ETA=0.25"
set "RHO=1.0"

set "CASE=%~1"
if "%CASE%"=="" set "CASE=baseline"

if /i "%CASE%"=="baseline" (
  set "TRACE=traces\trace_demo.csv"
  set "OUT1=%OUTDIR%\baseline_run1.csv"
  set "OUT2=%OUTDIR%\baseline_run2.csv"
  set "LOG=%OUTDIR%\baseline_RUN_log.txt"
  set "H1=%OUTDIR%\baseline_run1.csv.sha256.txt"
  set "H2=%OUTDIR%\baseline_run2.csv.sha256.txt"
) else if /i "%CASE%"=="edgezero" (
  set "TRACE=traces\trace_edgezero.csv"
  set "OUT1=%OUTDIR%\edgezero_run1.csv"
  set "OUT2=%OUTDIR%\edgezero_run2.csv"
  set "LOG=%OUTDIR%\edgezero_RUN_log.txt"
  set "H1=%OUTDIR%\edgezero_run1.csv.sha256.txt"
  set "H2=%OUTDIR%\edgezero_run2.csv.sha256.txt"
) else if /i "%CASE%"=="recovery3" (
  set "TRACE=traces\trace_recovery3.csv"
  set "OUT1=%OUTDIR%\recovery3_run1.csv"
  set "OUT2=%OUTDIR%\recovery3_run2.csv"
  set "LOG=%OUTDIR%\recovery3_RUN_log.txt"
  set "H1=%OUTDIR%\recovery3_run1.csv.sha256.txt"
  set "H2=%OUTDIR%\recovery3_run2.csv.sha256.txt"
) else (
  echo FAIL: Unknown case. Use: baseline or edgezero or recovery3
  exit /b 1
)

if not exist "%ENGINE%" (
  echo FAIL: Missing engine file
  exit /b 1
)

if not exist "%TRACE%" (
  echo FAIL: Missing trace file: %TRACE%
  exit /b 1
)

if not exist "%OUTDIR%" (
  mkdir "%OUTDIR%" >nul 2>&1
)

echo SSIL DEMO RUN START > "%LOG%"
echo CASE: %CASE% >> "%LOG%"
echo ENV: PYTHONHASHSEED=0 TZ=UTC LC_ALL=C LANG=C >> "%LOG%"
echo PARAMS: H=%H% delta_max=%DELTA_MAX% s_max=%S_MAX% beta=%BETA% gamma=%GAMMA% wA=%WA% wB=%WB% wS=%WS% eta=%ETA% rho=%RHO% >> "%LOG%"
echo TRACE: %TRACE% >> "%LOG%"
echo ENGINE: %ENGINE% >> "%LOG%"

python "%ENGINE%" --in "%TRACE%" --out "%OUT1%" --H %H% --delta-max %DELTA_MAX% --s-max %S_MAX% --beta %BETA% --gamma %GAMMA% --wA %WA% --wB %WB% --wS %WS% --eta %ETA% --rho %RHO% >> "%LOG%" 2>&1
if errorlevel 1 (
  echo FAIL: Engine run A failed
  echo SSIL_DEMO_RESULT: FAIL >> "%LOG%"
  exit /b 1
)

python "%ENGINE%" --in "%TRACE%" --out "%OUT2%" --H %H% --delta-max %DELTA_MAX% --s-max %S_MAX% --beta %BETA% --gamma %GAMMA% --wA %WA% --wB %WB% --wS %WS% --eta %ETA% --rho %RHO% >> "%LOG%" 2>&1
if errorlevel 1 (
  echo FAIL: Engine run B failed
  echo SSIL_DEMO_RESULT: FAIL >> "%LOG%"
  exit /b 1
)

python -c "import hashlib,sys; p=sys.argv[1]; print(hashlib.sha256(open(p,'rb').read()).hexdigest())" "%OUT1%" > "%H1%"
python -c "import hashlib,sys; p=sys.argv[1]; print(hashlib.sha256(open(p,'rb').read()).hexdigest())" "%OUT2%" > "%H2%"

set /p HASH1=<"%H1%"
set /p HASH2=<"%H2%"

if not defined HASH1 (
  echo FAIL: Could not compute hash for run1
  echo SSIL_DEMO_RESULT: FAIL >> "%LOG%"
  exit /b 1
)

if not defined HASH2 (
  echo FAIL: Could not compute hash for run2
  echo SSIL_DEMO_RESULT: FAIL >> "%LOG%"
  exit /b 1
)

fc /b "%OUT1%" "%OUT2%" >nul
if errorlevel 1 (
  echo SSIL_DEMO_RESULT: FAIL
  echo SSIL_DEMO_RESULT: FAIL >> "%LOG%"
  echo HASH1=%HASH1% >> "%LOG%"
  echo HASH2=%HASH2% >> "%LOG%"
  exit /b 1
)

if /i not "%HASH1%"=="%HASH2%" (
  echo SSIL_DEMO_RESULT: FAIL
  echo SSIL_DEMO_RESULT: FAIL >> "%LOG%"
  echo HASH1=%HASH1% >> "%LOG%"
  echo HASH2=%HASH2% >> "%LOG%"
  exit /b 1
)

echo SSIL_DEMO_RESULT: PASS
echo CANONICAL_SHA256=%HASH1%
echo SSIL_DEMO_RESULT: PASS >> "%LOG%"
echo CANONICAL_SHA256=%HASH1% >> "%LOG%"
exit /b 0