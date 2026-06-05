import joblib

model = joblib.load(
    "models/credit_risk_model.pkl"
)

print(
    "Model Loaded Successfully!"
)

import pandas as pd

sample_customer = pd.DataFrame({

    "Principal":[1000],

    "terms":[30],

    "age":[35],

    "education_encoded":[2],

    "gender_encoded":[1]
})

prediction = model.predict(
    sample_customer
)

print(
    prediction
)

encoder = joblib.load(
    "models/label_encoder.pkl"
)

result = encoder.inverse_transform(
    prediction
)

print(
    result
)