import pandas as pd

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print("Dataset Loaded!")
print(df.head())
import matplotlib.pyplot as plt

models = [
    "Logistic Regression",
    "Decision Tree"
]

scores = [
    0.44,
    0.46
]

plt.bar(
    models,
    scores
)

plt.title(
    "Model Accuracy Comparison"
)

plt.ylabel(
    "Accuracy"
)

plt.show()
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
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

model = DecisionTreeClassifier(
    max_depth=3
)

model.fit(
    X_train,
    y_train
)
importance = model.feature_importances_

print(importance)
plt.figure(figsize=(8,5))

plt.bar(
    features,
    importance
)

plt.title(
    "Feature Importance"
)

plt.xticks(rotation=45)

plt.show()

from sklearn.metrics import (
    confusion_matrix
)

import seaborn as sns
predictions = model.predict(
    X_test
)
cm = confusion_matrix(
    y_test,
    predictions
)

print(cm)
plt.figure(figsize=(6,4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d"
)

plt.title(
    "Confusion Matrix"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)

plt.show()

print("\nBUSINESS INSIGHTS")

print(
    "Age appears to be a strong predictor."
)

print(
    "Loan terms influence repayment outcomes."
)

print(
    "Model can assist in risk assessment."
)
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.bar(
    features,
    importance
)

plt.title(
    "Feature Importance"
)

plt.xlabel(
    "Features"
)

plt.ylabel(
    "Importance"
)

plt.xticks(rotation=45)

plt.show()

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
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
        average="weighted"
    )
)

print("\nRecall")
print(
    recall_score(
        y_test,
        predictions,
        average="weighted"
    )
)

print("\nF1 Score")
print(
    f1_score(
        y_test,
        predictions,
        average="weighted"
    )
)