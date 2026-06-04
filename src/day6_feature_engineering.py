import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_loan_data.csv"
)

print("Dataset Loaded Successfully")

print(df.head())

df = df.drop(
    columns=["Loan_ID"]
)

print(df.columns)

def age_group(age):

    if age < 25:
        return "Young"

    elif age < 40:
        return "Adult"

    else:
        return "Senior"


df["age_group"] = df["age"].apply(
    age_group
)

print(
    df[["age","age_group"]].head()
)

def loan_term_category(term):

    if term <= 15:
        return "Short"

    else:
        return "Long"


df["loan_term_category"] = df["terms"].apply(
    loan_term_category
)

print(
    df[
        ["terms",
         "loan_term_category"]
    ].head()
)

df["effective_date"] = pd.to_datetime(
    df["effective_date"]
)

df["loan_month"] = (
    df["effective_date"]
      .dt.month
)

print(
    df[
        ["effective_date",
         "loan_month"]
    ].head()
)

education_mapping = {

    "High School or Below":0,
    "college":1,
    "Bachelor":2,
    "Master or Above":3
}

df["education_encoded"] = (
    df["education"]
      .map(education_mapping)
)

print(
    df[
        ["education",
         "education_encoded"]
    ].head()
)

gender_mapping = {

    "male":1,
    "female":0,
    "Male":1,
    "Female":0
}

df["gender_encoded"] = (
    df["Gender"]
      .map(gender_mapping)
)

print(
    df[
        ["Gender",
         "gender_encoded"]
    ].head()
)

df.to_csv(
    "data/features/feature_engineered_data.csv",
    index=False
)

print(
    "\nFeature engineered dataset saved successfully!"
)