import pandas as pd


# Load original customer data
customers = pd.read_csv("data/retail_dataset.csv")

# Load DML treatment effects
effects = pd.read_csv("data/dml_results.csv")

print("Customer data loaded:", customers.shape)
print("DML results loaded:", effects.shape)

# Make sure both datasets have the same number of rows
if len(customers) != len(effects):
    raise ValueError(
        f"Customer rows ({len(customers)}) and "
        f"DML effects ({len(effects)}) do not match."
    )

# Add treatment effect to customer data
customers["treatment_effect"] = effects["treatment_effect"]

# Create pricing recommendation
def recommend_discount(effect, current_discount):
    if effect >= 0.80 and current_discount < 20:
        return "High Discount"
    elif effect >= 0.70 and current_discount < 15:
        return "Medium Discount"
    else:
        return "Low Discount"


customers["recommendation"] = customers.apply(
    lambda row: recommend_discount(
        row["treatment_effect"],
        row["discount"]
    ),
    axis=1
)

# Save recommendations
customers.to_csv(
    "data/pricing_recommendations.csv",
    index=False
)

print("\nDynamic pricing recommendations created!")

print("\nRecommendation summary:")
print(customers["recommendation"].value_counts())

print("\nSample recommendations:")
print(
    customers[
        [
            "customer_id",
            "discount",
            "treatment_effect",
            "recommendation"
        ]
    ].head(10)
)

print("\nSaved: data/pricing_recommendations.csv")