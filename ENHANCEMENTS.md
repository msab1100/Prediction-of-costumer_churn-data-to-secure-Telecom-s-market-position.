# Enhanced main.py - Complete Documentation

## Overview

The updated `main.py` has been enhanced to handle both sample data and external CSV/Excel files with full flexibility.

## Key Improvements

### 1. **Automatic Data Detection**
- Automatically searches for sample data in the current directory
- Supports both `.xlsx` and `.csv` formats
- Falls back to default paths if sample files not found
- Clear error messages if no data is available

### 2. **External Data Support**
- Accept any CSV or Excel file via command-line argument
- Full path support: `python main.py /path/to/file.csv`
- Validates file format before processing

### 3. **Dynamic Feature Selection**
- Automatically identifies numeric features in the dataset
- Scales only numeric columns
- Models adapt to available features
- Works with datasets having any number of features

### 4. **Flexible Analysis**
- Only performs analysis for columns that exist in the dataset
- Gracefully skips missing columns
- Provides clear feedback on what analysis was performed

### 5. **Better Error Handling**
- File not found: Clear error message
- Missing Churn column: Helpful error with column listing
- Unsupported format: Error message with usage instructions
- Insufficient features: Completes with available analysis

## Usage Examples

```bash
# Option 1: Auto-detect sample data
python main.py

# Option 2: Use specific sample file
python main.py sample_churn_dataset.xlsx

# Option 3: Use external CSV
python main.py ~/Documents/customer_data.csv

# Option 4: Use external Excel
python main.py /data/telco_churn.xlsx
```

## Supported Input Formats

### CSV Files
```csv
gender,tenure,MonthlyCharges,Churn
Male,12,50.5,No
Female,24,75.2,Yes
```

### Excel Files (.xlsx, .xls)
- Any structure with column headers
- Multiple sheets: reads first sheet

## Output Files

All outputs are saved to the `outputs/` directory:
- Visualization PNGs (charts, confusion matrices)
- Named descriptively based on what was analyzed

## Code Structure

```
main.py
├── 1. IMPORT LIBRARIES
├── 2. LOAD DATA
│   ├── load_data() function
│   └── Auto-detection logic
├── 3. DATA ANALYSIS (dynamic)
├── 4. VISUALIZATION (dynamic)
├── 5. PREPROCESSING (dynamic features)
├── 6-8. MODEL TRAINING (adaptive)
└── 9. FINAL OUTPUT
```

## Features by Data Type

### Numeric Columns
- Automatically scaled with StandardScaler
- Used as features in models
- Analyzed in preprocessing step

### Categorical Columns
- Displayed in exploratory analysis
- Optional analysis if relevant columns exist
- Target variable 'Churn' encoded for modeling

## Robustness

The script handles:
- ✓ Missing columns gracefully
- ✓ Different file formats
- ✓ Various feature combinations
- ✓ Small datasets (test_data.csv: 10 rows)
- ✓ Large datasets (sample: 1000 rows)
- ✓ Different data distributions
- ✓ Unicode/emoji compatibility (uses ASCII)

## Testing Performed

1. **Sample Data Test** ✓
   - Loads sample_churn_dataset.xlsx
   - Performs all analysis
   - Generates 8 output files

2. **Auto-Detection Test** ✓
   - Runs without arguments
   - Auto-finds sample file
   - Produces expected output

3. **External CSV Test** ✓
   - Loads test_data.csv
   - Handles minimal columns
   - Adapts analysis accordingly

4. **Error Handling Test** ✓
   - Detects missing files
   - Provides helpful error messages
   - Exits gracefully

## Files Included

- `main.py` - Enhanced main script
- `test_data.csv` - Sample CSV for testing
- `README.md` - User documentation
- `ENHANCEMENTS.md` - This file
- `sample_churn_dataset.xlsx` - Sample data (existing)
- `requirements.txt` - Dependencies (existing)

## How to Use Your Own Data

1. Prepare your CSV or Excel file with a 'Churn' column
2. Run: `python main.py your_file.csv`
3. Results appear in `outputs/` directory

Example custom data structure:
```csv
id,customer_age,monthly_spend,customer_tenure,Churn
1,35,100,24,No
2,42,150,12,Yes
3,28,75,6,No
```

## Backward Compatibility

The enhanced script:
- ✓ Works with original sample data
- ✓ Produces same outputs as before
- ✓ Uses same model architectures
- ✓ Maintains analysis methodology
- ✓ Compatible with existing workflows

## Future Enhancements

Possible improvements:
- Save model performance metrics to CSV
- Generate detailed analysis reports
- Support multiple Churn column names
- Interactive data preview
- Model persistence (save/load trained models)
- Parameter configuration file

---

**Summary**: The main.py script is now a flexible, robust tool for analyzing any customer churn dataset with automatic data detection and adaptive analysis.
