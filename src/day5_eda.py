import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/cleaned_loan_data.csv"
)

print("Dataset Loaded Successfully")

print("\n========== LOAN STATUS COUNTS ==========")

print(
    df["loan_status"].value_counts()
)

df["loan_status"].value_counts().plot(
    kind="bar"
)

plt.title("Loan Status Distribution")

plt.xlabel("Loan Status")

plt.ylabel("Count")

plt.show()

print("\n========== AGE SUMMARY ==========")

print(df["age"].describe())

plt.figure()

df["age"].hist()

plt.title("Age Distribution")

plt.xlabel("Age")

plt.ylabel("Frequency")

plt.show()

print("\n========== EDUCATION COUNTS ==========")

print(
    df["education"].value_counts()
)

plt.figure()

df["education"].value_counts().plot(
    kind="bar"
)

plt.title("Education Distribution")

plt.xlabel("Education")

plt.ylabel("Count")

plt.show()
plt.figure()

df.boxplot(column="age")

plt.title("Age Boxplot")

plt.show()