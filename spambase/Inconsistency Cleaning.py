import pandas as pd

# Load the dataset
file_path = "D:\college\Graduation Project\spambase/spambase_raw.xlsx"
df = pd.read_excel(file_path)

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()
print(f"Number of rows after removing duplicates: {df_no_duplicates.shape[0]}")

# Save the cleaned DataFrame to a new Excel file
df_no_duplicates.to_excel('cleaned_spambase.xlsx', index=False)