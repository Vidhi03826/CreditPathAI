from flask import (
    Flask,
    request,
    jsonify,
    render_template
)
import pandas as pd
import joblib
import logging
print("FLASK FILE STARTED")

# Create Flask App
app = Flask(
    __name__,
    template_folder="../templates"
)
logging.basicConfig(
    filename="logs/predictions.log",
    level=logging.INFO
)

# Load Model Once
model = joblib.load(
    "models/credit_risk_model_v1.pkl"
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

@app.route("/health")
def health():

    return {
        "status": "healthy",
        "model": "loaded"
    }
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
         
    if age < 18:

        return """
        <h2 style='color:red;'>
        Error: Age must be at least 18.
        </h2>

        <a href='/'>
        Go Back
        </a>
        """

    if principal <= 0:

        return """
        <h2 style='color:red;'>
        Error: Principal must be greater than 0.
        </h2>

        <a href='/'>
        Go Back
        </a>
        """

    if terms <= 0:

        return """
        <h2 style='color:red;'>
        Error: Terms must be greater than 0.
        </h2>

        <a href='/'>
        Go Back
        </a>
        """
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

    try:

        prediction = model.predict(sample)

        result = encoder.inverse_transform(
            prediction
        )

        logging.info(
            f"""
            Principal={principal},
            Terms={terms},
            Age={age},
            Education={education},
            Gender={gender},
            Prediction={result[0]}
            """
        )

        return render_template(
            "result.html",
            prediction=result[0]
        )

    except Exception as e:

        logging.error(
            f"Prediction Error: {str(e)}"
        )

        return f"""

        <h2 style='color:red;'>

        Error:
        {str(e)}

        </h2>

        <a href='/'>
        Go Back
        </a>

        """
    
if __name__ == "__main__":

     app.run(debug=True)
