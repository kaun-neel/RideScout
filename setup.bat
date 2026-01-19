@echo off
echo ============================================
echo   Cab Price Comparison Setup Script
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 3 is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✓ Python found
python --version
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

if errorlevel 1 (
    echo ❌ Failed to create virtual environment.
    pause
    exit /b 1
)

echo ✓ Virtual environment created
echo.

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

if errorlevel 1 (
    echo ❌ Failed to activate virtual environment.
    pause
    exit /b 1
)

echo ✓ Virtual environment activated
echo.

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies.
    pause
    exit /b 1
)

echo ✓ Dependencies installed
echo.

REM Create .env file if it doesn't exist
if not exist .env (
    echo 📝 Creating .env file...
    copy .env.example .env
    echo ✓ .env file created
    echo.
    echo ⚠️  IMPORTANT: Edit .env and add your OpenRouter API key!
    echo    Get your key from: https://openrouter.ai/keys
) else (
    echo ✓ .env file already exists
)

echo.
echo ============================================
echo   Setup Complete! 🎉
echo ============================================
echo.
echo Next steps:
echo 1. Edit .env and add your OpenRouter API key
echo 2. Start your Android emulator with Uber, Ola, Rapido installed
echo 3. Enable Droidrun Portal accessibility service
echo 4. Run: python cab_price_comparison.py
echo.
echo For detailed instructions, see README.md
echo.
pause
