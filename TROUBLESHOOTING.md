# Troubleshooting Guide

## Server Not Starting

Make sure the virtual environment is activated:

.\venv\Scripts\activate

Then run:

uvicorn App.main:app --reload

## Dashboard Not Opening

Open:

http://127.0.0.1:8000

## Dataset Validation Error

Run:

python data\validate_dataset.py

Check that the required dataset columns are present.

## Pricing Recommendation Error

Run:

python pricing_recommendation.py

Make sure data\retail_dataset.csv and data\dml_results.csv exist.
