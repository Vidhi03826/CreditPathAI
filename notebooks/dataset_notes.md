# Dataset Summary

## Total Records
500

## Total Features
11

## Target Variable
loan_status

## Important Features
- Principal
- terms
- age
- education
- Gender
- past_due_days

## Missing Values Found

paid_off_time:
100 missing values

past_due_days:
300 missing values

## Observations

- Dataset contains borrower and loan details.
- Missing values exist.
- Loan_ID is an identifier and likely not useful for prediction.
- Data preprocessing will be needed.

## Day 3 Observations

Average age ≈ 31

Education values:
- High School or Below
- Bechalor
- college
- Master or Above

Issues found:
- "Bechalor" spelling inconsistency
- Missing values in past_due_days
- Moderate class imbalance

Target distribution:
- PAIDOFF = 300
- COLLECTION = 100
- COLLECTION_PAIDOFF = 100

## Day 4 Cleaning Summary

### Missing Values Found

paid_off_time : 100 missing

past_due_days : 300 missing

### Cleaning Performed

- Fixed "Bechalor" → "Bachelor"
- Converted effective_date to datetime
- Converted due_date to datetime
- Filled missing values in past_due_days using mean imputation

### Remaining Issues

- paid_off_time still contains 100 missing values
- Requires business analysis before handling

### Output Dataset

data/processed/cleaned_loan_data.csv

## Day 5 EDA Findings

Target Distribution:
- PAIDOFF = 300
- COLLECTION = 100
- COLLECTION_PAIDOFF = 100

Age:
- Mean = 31.11
- Median = 30
- Range = 18–51

Education:
- college = 220
- High School or Below = 209
- Bachelor = 67
- Master or Above = 4

Correlation:
- Principal ↔ terms = 0.534 (strongest observed relationship)

Observations:
- Most borrowers are young professionals.
- Majority successfully repay loans.
- No obvious age outliers detected.
## Day 6 Feature Engineering

New Features Created:

- age_group
- loan_term_category
- loan_month
- education_encoded
- gender_encoded

Removed Features:

- Loan_ID

Observations:

- Categorical variables encoded successfully.
- Feature dataset saved.
- Prepared for machine learning model training.

## Day 7 ML Preparation

Target Variable:
- loan_status

Training Data:
- 400 records

Testing Data:
- 100 records

Selected Features:
- Principal
- terms
- effective_date
- due_date
- past_due_days
- age
- age_group
- loan_term_category
- loan_month
- education_encoded
- gender_encoded

Concepts Learned:
- Feature Selection
- Train-Test Split
- Data Leakage
- Bias vs Variance
- Cross Validation

## Day 8 Model Training

Algorithm:
- Logistic Regression

Experiments:
1. Baseline Logistic Regression
2. Scaled + Balanced Logistic Regression

Key Learnings:
- Accuracy alone is misleading.
- Class imbalance affects model behavior.
- Feature scaling improves optimization.
- Confusion Matrix provides deeper insight than accuracy.

## Day 9 Tree-Based Models

Algorithms:
- Decision Tree
- Random Forest

Feature Importance:
- age = 0.4385
- terms = 0.2839
- Principal = 0.1284

Observations:
- Age was the strongest predictor.
- loan_month had zero importance.
- Random Forest did not outperform Decision Tree on current features.

## Day 10 Model Optimization

Cross Validation Scores:
[0.36, 0.41, 0.42, 0.46, 0.36]

Average:
40.2%

Best Hyperparameters:
- max_depth = 3
- min_samples_split = 5

Best Score:
58.8%

Key Insight:
Reducing model complexity improved generalization.

## Day 11 Production ML Basics

Best Model:
- Tuned Decision Tree

Saved Files:
- credit_risk_model.pkl
- label_encoder.pkl

Concepts Learned:
- Serialization
- Joblib
- Model Loading
- Inference Pipeline

## Day 11 Production Preparation

Model Saved:
- credit_risk_model.pkl

