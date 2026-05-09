# Customer Churn Analysis Web Dashboard

A modern, interactive web-based dashboard for analyzing customer churn data built with Streamlit.

## Features

✨ **Interactive Dashboard**
- Real-time data upload and analysis
- Multiple tabs for different analysis views
- Beautiful, responsive UI

📊 **Data Visualization**
- Churn distribution pie charts
- Internet service distribution bar charts
- Confusion matrices for model evaluation
- All visualizations update dynamically

🤖 **Machine Learning**
- 3 different neural network models
- Automatic feature selection
- Train/validation accuracy metrics
- Confusion matrices and performance metrics

📁 **Flexible Data Input**
- Load sample data automatically
- Upload custom CSV files
- Upload custom Excel files (.xlsx, .xls)
- Data validation and error handling

## Quick Start

### Option 1: Run with Python (Recommended)
```bash
python run_app.py
```
The app will automatically:
- Install Streamlit (if needed)
- Start the web server
- Open your browser at http://localhost:8501

### Option 2: Run with Batch File (Windows)
```bash
run_app.bat
```

### Option 3: Run with PowerShell (Windows)
```powershell
.\run_app.ps1
```

### Option 4: Manual Streamlit Launch
```bash
pip install streamlit
streamlit run app.py
```

## Dashboard Tabs

### 📈 Overview
- Dataset statistics (record count, feature count, churn rate)
- First 10 rows of data
- Column names and data types

### 🔍 Analysis
- Total male customers
- Customers with DSL internet
- Female senior citizens using mailed checks
- Customers with low tenure or low charges
- Summary statistics for all numeric columns

### 📊 Visualizations
- **Churn Distribution**: Pie chart showing retention vs churn
- **Internet Service**: Bar chart of service types (if available)

### 🤖 Models
- **Model 1**: Single feature neural network
  - Train/validation accuracy
  - Confusion matrix
  
- **Model 2**: Regularized neural network
  - L2 regularization for better generalization
  - Confusion matrix
  
- **Model 3**: Multi-feature neural network
  - Uses up to 3 features
  - Confusion matrix

## Data Input

### Using Sample Data
1. Place `sample_churn_dataset.xlsx` or `.csv` in the project directory
2. Select "Sample Data" from the sidebar
3. Analysis starts automatically

### Upload Custom Data
1. Select "Upload CSV" or "Upload Excel" from sidebar
2. Choose your file
3. Analysis starts immediately

### Data Requirements
Your dataset must have:
- **Churn column**: Binary target variable (Yes/No or 1/0)
- Any other columns as features
- Can be any size (tested with 10-1000+ rows)

### Example CSV Format
```csv
gender,tenure,MonthlyCharges,TotalCharges,Churn
Male,12,50.5,606,No
Female,24,75.2,1804.8,No
Male,6,45.0,270,Yes
```

## System Requirements

- Python 3.8+
- Windows, macOS, or Linux
- Web browser (Chrome, Firefox, Safari, Edge)
- ~200MB disk space for dependencies

## Installation

### 1. Install Dependencies
```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn openpyxl
```

Or use the requirements file (if created):
```bash
pip install -r requirements_app.txt
```

### 2. Run the App
```bash
python run_app.py
```

## File Structure

```
cosutmer_churn/
├── app.py                 # Streamlit web app
├── main.py               # Command-line analysis script
├── run_app.py            # Python launcher
├── run_app.bat           # Windows batch launcher
├── run_app.ps1           # PowerShell launcher
├── test_data.csv         # Sample CSV for testing
├── sample_churn_dataset.xlsx  # Sample Excel data
├── requirements.txt      # Command-line dependencies
└── README.md             # Documentation
```

## Browser Access

Once running, open your browser and go to:
```
http://localhost:8501
```

The dashboard is only accessible locally unless configured otherwise.

## Troubleshooting

### "Streamlit not found" error
```bash
pip install streamlit
```

### "No data source found" error
- Ensure sample file exists in current directory, OR
- Use the file uploader in the sidebar

### "Churn column not found" error
- Your CSV/Excel must have a column named 'Churn'
- Column names are case-sensitive

### Browser won't open automatically
- Manually navigate to http://localhost:8501
- Or use the URL printed in the terminal

### Port 8501 already in use
```bash
streamlit run app.py --server.port=8502
```

## Performance

- Small datasets (10-100 rows): < 5 seconds
- Medium datasets (100-1000 rows): 5-10 seconds
- Large datasets (1000+ rows): 10-30 seconds

## Features Comparison

| Feature | app.py (Web) | main.py (CLI) |
|---------|---------|----------|
| Interactive UI | ✓ | ✗ |
| Real-time analysis | ✓ | ✗ |
| File upload | ✓ | ✓ |
| Visualizations | ✓ | ✓ |
| Models | ✓ | ✓ |
| Browser view | ✓ | ✗ |

## Advanced Usage

### Run on different port
```bash
streamlit run app.py --server.port=8080
```

### Disable browser auto-open
```bash
streamlit run app.py --server.headless true
```

### Custom theme
Edit streamlit config (created automatically):
- Windows: `%userprofile%\.streamlit\config.toml`
- macOS/Linux: `~/.streamlit/config.toml`

## Tips & Tricks

1. **File Upload**: You can drag and drop files into the upload area
2. **Keyboard Shortcuts**: 
   - 'R' to rerun the app
   - 'C' to clear cache
3. **Mobile**: The dashboard is responsive and works on tablets/phones
4. **Sharing**: Run with `--server.enableXsrfProtection=false` to share easily

## Notes

- All analysis is performed on your local machine
- No data is sent to external servers
- Browser cache is used for faster reloads
- Multiple users can access if network sharing is enabled

## Getting Help

If you encounter issues:
1. Check the browser console (F12) for JavaScript errors
2. Check the terminal for Python errors
3. Ensure all dependencies are installed: `pip list`
4. Try restarting the app: Ctrl+C then run again

---

**Happy analyzing! 📊**
