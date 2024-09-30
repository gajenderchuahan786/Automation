import pandas as pd


input_file_path = "path/to/your/input.csv"
output_file_path = "path/to/your/output.csv"


df = pd.read_csv(input_file_path)


print("Initial data preview:\n", df.head())

df.drop_duplicates(inplace=True)


df.dropna(inplace=True)


if 'text_column' in df.columns:
    df['text_column'] = df['text_column'].str.lower().str.strip()

df.to_csv(output_file_path, index=False)

print(f"Data cleaning successfully finished. Cleaned data is stored in: {output_file_path}")
