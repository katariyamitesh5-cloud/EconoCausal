import pandas as pd


REQUIRED_COLUMNS = [
    "customer_id",
    "age",
    "gender",
    "income",
    "previous_purchases",
    "discount",
    "purchase_status"
]


def validate_dataset(file_path):
    df = pd.read_csv(file_path)

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        print("Missing columns:")
        print(missing_columns)
        return False

    if df["customer_id"].duplicated().any():
        print("Duplicate customer IDs found.")
        return False

    if df.isnull().sum().sum() > 0:
        print("Missing values found.")
        return False

    if not df["purchase_status"].isin([0, 1]).all():
        print("Invalid purchase status values found.")
        return False

    print("Dataset validation successful!")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    return True


if __name__ == "__main__":
    validate_dataset(
        "backend/data/retail_dataset.csv"
    )
