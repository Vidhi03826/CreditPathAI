import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print("Dataset Loaded Successfully")

features = [
    "Principal",
    "terms",
    "age",
    # "loan_month",
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
from sklearn.tree import DecisionTreeClassifier

tree_model = DecisionTreeClassifier(

    max_depth=5,

    random_state=42
)

tree_model.fit(
    X_train,
    y_train
)

print("Decision Tree Trained!")
predictions = tree_model.predict(
    X_test
)

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
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

importance = tree_model.feature_importances_

for feature, score in zip(features, importance):

    print(
        feature,
        "=>",
        round(score,4)
    )