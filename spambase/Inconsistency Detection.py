import pandas as pd

# Load the dataset
file_path = "D:\college\Graduation Project\spambase/spambase_raw.xlsx"
df = pd.read_excel(file_path)

# 1. Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values[missing_values > 0])

# 2. Check data types
data_types = df.dtypes
print("\nData Types:\n", data_types)

# 3. Check for duplicate rows
duplicate_rows = df.duplicated().sum()
print("\nNumber of Duplicate Rows:", duplicate_rows)

# 4. Detect outliers (using Z-score method for numerical columns)
from scipy import stats
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
z_scores = stats.zscore(df[numeric_cols])
outliers = (abs(z_scores) > 3).sum(axis=0)
print("\nOutliers detected in each numerical column:\n", outliers)

# 5. Range checks for numerical columns
for col in numeric_cols:
    if df[col].min() < 0:  # Adjust the condition based on expected range
        print(f"\nColumn '{col}' contains negative values.")
