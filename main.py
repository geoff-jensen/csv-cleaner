import pandas as pd
import numpy as np

# Load the CSV
df = pd.read_csv("sample.csv")

# Print the raw data
print("Raw Data:")
print(df)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# turn whitespace into NaN
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

# Print data after removing whitespace
print('data after removing whitespace:')
print(df)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Drop completely empty rows
df.dropna(how='all', inplace=True)

# Drop rows where all values *except Name* are missing (optional)
df.dropna(subset=['Age', 'Email'], how='all', inplace=True)

# Fill missing values (optional demo)
df.fillna("MISSING", inplace=True)

# Save cleaned data
df.to_csv("cleaned_sample.csv", index=False)

print("\n Cleaned CSV saved as 'cleaned_sample.csv'")
print('Here is the cleaned data:')
print(df)
