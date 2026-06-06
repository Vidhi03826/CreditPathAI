# CreditPathAI

CreditPathAI is a machine learning-based system designed to predict loan default risk and recommend personalized recovery actions.

## Objective
To automate loan recovery decision-making using data-driven insights.

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI (later)
- React.js (later)

## Current Status
✅ Day 1: Project setup completed
✅ Day 2: Dataset understanding completed
✅ Day 3: Pandas Fundamentals and Exploration completed
✅ Day 4: Data Cleaning and Preprocessing Completed
✅ Day 5: Exploratory Data Analysis (EDA) Completed
✅ Day 6: Feature Engineering Completed
✅ Day 7: Feature Selection and Train-Test Split Completed
✅ Day 8: Logistic Regression Model Built

Results:
- Baseline Accuracy = 52%
- Improved Logistic Regression = 44%
- Learned importance of class imbalance and feature scaling.

✅ Day 9: Decision Tree & Random Forest

Models Built:
- Decision Tree Classifier
- Random Forest Classifier

Concepts Learned:
- Entropy
- Gini Index
- Information Gain
- Feature Importance
- Hyperparameter Tuning

Results:
- Decision Tree Accuracy = 46%
- Random Forest Accuracy = 44%

Key Finding:
Age was the most important feature.
Loan Month contributed almost no predictive value.

✅ Day 10: Cross Validation & Hyperparameter Tuning

Concepts:
- K-Fold Cross Validation
- GridSearchCV
- Hyperparameter Tuning
- Model Selection
- Bias-Variance Tradeoff

Results:
- Average CV Score = 40.2%
- Best Parameters:
  - max_depth = 3
  - min_samples_split = 5
- Best Cross Validation Score = 58.8%

Best Model:
- Tuned Decision Tree

✅ Day 11: Model Persistence & Inference

Concepts:
- Serialization
- Joblib
- Model Persistence
- Inference Pipeline

Artifacts:
- credit_risk_model.pkl
- label_encoder.pkl

Key Learning:
A trained model can be saved, loaded, and reused without retraining.

✅ Day 11: Model Persistence & Inference

Concepts Learned:
- Serialization
- Joblib
- Model Saving
- Model Loading
- Inference Pipeline
- Label Decoding

Artifacts:
- models/credit_risk_model.pkl
- models/label_encoder.pkl

Prediction Example:
Customer → PAIDOFF

✅ Day 12: Flask API Deployment

Concepts:
- Flask
- REST API
- Routes
- Endpoints
- JSON Responses
- Model Serving

Endpoint:
GET /predict

Example:

{
  "prediction":"PAIDOFF"
}

## Day 13 - Web Application Interface

Features Added:

* HTML Frontend
* User Input Form
* Flask Template Rendering
* Prediction Result Page
* Frontend + Backend Integration

Workflow:

User Input
→ Flask Backend
→ ML Model
→ Prediction
→ Result Page

Technologies:

* HTML
* CSS
* Flask
* Scikit-learn
* Joblib

## Day 14 - Professional Web Application

Features Added:

* Bootstrap UI
* Responsive Forms
* Dynamic Result Page
* Input Validation
* Error Handling
* Conditional Rendering

Validation Rules:

* Age >= 18
* Principal > 0
* Terms > 0

Technologies:

* Flask
* Bootstrap
* Jinja2
* Scikit-learn
* Joblib

Highlights:

* Professional UI
* Production Concepts
* Defensive Programming
* Better User Experience

## Day 15 - Model Performance Dashboard

Features Added:

* Accuracy Comparison
* Feature Importance Analysis
* Confusion Matrix Visualization
* Business Insights
* Explainability Dashboard

Visualizations:

1. Logistic Regression vs Decision Tree Accuracy
2. Feature Importance Bar Chart
3. Confusion Matrix Heatmap

Key Findings:

* Decision Tree outperformed Logistic Regression.
* Loan Terms are the strongest predictor.
* Age significantly impacts repayment behavior.
* Dataset shows class imbalance.

Skills Demonstrated:

* Model Evaluation
* Explainable AI
* Data Visualization
* Business Interpretation

## Day 16 - Advanced Model Evaluation

Metrics Implemented:

* Accuracy
* Precision
* Recall
* F1 Score
* Probability Predictions

Concepts Learned:

* ROC Curve
* AUC Score
* Class Imbalance
* Cross Validation
* Bias-Variance Tradeoff

Results:

Accuracy: 52%

Precision: 27%

Recall: 52%

F1 Score: 35.6%

Key Insights:

* Accuracy alone is misleading.
* Model favors majority class.
* F1 Score provides a better evaluation.
* Probability outputs improve explainability.

Skills Demonstrated:

* Advanced Evaluation
* Explainable AI
* Classification Metrics
* Business Interpretation

## Day 17 - Handling Class Imbalance

Features Added:

* Random Forest Classifier
* Class Weighting
* Cross Validation
* Model Comparison

Results:

Accuracy: 38%

Precision: 39%

Recall: 38%

F1 Score: 38%

Key Insights:

* Balanced learning reduced bias.
* Precision improved significantly.
* Cross validation provided reliable evaluation.
* Accuracy alone is insufficient.

Skills Demonstrated:

* Model Improvement
* Class Imbalance Handling
* Cross Validation
* Random Forest Training
