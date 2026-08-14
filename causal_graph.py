import pandas as pd
from dowhy import CausalModel

df = pd.read_csv("data/preprocessed.csv")

print("Dataset loaded")
print("Shape:", df.shape)

treatment = "discount"
outcome = "sales"

confounders = [
    "age",
    "gender_Male",
    "income",
    "previous_purchases"
]

print("Treatment:", treatment)
print("Outcome:", outcome)
print("Confounders:", confounders)

model = CausalModel(
    data=df,
    treatment=treatment,
    outcome=outcome,
    common_causes=confounders
)

print("\nDoWhy model created successfully!")

identified_effect = model.identify_effect(
    proceed_when_unidentifiable=True
)

print("\nIdentified causal effect:")
print(identified_effect)

with open("causal_variables.txt", "w") as file:
    file.write("EconoCausal Causal Model\n")
    file.write("========================\n")
    file.write(f"Treatment: {treatment}\n")
    file.write(f"Outcome: {outcome}\n")
    file.write("\nConfounders:\n")

    for variable in confounders:
        file.write(f"- {variable}\n")

print("\nCausal graph implementation completed!")