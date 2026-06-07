import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
)

import seaborn as sns
import matplotlib.pyplot as plt

# ======================================
# LOAD DATASET
# ======================================

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print("Dataset Loaded Successfully")

# ======================================
# FEATURES
# ======================================

features = [
    "Principal",
    "terms",
    "age",
    "loan_month",
    "education_encoded",
    "gender_encoded"
]

X = df[features]

# ======================================
# TARGET
# ======================================

y = df["loan_status"]

encoder = LabelEncoder()

y = encoder.fit_transform(y)

print("\nClasses:")
print(encoder.classes_)

# ======================================
# TRAIN TEST SPLIT
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ======================================
# MODEL TRAINING
# ======================================

model = RandomForestClassifier(
    random_state=42
)

model.fit(
    X_train,
    y_train
)

print("\nModel Trained Successfully!")

# ======================================
# PREDICTIONS
# ======================================

predictions = model.predict(
    X_test
)

# ======================================
# ACCURACY
# ======================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy")
print(accuracy)

# ======================================
# CONFUSION MATRIX
# ======================================

cm = confusion_matrix(
    y_test,
    predictions
)

print("\nConfusion Matrix")
print(cm)

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title(
    "Confusion Matrix Heatmap"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)

plt.savefig(
    "confusion_matrix.png"
)

plt.show()

# ======================================
# FEATURE IMPORTANCE
# ======================================

importance = model.feature_importances_

print("\nFeature Importance")

for feature, score in zip(
    features,
    importance
):
    print(
        feature,
        "=>",
        round(score, 4)
    )

plt.figure(figsize=(8, 5))

plt.bar(
    features,
    importance
)

plt.title(
    "Feature Importance"
)

plt.ylabel(
    "Importance Score"
)

plt.xticks(rotation=45)

plt.savefig(
    "feature_importance.png"
)

plt.show()

# ======================================
# MODEL COMPARISON
# ======================================

models = [
    "Logistic",
    "Decision Tree",
    "Random Forest"
]

scores = [
    0.44,
    0.46,
    accuracy
]

plt.figure(figsize=(6, 4))

plt.bar(
    models,
    scores
)

plt.title(
    "Model Comparison"
)

plt.ylabel(
    "Accuracy"
)

plt.savefig(
    "model_comparison.png"
)

plt.show()

print("\nCharts Saved Successfully!")

print("""
Generated Files:

1. confusion_matrix.png
2. feature_importance.png
3. model_comparison.png
""")