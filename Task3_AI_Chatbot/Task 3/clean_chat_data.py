import pandas as pd

# Load raw file
raw_file = "customer_chat_data.csv"
output_file = "chat_data_clean.csv"

try:
    df = pd.read_csv(raw_file, on_bad_lines='skip')
except Exception as e:
    print("Error reading file:", e)
    exit()

# Ensure only rows with proper Q&A are picked (exact match of Question + Answer format)
# We'll look for rows where columns 'Question' and 'Answer' exist
if 'Question' in df.columns and 'Answer' in df.columns:
    cleaned_data = df[['Question', 'Answer']].dropna()
else:
    # Try reading it as no-header fallback
    df = pd.read_csv(raw_file, header=None, on_bad_lines='skip')
    cleaned_data = df[[0, 1]].dropna()
    cleaned_data.columns = ['Question', 'Answer']

cleaned_data.drop_duplicates(subset='Question', inplace=True)
cleaned_data.to_csv(output_file, index=False)
print(f"✅ Cleaned data saved to: {output_file}")
