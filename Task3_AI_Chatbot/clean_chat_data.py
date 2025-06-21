import pandas as pd

# Load raw data
raw_file = "customer_chat_data.csv"
output_file = "chat_data_clean.csv"

# Try reading raw data ignoring bad lines
try:
    df = pd.read_csv(raw_file, on_bad_lines='skip', header=None)
except Exception as e:
    print("Error reading the file:", e)
    exit()

# Filter rows that have valid Question and Answer (Column 0 and 1)
cleaned_data = df[[0, 1]].dropna()
cleaned_data.columns = ['Question', 'Answer']

# Optional: remove duplicates
cleaned_data.drop_duplicates(subset='Question', inplace=True)

# Save cleaned data
cleaned_data.to_csv(output_file, index=False)

print(f"✅ Cleaned chat data saved as: {output_file}")
