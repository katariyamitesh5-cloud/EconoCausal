import pandas as pd
from sklearn.preprocessing import StandardScaler

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

# Remove duplicates
df = df.drop_duplicates()

print("Duplicate records removed.")

# Encode categorical features
categorical_cols = df.select_dtypes(
    include=["object"]
).columns

df = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

print("Categorical features encoded.")

# Normalize numerical features
numeric_cols = df.select_dtypes(
    include=["int64", "float64"]
).columns

scaler = StandardScaler()

df[numeric_cols] = scaler.fit_transform(
    df[numeric_cols]
)

print("Numerical features normalized.")

# Save final dataset
df.to_csv(
    "data/preprocessed.csv",
    index=False
)

print("Final shape:", df.shape)
print("Preprocessing completed successfully!")
