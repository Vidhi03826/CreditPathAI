import pandas as pd

df = pd.read_csv("data/raw/loan_data.csv")

print("\n========== AGE > 30 ==========")
print(df[df["age"] > 30])

print("\n========== ONLY COLLEGE STUDENTS ==========")
print(df[df["education"]=="college"])

print("\n========== PAIDOFF LOANS ==========")
print(df[df["loan_status"]=="PAIDOFF"])