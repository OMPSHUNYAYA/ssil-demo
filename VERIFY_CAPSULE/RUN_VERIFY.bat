@echo off
setlocal EnableExtensions

REM Move to repo root
cd /d "%~dp0..\" || exit /b 1

set "RESULT=VERIFY_CAPSULE\VERIFY_RESULT.txt"

REM Start fresh result file
> "%RESULT%" (
  echo ========================================
  echo SSIL DEMO VERIFY CAPSULE RUN
  echo ========================================
  echo.
)

REM Run the full demo (root)
call RUN_ALL.bat >> "%RESULT%" 2>&1
if errorlevel 1 (
  >> "%RESULT%" echo VERIFY_CAPSULE_RESULT: FAIL
  if exist "%RESULT%" type "%RESULT%"
  exit /b 1
)

>> "%RESULT%" (
  echo.
  echo VERIFY_CAPSULE_RESULT: PASS
)

REM Build / refresh capsule manifest (authoritative sealing step)
call VERIFY_CAPSULE\BUILD_MANIFEST.bat >> "%RESULT%" 2>&1
if errorlevel 1 (
  >> "%RESULT%" echo VERIFY_CAPSULE_MANIFEST: FAIL
  if exist "%RESULT%" type "%RESULT%"
  exit /b 1
)

REM Confirm manifest exists (strong audit line)
if exist "VERIFY_CAPSULE\MANIFEST.sha256" (
  >> "%RESULT%" echo MANIFEST_BUILT: VERIFY_CAPSULE\MANIFEST.sha256
) else (
  >> "%RESULT%" echo FAIL: MANIFEST.sha256 not found after BUILD_MANIFEST.bat
  if exist "%RESULT%" type "%RESULT%"
  exit /b 1
)

REM Print results to console if present
if exist "%RESULT%" (
  type "%RESULT%"
) else (
  echo FAIL: Missing VERIFY_RESULT.txt
  exit /b 1
)

exit /b 0