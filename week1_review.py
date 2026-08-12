import os
import pandas as pd

print("WEEK 1 DATA REVIEW")
print("=" * 30)

dataset_path = "data/preprocessed.csv"

# Check dataset
if os.path.exists(dataset_path):

    print("[OK] Preprocessed dataset found")

    df = pd.read_csv(dataset_path)

    print("\nDataset Information")
    print("-" * 20)

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # Missing values
    missing = df.isnull().sum().sum()

    print("Missing values:", missing)

    # Duplicate records
    duplicates = df.duplicated().sum()

    print("Duplicate records:", duplicates)

    # Data types
    print("\nData Types:")
    print(df.dtypes)

    # Basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    if missing == 0:
        print("\n[OK] No missing values")

    if duplicates == 0:
        print("[OK] No duplicate records")

else:

    print("[MISSING] Preprocessed dataset")
    print("Expected:", dataset_path)

print("\nDataset review completed.")