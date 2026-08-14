import pandas as pd
from dowhy import CausalModel

# Load preprocessed dataset
df = pd.read_csv("data/preprocessed.csv")

print("Dataset loaded:", df.shape)

# Treatment and outcome
treatment = "discount"
outcome = "sales"

# Confounders
confounders = [
    "age",
    "income",
    "previous_purchases",
    "gender_Male"
]

# Create causal model
model = CausalModel(
    data=df,
    treatment=treatment,
    outcome=outcome,
    common_causes=confounders
)

print("DoWhy model created successfully!")

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
    file.write("Treatment: discount\n")
    file.write("Outcome: sales\n")
    file.write("\nConfounders:\n")

    for variable in confounders:
        file.write(f"- {variable}\n")

print("\nCausal graph completed!")
