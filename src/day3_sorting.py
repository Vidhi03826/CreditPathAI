import pandas as pd

df = pd.read_csv("data/raw/loan_data.csv")

print("\n========== SORT BY AGE ==========")

sorted_data = df.sort_values(by="age")

print(sorted_data[["age","Principal"]])