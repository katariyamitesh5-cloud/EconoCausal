# RUN_GUIDE.md

## 1. Activate Environment

.\venv\Scripts\activate

## 2. Validate Dataset

python data\validate_dataset.py

## 3. Run DML Analysis

python analyze_results.py

## 4. Generate Recommendations

python pricing_recommendation.py

## 5. Start Application

uvicorn App.main:app --reload

## 6. Open Dashboard

http://127.0.0.1:8000

## One-Click Option

The project also includes start.bat for starting the application quickly.
