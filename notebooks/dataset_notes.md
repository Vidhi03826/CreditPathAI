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