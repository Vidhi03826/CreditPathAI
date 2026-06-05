import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

features = [

    "Principal",
    "terms",
    "age",
    "education_encoded",
    "gender_encoded"
]

X = df[features]

y = df["loan_status"]

encoder = LabelEncoder()

y = encoder.fit_transform(y)

model = DecisionTreeClassifier(

    max_depth=3,

    min_samples_split=5,

    random_state=42
)

model.fit(
    X,
    y
)

print(
    "Model Trained Successfully!"
)

import joblib
joblib.dump(

    model,

    "models/credit_risk_model.pkl"
)

print(
    "Model Saved Successfully!"
)

joblib.dump(

    encoder,

    "models/label_encoder.pkl"
)

