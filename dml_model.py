import pandas as pd
from econml.dml import LinearDML
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("data/preprocessed.csv")

print("Dataset loaded:", df.shape)

# Treatment
T = df["discount"].values

# Outcome
Y = df["sales"].values

# Features / confounders
X = df[
    ["age", "income", "previous_purchases", "gender_Male"]
].values

# Split data
X_train, X_test, T_train, T_test, Y_train, Y_test = train_test_split(
    X, T, Y, test_size=0.2, random_state=42
)

# DML model
model = LinearDML(
    model_y=RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),
    model_t=RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),
    random_state=42
)

# Train
model.fit(Y_train, T_train, X=X_train)

# Estimate treatment effect
effect = model.effect(X_test)

print("\nDML Model trained successfully!")
print("Average Treatment Effect:", effect.mean())
print("Minimum Effect:", effect.min())
print("Maximum Effect:", effect.max())

# Save results
results = pd.DataFrame({
    "treatment_effect": effect
})

results.to_csv("data/dml_results.csv", index=False)

print("\nResults saved to data/dml_results.csv")