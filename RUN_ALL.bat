@echo off
setlocal

echo ========================================
echo SSIL DEMO FULL VERIFICATION
echo ========================================

echo.
echo Running baseline case...
call RUN_DEMO.bat baseline
if errorlevel 1 goto fail

echo.
echo Running edgezero case...
call RUN_DEMO.bat edgezero
if errorlevel 1 goto fail

echo.
echo Running recovery3 case...
call RUN_DEMO.bat recovery3
if errorlevel 1 goto fail

echo.
echo ----------------------------------------
echo Canonical Hashes (Reference Outputs)
echo ----------------------------------------

echo Baseline Hash (run1):
type reference_outputs\baseline_run1.csv.sha256.txt

echo.
echo EdgeZero Hash (run1):
type reference_outputs\edgezero_run1.csv.sha256.txt

echo.
echo Note: recovery3 reference output uses:
echo reference_outputs\recovery3_run.csv.sha256

echo.
echo ========================================
echo SSIL FULL DEMO RESULT: PASS
echo ========================================
exit /b 0

:fail
echo.
echo ========================================
echo SSIL FULL DEMO RESULT: FAIL
echo ========================================
exit /b 1