@echo off
echo Installing Python dependencies...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install Python dependencies. Pausing...
    pause
)

echo Installing Node.js dependencies...
cd Zero-Tool/nuke-bot
call npm i
if %errorlevel% neq 0 (
    echo Failed to install Node.js dependencies. Pausing...
    pause
)

cd ../..
start.bat
