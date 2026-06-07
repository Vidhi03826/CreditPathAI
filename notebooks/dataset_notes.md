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

Objective:
Transform the basic ML web application into a professional, production-style application.

Concepts Learned:

Bootstrap
Jinja2 Templates
Conditional Rendering
Input Validation
Exception Handling
Bootstrap Components
Professional UI Design
Separation of Concerns

Files Updated:

templates/index.html
templates/result.html
src/day13_web_app.py

Features Added:

Bootstrap Styling
Modern UI
Responsive Design
Better Forms
Styled Buttons
Separate Result Page
result.html created
Dynamic prediction display
Conditional Rendering
Green color for PAIDOFF
Red color for COLLECTION
Red color for COLLECTION_PAIDOFF
Input Validation
Age >= 18
Principal > 0
Terms > 0
Exception Handling
try-except blocks
Graceful error messages
Improved reliability
Professional Result Card
Bootstrap Card Component
Center Alignment
Styled Result Display

Application Flow:

User Input
↓
Validation
↓
Flask Backend
↓
Model Prediction
↓
Result Rendering
↓
Professional Result Page

Production Concepts Learned:

Input Validation
Exception Handling
Server-Side Rendering
UI/UX Improvements
Defensive Programming
Separation of Concerns

Interview Questions Covered:

What is Bootstrap?
What is Jinja2?
What is Conditional Rendering?
What is Input Validation?
Why validate user input?
What is Exception Handling?
What is Defensive Programming?
What is Server-Side Rendering?
Why separate frontend and backend?
Why use templates?

Day 14 Status:

Bootstrap UI ✅
Jinja2 Templates ✅
Conditional Rendering ✅
Input Validation ✅
Exception Handling ✅
Result Card ✅
Interview Prep ✅

# DAY 14 COMPLETED SUCCESSFULLY

======================================== DAY 15 - MODEL PERFORMANCE DASHBOARD

Objective:
Evaluate model performance using visualizations, feature importance analysis, and business insights.

Concepts Learned:

Model Evaluation
Accuracy Comparison
Feature Importance
Confusion Matrix
Heatmap Visualization
Business Insights
Explainable AI Basics
Dashboard Thinking

Files Created:

src/day15_dashboard.py

Visualizations Created:

Accuracy Comparison Chart
Feature Importance Chart
Confusion Matrix Heatmap

Models Compared:

Logistic Regression
Decision Tree

Results:

Logistic Regression Accuracy:
0.44

Decision Tree Accuracy:
0.46

Observation:
Decision Tree performs slightly better than Logistic Regression.

Feature Importance Findings:

Most Important:

Terms
Age
Principal

Least Important:

Loan Month
Education
Gender

Business Insights:

Loan duration strongly affects repayment behavior.
Age influences repayment patterns.
Principal amount contributes moderately.
Education has limited impact in this dataset.

Confusion Matrix Findings:

Observation:
Model predicts majority class frequently.

Reason:
Class imbalance exists in the dataset.

Important Lesson:

High Accuracy
≠
Good Model

A confusion matrix provides deeper understanding than accuracy alone.

Interview Topics Covered:

Feature Importance
Confusion Matrix
Explainable AI
Model Evaluation
Business Insights
Accuracy vs Interpretability
Class Imbalance
Data Visualization

Industry Concepts Learned:

Dashboard Design
Explainability
Model Monitoring
Stakeholder Reporting
Business Communication

Day 15 Status:

Accuracy Chart ✅
Feature Importance ✅
Feature Importance Plot ✅
Confusion Matrix ✅
Heatmap ✅
Business Insights ✅
Interview Prep ✅

# DAY 15 COMPLETED SUCCESSFULLY

======================================== # DAY 16 ADVANCED MODEL EVALUATION

Objective:
Learn industry-standard model evaluation techniques beyond accuracy.

Concepts Covered:

Accuracy
Precision
Recall
F1 Score
Probability Predictions
Class Imbalance
ROC Curve
AUC
Cross Validation
Bias-Variance Tradeoff

Results:

Accuracy:
0.52

Precision:
0.2704

Recall:
0.52

F1 Score:
0.3558

Key Findings:

Accuracy alone is insufficient.
Precision is low.
Recall is moderate.
F1 Score indicates weak balance.
Model favors majority class.

Probability Analysis:

COLLECTION 17.9%
COLLECTION_PAIDOFF 16.7%
PAIDOFF 65.3%

Business Insights:

Loan repayment class dominates predictions.
Class imbalance affects model performance.
Better balancing strategies are required.

Advanced Concepts Learned:

ROC Curve
AUC Score
Cross Validation
Overfitting
Underfitting
Bias vs Variance
Model Explainability

Interview Topics Covered:

