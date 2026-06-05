from flask import (
    Flask,
    request,
    jsonify,
    render_template
)
import pandas as pd
import joblib

# Create Flask App
app = Flask(
    __name__,
    template_folder="../templates"
)

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

    return render_template(
        "index.html"
    )


# Prediction Route
@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    principal = float(
        request.form.get("principal")
    )

    terms = float(
        request.form.get("terms")
    )

    age = float(
        request.form.get("age")
    )

    education = float(
        request.form.get("education")
    )

    gender = float(
        request.form.get("gender")
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


    return f"""

<h1>
Credit Risk Prediction Result
</h1>

<h2>
{result[0]}
</h2>

<a href="/">
Go Back
</a>

"""


if __name__ == "__main__":

    app.run(debug=True)