import pandas as pd

# Step 1: Load the Excel file into a DataFrame
file_path = "D:\college\Graduation Project\spambase/cleaned_spambase.xlsx"
df = pd.read_excel(file_path)

# Step 2: Save the DataFrame to a .data file without headers and indices
output_file_path = "cleaned_spambase.data"
df.to_csv(output_file_path, header=False, index=False)

print(f"Data has been successfully saved to {output_file_path}")