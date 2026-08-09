import pandas as pd

# Load dataset
df = pd.read_csv("data/dataset.csv")

print("Dataset loaded")
print("Shape:", df.shape)

# Check missing values
print("\nMissing values before:")
print(df.isnull().sum())

# Find numerical and categorical columns
numeric_cols = df.select_dtypes(
    include=["int64", "float64"]
).columns

categorical_cols = df.select_dtypes(
    include=["object"]
).columns

# Fill numerical missing values
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(
            df[col].median()
        )

# Fill categorical missing values
for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

# Check missing values after
print("\nMissing values after:")
print(df.isnull().sum())

# Save processed dataset
df.to_csv(
    "data/preprocessed.csv",
    index=False
)

print("\nMissing values handled successfully
!")

import pandas as pd

# Load dataset
df = pd.read_csv("data/dataset.csv")

print("Dataset loaded")
print("Original shape:", df.shape)

# Handle missing values
numeric_cols = df.select_dtypes(
    include=["int64", "float64"]
).columns

categorical_cols = df.select_dtypes(
    include=["object"]
).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

print("Missing values handled.")

# Check duplicate records
duplicates = df.duplicated().sum()

print("Duplicate records found:", duplicates)

# Remove duplicates
df = df.drop_duplicates()

print("Duplicates after removal:",
      df.duplicated().sum())

print("New shape:", df.shape)

# Save processed dataset
df.to_csv(
    "data/preprocessed.csv",
    index=False
)

print("Duplicate records removed successfully!")