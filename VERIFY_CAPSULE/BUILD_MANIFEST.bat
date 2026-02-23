@echo off
setlocal EnableExtensions

REM Move to repo root
cd /d "%~dp0..\" || exit /b 1

set "CAP=VERIFY_CAPSULE\CAPSULE"
set "SEEDS=VERIFY_CAPSULE\SEEDS"

REM Rebuild capsule directory
if exist "%CAP%" rmdir /s /q "%CAP%"
mkdir "%CAP%" || exit /b 1

REM Copy deterministic demo contents
xcopy /e /i /y docs "%CAP%\docs" >nul
xcopy /e /i /y engine "%CAP%\engine" >nul
xcopy /e /i /y traces "%CAP%\traces" >nul
xcopy /e /i /y reference_outputs "%CAP%\reference_outputs" >nul

copy /y README.txt "%CAP%\" >nul
copy /y RUN_DEMO.bat "%CAP%\" >nul
copy /y RUN_DEMO.sh "%CAP%\" >nul
copy /y RUN_ALL.bat "%CAP%\" >nul

REM Copy frozen demo manifests only if seed folder exists
if exist "%SEEDS%" (
  if exist "%SEEDS%\demo_manifest*.txt" (
    copy /y "%SEEDS%\demo_manifest*.txt" "%CAP%\" >nul
  )
  if exist "%SEEDS%\demo_manifest*.sha256" (
    copy /y "%SEEDS%\demo_manifest*.sha256" "%CAP%\" >nul
  )
)

REM Rebuild MANIFEST.sha256 deterministically
del /q VERIFY_CAPSULE\MANIFEST.sha256 2>nul

for /r "%CAP%" %%F in (*) do (
  certutil -hashfile "%%F" SHA256 | findstr /i /v "hash of CertUtil" >> VERIFY_CAPSULE\MANIFEST.sha256
)

exit /b 0