Accuracy vs Precision
Precision vs Recall
F1 Score
ROC Curve
AUC
Class Imbalance
Overfitting
Underfitting
Cross Validation
Explainable AI
# DAY 16 COMPLETED SUCCESSFULLY

======================================== DAY 17 - MODEL IMPROVEMENT & CLASS IMBALANCE

Objective:
Improve model fairness and learn techniques for handling imbalanced datasets.

Concepts Learned:

Class Imbalance
Class Weighting
Random Forest
Cross Validation
Model Comparison
Model Stability

File Created:

src/day17_balanced_model.py

Techniques Applied:

Random Forest Classifier
class_weight="balanced"
Cross Validation

Results:

Day 16:

Accuracy = 0.52
Precision = 0.27
Recall = 0.52
F1 Score = 0.356

Day 17:

Accuracy = 0.38
Precision = 0.39
Recall = 0.38
F1 Score = 0.384

Observations:

Accuracy decreased.
Precision improved significantly.
F1 score improved.
Model became less biased toward majority class.

Cross Validation:

Scores:

0.34
0.29
0.34
0.29
0.36

Average Score:

0.324

Key Lesson:

Higher Accuracy
≠
Better Model

Balanced models often provide better business value.

Industry Concepts Learned:

Class Weighting
Fair Learning
Cross Validation
Model Stability
Bias Reduction

Interview Questions Covered:

What is Class Imbalance?
What is Class Weighting?
Why can Accuracy decrease after balancing?
What is Random Forest?
What is Cross Validation?
Why compare multiple models?
What is Model Stability?
# DAY 17 COMPLETED SUCCESSFULLY

========================================
DAY 18 - FEATURE SELECTION
========================================

Objective:
Learn how feature selection affects model performance.

Concepts Learned:

1. Correlation Analysis
2. Correlation Heatmaps
3. Feature Selection
4. Feature Importance
5. Feature Interaction
6. Curse of Dimensionality

Results:

All Features Accuracy:
0.44

Selected Features Accuracy:
0.40

Feature Importance:

Age:
0.798

Terms:
0.123

Principal:
0.079

Key Findings:

- Age is the most important feature.
- Removing features reduced accuracy.
- Weak features may still contribute through interaction.
- Feature selection should be validated experimentally.

Correlation Findings:

Principal ↔ Terms:
0.53

Moderate positive relationship.

Interview Topics Covered:

- Feature Selection
- Correlation
- Feature Importance
- Feature Interaction
- Curse of Dimensionality

# DAY 18 COMPLETED SUCCESSFULLY
========================================
======================================== DAY 21 - ADVANCED MODEL EVALUATION

Objective:
Perform advanced evaluation and visualization of machine learning models.

Concepts Learned:

Confusion Matrix
Confusion Matrix Heatmap
Feature Importance
Model Comparison
ROC Curve Theory
AUC Score Theory
Precision-Recall Tradeoff

Results:

Accuracy:
0.44

Feature Importance:

Age:
0.6628

Education:
0.1321

Terms:
0.1004

Principal:
0.0615

Gender:
0.0433

Loan Month:
0.0000

Key Findings:

Age is the strongest predictor.
Loan Month contributes no predictive value.
The model is biased toward the PAIDOFF class.
Class imbalance affects performance.
Data quality is the main limitation.

Interview Topics Covered:

ROC
AUC
Precision
Recall
F1 Score
Confusion Matrix
Feature Importance
# DAY 21 COMPLETED SUCCESSFULLY

http://127.0.0.1:5000/health -- Halth prediction
========================================
DAY 22 - PRODUCTION READINESS
========================================

Concepts Learned:

1. Prediction Logging
2. Health Endpoint
3. Model Versioning
4. Error Handling
5. Production Folder Structure

Features Implemented:

- logs/predictions.log
- /health endpoint
- credit_risk_model_v1.pkl
- Error Logging
- Organized Project Structure

Key Learnings:

- Production systems require monitoring.
- Logs are essential for debugging.
- Models should be versioned.
- Applications should fail gracefully.
- Folder structure improves maintainability.

Interview Topics:

- Logging
- Health Checks
- Monitoring
- Versioning
- Error Handling

# DAY 22 COMPLETED SUCCESSFULLY

========================================
DAY 23 - PORTFOLIO POLISH
========================================

Concepts Learned:

1. Project Documentation
2. GitHub Presentation
3. Resume Integration
4. Architecture Explanation
5. Project Storytelling

Deliverables:

- Professional README
- Screenshots
- Architecture Diagram
- Resume Description
- Interview Preparation

Key Learnings:

- Technical skills are important.
- Presentation is equally important.
- Recruiters spend limited time reviewing projects.
- Clear documentation increases project value.

DAY 23 COMPLETED SUCCESSFULLY
========================================


