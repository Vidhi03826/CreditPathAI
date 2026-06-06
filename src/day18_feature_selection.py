import pandas as pd

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print("Dataset Loaded!")

print("\nCorrelation Matrix")

print(
    df[
        [
            "Principal",
            "terms",
            "past_due_days",
            "age"
        ]
    ].corr()
)
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))

sns.heatmap(
    df[
        [
            "Principal",
            "terms",
            "past_due_days",
            "age"
        ]
    ].corr(),
    annot=True
)

plt.title(
    "Feature Correlation Heatmap"
)

plt.show()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==========================
# ALL FEATURES MODEL
# ==========================

features_all = [
    "Principal",
    "terms",
    "age",
    "loan_month",
    "education_encoded",
    "gender_encoded"
]

X = df[features_all]

y = df["loan_status"]

encoder = LabelEncoder()

y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model_all = RandomForestClassifier(
    random_state=42
)

model_all.fit(
    X_train,
    y_train
)

predictions_all = model_all.predict(
    X_test
)

accuracy_all = accuracy_score(
    y_test,
    predictions_all
)

# ==========================
# SELECTED FEATURES MODEL
# ==========================

features_selected = [
    "Principal",
    "terms",
    "age"
]

X = df[features_selected]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy_selected = accuracy_score(
    y_test,
    predictions
)

# ==========================
# ACCURACY COMPARISON
# ==========================

print("\nAll Features Accuracy")
print(accuracy_all)

print("\nSelected Features Accuracy")
print(accuracy_selected)

# ==========================
# FEATURE IMPORTANCE
# ==========================

importance = model.feature_importances_

print("\nFeature Importance")

for feature, score in zip(
    features_selected,
    importance
):

    print(
        feature,
        "=>",
        score
    )