import pandas as pd

print("\nLoading dataset...")

df = pd.read_csv("data/raw/loan_data.csv")

print("\nDataset loaded successfully!")

# Shape
print("\n========== SHAPE ==========")
print(df.shape)

# First rows
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

# Last rows
print("\n========== LAST 5 ROWS ==========")
print(df.tail())

# Select one column
print("\n========== AGE COLUMN ==========")
print(df["age"])

# Select multiple columns
print("\n========== AGE + EDUCATION ==========")
print(df[["age","education"]])

# Statistics
print("\n========== NUMERICAL SUMMARY ==========")
print(df.describe())

# Unique values
print("\n========== UNIQUE EDUCATION VALUES ==========")
print(df["education"].unique())

# Count values
print("\n========== LOAN STATUS COUNTS ==========")
print(df["loan_status"].value_counts())