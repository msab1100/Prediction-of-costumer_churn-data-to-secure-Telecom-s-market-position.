@echo off
REM Launch the Customer Churn Analysis Web App

echo ========================================
echo Customer Churn Analysis Web Dashboard
echo ========================================
echo.

REM Check if streamlit is installed
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing Streamlit...
    pip install streamlit -q
)

echo.
echo [INFO] Starting Streamlit app...
echo [INFO] The app will open in your browser at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the app
echo.

streamlit run app.py --logger.level=error
