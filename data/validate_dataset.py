import pandas as pd


def validate_dataset(file_path):

    required_columns = [
        "customer_id",
        "age",
        "gender",
        "income",
        "previous_purchases",
        "discount",
        "sales"
    ]

    try:
        df = pd.read_csv(file_path)

        print("Dataset Loaded Successfully")
        print("Rows:", len(df))
        print("Columns:", len(df.columns))

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            print("\nMissing columns:")
            print(missing_columns)
            return False

        print("\nRequired columns: PASS")

        if df.isnull().sum().sum() == 0:
            print("Missing values: PASS")
        else:
            print("Missing values: FAIL")
            print(df.isnull().sum())

        if df["customer_id"].is_unique:
            print("Customer IDs unique: PASS")
        else:
            print("Customer IDs unique: FAIL")

        if (df["age"] > 0).all():
            print("Age validation: PASS")
        else:
            print("Age validation: FAIL")

        if (df["income"] >= 0).all():
            print("Income validation: PASS")
        else:
            print("Income validation: FAIL")

        if (df["previous_purchases"] >= 0).all():
            print("Previous purchases validation: PASS")
        else:
            print("Previous purchases validation: FAIL")

        if (df["discount"] >= 0).all():
            print("Discount validation: PASS")
        else:
            print("Discount validation: FAIL")

        if (df["sales"] >= 0).all():
            print("Sales validation: PASS")
        else:
            print("Sales validation: FAIL")

        print("\nDataset validation completed successfully!")

        return True

    except Exception as e:
        print("Validation failed:", e)
        return False


if __name__ == "__main__":

    validate_dataset(
        "data/retail_dataset.csv"
    )