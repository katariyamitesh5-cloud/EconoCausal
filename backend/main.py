from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="EconoCausal API",
    description="Dynamic Pricing via Double Machine Learning",
    version="1.0.0"
)

# Load pricing recommendations
recommendations = pd.read_csv(
    "data/pricing_recommendations.csv"
)


@app.get("/")
def home():
    return {
        "message": "EconoCausal API is running!",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/recommendation/{customer_id}")
def get_recommendation(customer_id: int):

    customer = recommendations[
        recommendations["customer_id"] == customer_id
    ]

    if customer.empty:
        return {
            "status": "error",
            "message": "Customer not found"
        }

    row = customer.iloc[0]

    return {
        "customer_id": int(row["customer_id"]),
        "current_discount": float(row["discount"]),
        "treatment_effect": float(row["treatment_effect"]),
        "recommendation": row["recommendation"]
    }