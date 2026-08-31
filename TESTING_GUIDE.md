# Testing Guide

## Dataset Validation

Run:

python data\validate_dataset.py

The validation should confirm that the required columns, missing values, customer IDs, age, income, previous purchases, discount, and sales are valid.

## DML Analysis

Run:

python analyze_results.py

This generates the treatment-effect analysis file.

## Pricing Recommendations

Run:

python pricing_recommendation.py

This generates customer-level pricing recommendations.

## Application Testing

Start the application with:

start.bat

Then open:

http://127.0.0.1:8000

## Final Verification

Before deployment, verify:

- Dataset validation passes
- DML analysis completes
- Pricing recommendations are generated
- FastAPI server starts successfully
- Dashboard loads successfully
- Customer recommendation API works
