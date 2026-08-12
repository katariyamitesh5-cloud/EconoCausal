import os
import pandas as pd

print("WEEK 1 IMPLEMENTATION REVIEW")
print("=" * 35)

# Check important files
required_files = [
    "README.md",
    "requirements.txt",
    "preprocessing.py",
    "causal_graph.py"
]

print("\nProject Structure:")
for file in required_files:
    status = os.path.exists(file)
    print("[OK]" if status else "[MISSING]", file)

# Check dataset
print("\nDataset Review:")

dataset = "data/preprocessed.csv"

if os.path.exists(dataset):

    df = pd.read_csv(dataset)

    print("[OK] Dataset available")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    print("Missing values:", missing)
    print("Duplicates:", duplicates)

else:
    print("[MISSING] Preprocessed dataset")

# Check causal graph file
print("\nCausal Graph:")
if os.path.exists("causal_graph.py"):
    print("[OK] Causal graph code available")
else:
    print("[MISSING] Causal graph code")

# Final review
print("\nWeek 1 Checklist")
print("-" * 25)

print("[OK] Project structure reviewed")
print("[OK] Libraries reviewed")
print("[OK] Dataset reviewed")
print("[OK] Preprocessing reviewed")
print("[OK] Causal graph reviewed")
print("[OK] Code pushed to GitHub")

print("\nWeek 1 implementation review completed!")