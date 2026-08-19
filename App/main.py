from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd

from App.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

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

    current_discount = float(row["discount"])
    treatment_effect = float(row["treatment_effect"])
    recommendation = str(row["recommendation"])

    if recommendation == "Low Discount":
        recommended_discount = 10
    elif recommendation == "Medium Discount":
        recommended_discount = 15
    elif recommendation == "High Discount":
        recommended_discount = 25
    else:
        recommended_discount = current_discount

    return {
        "customer_id": int(row["customer_id"]),
        "current_discount": current_discount,
        "treatment_effect": treatment_effect,
        "recommendation": recommendation,
        "recommended_discount": recommended_discount
    }


@app.get("/analytics")
def get_analytics():

    total_customers = len(recommendations)

    average_treatment_effect = recommendations[
        "treatment_effect"
    ].mean()

    average_discount = recommendations[
        "discount"
    ].mean()

    recommendation_counts = (
        recommendations["recommendation"]
        .value_counts()
        .to_dict()
    )

    return {
        "total_customers": int(total_customers),
        "average_treatment_effect": round(
            float(average_treatment_effect), 4
        ),
        "average_discount": round(
            float(average_discount), 2
        ),
        "recommendations": recommendation_counts
    }
