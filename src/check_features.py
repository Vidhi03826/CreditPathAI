import pandas as pd

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print(df.head())

print("\nColumns:")
print(df.columns)