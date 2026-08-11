import pandas as pd

# Load preprocessed dataset
df = pd.read_csv("data/preprocessed.csv")

print("Dataset loaded successfully")
print("Dataset shape:", df.shape)

# Display all columns
print("\nAvailable columns:")
for column in df.columns:
    print("-", column)

# Identify possible treatment columns
treatment_keywords = [
    "treatment",
    "treat",
    "policy",
    "intervention",
    "exposure"
]

treatment_columns = []

for column in df.columns:
    name = column.lower()

    for keyword in treatment_keywords:
        if keyword in name:
            treatment_columns.append(column)
            break

# Display treatment candidates
print("\nPossible treatment variables:")

if treatment_columns:
    for column in treatment_columns:
        print("-", column)
else:
    print("No treatment column found.")

# Select treatment variable
if treatment_columns:
    treatment = treatment_columns[0]
else:
    treatment = None

print("\nSelected Treatment:", treatment)

# Check treatment data
if treatment:
    print("\nTreatment values:")
    print(df[treatment].value_counts())

# Save treatment information
with open("treatment_info.txt", "w") as file:
    file.write("Treatment Variable Identification\n")
    file.write("--------------------------------\n")
    file.write(f"Selected Treatment: {treatment}\n")
    file.write("\nPossible Treatment Columns:\n")

    for column in treatment_columns:
        file.write(f"- {column}\n")

print("\nTreatment identification completed.")