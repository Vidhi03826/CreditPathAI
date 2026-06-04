import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load dataset
df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print("Dataset Loaded Successfully")

# Features
features = [
    "Principal",
    "terms",
    "age",
    "loan_month",
    "education_encoded",
    "gender_encoded"
]

X = df[features]

# Target
y = df["loan_status"]

# Encode target
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Train Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# Model
model = LogisticRegression(
    max_iter=3000,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("\nModel Training Completed!")

# Prediction
predictions = model.predict(X_test)

# Accuracy
print("\nAccuracy")
print(
    accuracy_score(
        y_test,
        predictions
    )
)

# Confusion Matrix
print("\nConfusion Matrix")
print(
    confusion_matrix(
        y_test,
        predictions
    )
)

# Classification Report
print("\nClassification Report")
print(
    classification_report(
        y_test,
        predictions
    )
)