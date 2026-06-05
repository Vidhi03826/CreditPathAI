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