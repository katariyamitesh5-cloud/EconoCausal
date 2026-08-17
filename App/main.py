from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd

from App.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

# Load pricing recommendations
recommendations = pd.read_csv(
    "data/pricing_recommendations.csv"
)


@app.get("/")
def home():
    return FileResponse("App/index.html")


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