import pandas as pd

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print("Dataset Loaded Successfully")

df = df.drop(
    columns=[
        "paid_off_time",
        "education",
        "Gender"
    ]
)

print(df.columns)

X = df.drop(
    columns=["loan_status"]
)

y = df["loan_status"]

print("\nFeatures Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

print("\nTraining Features:")
print(X_train.shape)

print("\nTesting Features:")
print(X_test.shape)

print("\nTraining Labels:")
print(y_train.shape)

print("\nTesting Labels:")
print(y_test.shape)

X_train.to_csv(
    "data/model_input/X_train.csv",
    index=False
)

X_test.to_csv(
    "data/model_input/X_test.csv",
    index=False
)

y_train.to_csv(
    "data/model_input/y_train.csv",
    index=False
)

y_test.to_csv(
    "data/model_input/y_test.csv",
    index=False
)

print(
    "\nTrain/Test datasets saved successfully!"
)