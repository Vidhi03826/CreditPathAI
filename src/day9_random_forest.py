import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

features = [

    "Principal",
    "terms",
    "age",
    "loan_month",
    "education_encoded",
    "gender_encoded"
]

X = df[features]

y = df["loan_status"]

encoder = LabelEncoder()

y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42
)

rf_model = RandomForestClassifier(

    n_estimators=100,

    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)

predictions = rf_model.predict(
    X_test
)

print("\nAccuracy")

print(
    accuracy_score(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)

print("\nClassification Report")

print(
    classification_report(
        y_test,
        predictions
    )
)