import pandas as pd
from dowhy import CausalModel

# Load dataset
df = pd.read_csv("data/preprocessed.csv")

print("Dataset loaded")
print("Shape:", df.shape)

# Define causal variables
treatment = "discount"
outcome = "sales"

# Confounding variables
confounders = [
    "age",
    "gender",
    "income",
    "previous_purchases"
]

print("Treatment:", treatment)
print("Outcome:", outcome)
print("Confounders:", confounders)

# Create DoWhy causal model
model = CausalModel(
    data=df,
    treatment=treatment,
    outcome=outcome,
    common_causes=confounders
)

print("\nDoWhy model created successfully!")

# Identify causal effect
identified_effect = model.identify_effect(
    proceed_when_unidentifiable=True
)

print("\nIdentified causal effect:")
print(identified_effect)

# Save causal information
with open("causal_variables.txt", "w") as file:
    file.write("EconoCausal Causal Model\n")
    file.write("========================\n")
    file.write(f"Treatment: {treatment}\n")
    file.write(f"Outcome: {outcome}\n")

    file.write("\nConfounders:\n")

    for variable in confounders:
        file.write(f"- {variable}\n")

print("\nCausal graph implementation completed!")