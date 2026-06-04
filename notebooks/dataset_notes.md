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