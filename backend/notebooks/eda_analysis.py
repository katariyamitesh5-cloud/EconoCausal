import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = "backend/data/retail_dataset.csv"


def load_dataset():
    return pd.read_csv(DATA_PATH)


def create_correlation_matrix(df):
    numeric_columns = [
        "age",
        "income",
        "previous_purchases",
        "discount",
        "purchase_status"
    ]

    correlation = df[numeric_columns].corr()

    print("\nCorrelation Matrix:")
    print(correlation)

    plt.figure(figsize=(8, 6))

    plt.imshow(correlation, interpolation="nearest")

    plt.colorbar()

    plt.xticks(
        range(len(numeric_columns)),
        numeric_columns,
        rotation=45,
        ha="right"
    )

    plt.yticks(
        range(len(numeric_columns)),
        numeric_columns
    )

    plt.title("Feature Correlation Matrix")

    plt.tight_layout()

    plt.savefig(
        "backend/notebooks/correlation_matrix.png"
    )

    plt.close()


if __name__ == "__main__":
    df = load_dataset()

    create_correlation_matrix(df)

    print("Correlation analysis completed successfully.")