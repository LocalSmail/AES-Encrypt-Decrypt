@echo off
::Thx KDot
cd /d "%~dp0"

color 0a
title Requirements Installer
cls

set "python_path=%localappdata%\Programs\Python"

python --version
if not %errorlevel% == 0 (
    echo "Python is not installed or not added to path. Please install the newest version of python and add it to path"
    pause
    exit /b 1
)

python -m pip install -r requirements.txt

exit /b 0
