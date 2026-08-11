import pandas as pd

# Load dataset
df = pd.read_csv("data/preprocessed.csv")

print("Dataset loaded successfully")
print("Dataset shape:", df.shape)

# Display columns
print("\nAvailable columns:")
for column in df.columns:
    print("-", column)

# -------------------------------
# Identify Treatment
# -------------------------------

treatment_keywords = [
    "treatment", "treat", "policy",
    "intervention", "exposure"
]

treatment_columns = []

for column in df.columns:
    name = column.lower()

    for keyword in treatment_keywords:
        if keyword in name:
            treatment_columns.append(column)
            break

if treatment_columns:
    treatment = treatment_columns[0]
else:
    treatment = None

print("\nTreatment:", treatment)

# -------------------------------
# Identify Outcome
# -------------------------------

outcome_keywords = [
    "outcome", "result", "target",
    "effect", "response"
]

outcome_columns = []

for column in df.columns:
    name = column.lower()

    for keyword in outcome_keywords:
        if keyword in name:
            outcome_columns.append(column)
            break

print("\nPossible outcome variables:")

for column in outcome_columns:
    print("-", column)

if outcome_columns:
    outcome = outcome_columns[0]
else:
    outcome = None

print("\nSelected Outcome:", outcome)

# Save information
with open("causal_variables.txt", "w") as file:
    file.write("Causal Variable Identification\n")
    file.write("-----------------------------\n")
    file.write(f"Treatment: {treatment}\n")
    file.write(f"Outcome: {outcome}\n")

print("\nTreatment and outcome identification completed.")