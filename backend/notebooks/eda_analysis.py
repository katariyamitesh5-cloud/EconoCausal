import pandas as pd


DATA_PATH = "backend/data/retail_dataset.csv"


def load_dataset():
    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully.")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df


if __name__ == "__main__":
    df = load_dataset()

    print("\nDataset Information:")
    print(df.info())

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nStatistical Summary:")
    print(df.describe())