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

    # Recommended discount based on recommendation
    if row["recommendation"] == "Low Discount":
        recommended_discount = 10

    elif row["recommendation"] == "Medium Discount":
        recommended_discount = 15

    elif row["recommendation"] == "High Discount":
        recommended_discount = 25

    else:
        recommended_discount = float(row["discount"])

    return {
        "customer_id": int(row["customer_id"]),
        "age": int(row["age"]),
        "gender": str(row["gender"]),
        "income": float(row["income"]),
        "previous_purchases": int(row["previous_purchases"]),
        "current_discount": float(row["discount"]),
        "sales": float(row["sales"]),
        "treatment_effect": float(row["treatment_effect"]),
        "recommendation": str(row["recommendation"]),
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

        "recommendations": {
            str(key): int(value)
            for key, value in recommendation_counts.items()
        }
    }


@app.get("/chart-data")
def get_chart_data():

    # --------------------------------
    # Recommendation Distribution
    # --------------------------------

    recommendation_counts = (
        recommendations["recommendation"]
        .value_counts()
        .to_dict()
    )


    # --------------------------------
    # Treatment Effect Distribution
    # --------------------------------

    treatment_effect = recommendations[
        "treatment_effect"
    ]

    effect_bins = [
        {
            "range": "0.0 - 0.5",
            "count": int(
                (treatment_effect < 0.5).sum()
            )
        },

        {
            "range": "0.5 - 0.6",
            "count": int(
                (
                    (treatment_effect >= 0.5)
                    & (treatment_effect < 0.6)
                ).sum()
            )
        },

        {
            "range": "0.6 - 0.7",
            "count": int(
                (
                    (treatment_effect >= 0.6)
                    & (treatment_effect < 0.7)
                ).sum()
            )
        },

        {
            "range": "0.7 - 0.8",
            "count": int(
                (
                    (treatment_effect >= 0.7)
                    & (treatment_effect < 0.8)
                ).sum()
            )
        },

        {
            "range": "0.8+",
            "count": int(
                (treatment_effect >= 0.8).sum()
            )
        }
    ]


    # --------------------------------
    # Discount vs Sales
    # --------------------------------

    discount_sales = (
        recommendations
        .groupby("discount")["sales"]
        .mean()
        .reset_index()
        .sort_values("discount")
    )


    return {

        "recommendations": {

            "Low Discount": int(
                recommendation_counts.get(
                    "Low Discount", 0
                )
            ),

            "Medium Discount": int(
                recommendation_counts.get(
                    "Medium Discount", 0
                )
            ),

            "High Discount": int(
                recommendation_counts.get(
                    "High Discount", 0
                )
            )
        },


        "treatment_effect": effect_bins,


        "discount_sales": [

            {
                "discount": float(
                    row["discount"]
                ),

                "sales": round(
                    float(row["sales"]), 2
                )
            }

            for _, row in discount_sales.iterrows()
        ]
    }