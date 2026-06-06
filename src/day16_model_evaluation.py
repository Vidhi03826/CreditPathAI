import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print("Dataset Loaded Successfully")
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

print(
    encoder.classes_
)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = DecisionTreeClassifier(
    max_depth=3
)

model.fit(
    X_train,
    y_train
)

print("Model Trained!")
predictions = model.predict(
    X_test
)

print("\nAccuracy")

print(
    accuracy_score(
        y_test,
        predictions
    )
)
print("\nPrecision")

print(
   precision_score(
    y_test,
    predictions,
    average="weighted",
    zero_division=0
)
)
print("\nRecall")

print(
     recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
)
)
print("\nF1 Score")

print(
    f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )
)
from sklearn.metrics import (
    roc_curve,
    roc_auc_score
)

import matplotlib.pyplot as plt
probabilities = model.predict_proba(
    X_test
)

print(
    probabilities[:5]
)