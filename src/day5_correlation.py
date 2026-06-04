import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_loan_data.csv"
)

print(
    df[
        ["Principal",
         "terms",
         "past_due_days",
         "age"]
    ].corr()
)

print("\n========== EDUCATION COUNTS ==========")

print(
    df["education"].value_counts()
)

print("\n========== AGE SUMMARY ==========")

print(df["age"].describe())