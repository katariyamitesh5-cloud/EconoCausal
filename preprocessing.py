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
        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

print("Missing values handled.")

# Remove duplicate records
duplicates = df.duplicated().sum()
print("Duplicates found:", duplicates)

df = df.drop_duplicates()

print("Duplicates removed.")

# Find categorical columns
categorical_cols = df.select_dtypes(
    include=["object"]
).columns

print("Categorical columns:")
print(list(categorical_cols))

# Encode categorical features
df = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

print("Categorical features encoded.")

# Save processed dataset
df.to_csv(
    "data/preprocessed.csv",
    index=False
)

print("New shape:", df.shape)
print("Encoding completed successfully!")