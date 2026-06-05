from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Create Flask App
app = Flask(__name__)

# Load Model Once
model = joblib.load(
    "models/credit_risk_model.pkl"
)

encoder = joblib.load(
    "models/label_encoder.pkl"
)

# Home Route
@app.route("/")
def home():

    return "CreditPathAI API Running"


# Prediction Route
@app.route("/predict")
def predict():

    principal = float(
        request.args.get("principal")
    )

    terms = float(
        request.args.get("terms")
    )

    age = float(
        request.args.get("age")
    )

    education = float(
        request.args.get("education")
    )

    gender = float(
        request.args.get("gender")
    )

    sample = pd.DataFrame({

        "Principal": [principal],

        "terms": [terms],

        "age": [age],

        "education_encoded": [education],

        "gender_encoded": [gender]

    })

    prediction = model.predict(sample)

    result = encoder.inverse_transform(
        prediction
    )

    return jsonify({

        "prediction": result[0]
    })


if __name__ == "__main__":

    app.run(debug=True)