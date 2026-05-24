import pandas as pd

print("\nLoading dataset...")

# Read dataset
df = pd.read_csv("data/raw/loan_data.csv")

print("\nDataset loaded successfully!")

print("\n==============================")
print("Dataset Shape")
print("==============================")

print(df.shape)

print("\n==============================")
print("Column Names")
print("==============================")

for col in df.columns:
    print(col)

print("\n==============================")
print("First 5 Rows")
print("==============================")

print(df.head())

print("\n==============================")
print("Dataset Information")
print("==============================")

df.info()