# Customer Churn Analysis Web App Launcher (PowerShell)

Write-Host "========================================" -ForegroundColor Green
Write-Host "Customer Churn Analysis Web Dashboard" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Check if streamlit is installed
$streamlitCheck = pip show streamlit 2>$null
if (-not $streamlitCheck) {
    Write-Host "[INFO] Installing Streamlit..." -ForegroundColor Yellow
    pip install streamlit -q
}

Write-Host ""
Write-Host "[INFO] Starting Streamlit app..." -ForegroundColor Green
Write-Host "[INFO] The app will open in your browser at: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the app" -ForegroundColor Yellow
Write-Host ""

streamlit run app.py --logger.level=error
