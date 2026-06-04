import pandas as pd

df = pd.read_csv("data/raw/loan_data.csv")

print("Dataset Loaded Successfully")


print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())


print("\n========== MISSING PERCENTAGE ==========")

missing_percent = (df.isnull().sum()/len(df))*100

print(missing_percent)


print("\n========== EDUCATION VALUES ==========")

print(df["education"].unique())
df["education"] = df["education"].replace(
    "Bechalor",
    "Bachelor"
)

print(df["education"].unique())
print(df.dtypes)
df["effective_date"] = pd.to_datetime(
    df["effective_date"],
    format="mixed"
)

df["due_date"] = pd.to_datetime(
    df["due_date"],
    format="mixed"
)
print("\nDATE CONVERSION CHECK")

print(df[["effective_date","due_date"]].head())
print(df.dtypes)

df["past_due_days"] = df["past_due_days"].fillna(
    df["past_due_days"].mean()
)
print(df.isnull().sum())

print("\nPAID OFF TIME MISSING:")
print(df["paid_off_time"].isnull().sum())
print("\n========== FINAL DATASET INFO ==========")
df.info()

df.to_csv(
    "data/processed/cleaned_loan_data.csv",
    index=False
)

print("Cleaned dataset saved successfully!")