Encoder Saved:
- label_encoder.pkl

Prediction Pipeline:
Input Data
→ Model
→ Encoded Prediction
→ Label Decoder
→ Final Result

Output Example:
PAIDOFF

========================================
DAY 12 - FLASK API & MODEL SERVING
========================================

Objective:
Convert the trained Machine Learning model into a usable web service.

Concepts Learned:
- Flask Framework
- REST API
- Routes
- Endpoints
- HTTP Requests
- JSON Responses
- Model Serving
- Inference Pipeline

Files Created:
1. src/day12_flask_api.py

Models Used:
1. credit_risk_model.pkl
2. label_encoder.pkl

Flask Routes:

1. Home Route
URL:
/

Purpose:
Check whether API is running.

Response:
CreditPathAI API Running

----------------------------------------

2. Prediction Route

URL:
/predict

Parameters:
- principal
- terms
- age
- education
- gender

Example:
Run the file
http://127.0.0.1:5000/

http://127.0.0.1:5000/predict?principal=1000&terms=30&age=35&education=2&gender=1

Output:

{
  "prediction":"PAIDOFF"
}

----------------------------------------

Prediction Pipeline:

User Input
      ↓
Flask API
      ↓
Request Processing
      ↓
DataFrame Creation
      ↓
Decision Tree Model
      ↓
Encoded Prediction
      ↓
Label Decoder
      ↓
JSON Response

----------------------------------------

Production Concepts Learned:

1. Model Serving
Exposing a trained model through an API.

2. Inference
Using a trained model to predict new data.

3. Serialization
Saving models for future use.

4. Latency
Time taken to generate a prediction.

5. Scalability
Ability to handle many users.

----------------------------------------

Key Learnings:

- Flask can expose ML models as APIs.
- APIs allow communication between applications.
- JSON is the standard response format.
- Saved models can be loaded without retraining.
- Real-world ML systems use model serving pipelines.

----------------------------------------

Interview Questions Covered:

1. What is Flask?
2. What is REST API?
3. What is JSON?
4. What is an Endpoint?
5. Difference between GET and POST?
6. What is Model Serving?
7. What is Inference?
8. What is Latency?
9. Why load the model only once?
10. How do ML models work in production?

----------------------------------------



DAY 12 COMPLETED SUCCESSFULLY

Objective:
Create a user-friendly web interface for the CreditPathAI prediction system.

Concepts Learned:

* HTML
* CSS
* Flask Templates
* Jinja2
* Form Handling
* POST Requests
* Frontend & Backend Integration

Files Created:

1. templates/index.html
2. src/day13_web_app.py

Frontend Components:

* Principal Input
* Terms Input
* Age Input
* Education Dropdown
* Gender Dropdown
* Predict Button

Backend Components:

* Flask Server
* Model Loading
* Encoder Loading
* Prediction Logic
* Result Rendering

Application Flow:

User Opens Website
↓
HTML Form Displayed
↓
User Enters Details
↓
POST Request Sent
↓
Flask Receives Data
↓
DataFrame Created
↓
Decision Tree Predicts
↓
Label Decoder Converts Output
↓
Result Page Displayed

Key Learnings:

* HTML creates page structure.
* CSS improves appearance.
* Flask connects frontend and backend.
* POST requests send form data.
* render_template() loads HTML pages.
* Web applications are easier for users than raw APIs.

Interview Questions Covered:

1. What is HTML?
2. What is CSS?
3. What is Flask Template Rendering?
4. What is Jinja2?
5. Difference between GET and POST?
6. What is a Web Application?
7. What is Frontend?
8. What is Backend?
9. What is Full Stack Development?
10. How does Flask connect UI with ML models?

Day 13 Status:

HTML Form             ✅
CSS Styling           ✅
Flask Templates       ✅
POST Requests         ✅
Prediction Page       ✅
Frontend Integration  ✅
Interview Prep        ✅

# DAY 13 COMPLETED SUCCESSFULLY
