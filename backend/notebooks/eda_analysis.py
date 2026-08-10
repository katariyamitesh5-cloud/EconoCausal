import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = "backend/data/retail_dataset.csv"


def load_dataset():
    return pd.read_csv(DATA_PATH)


def analyze_discount_behavior(df):
    discount_analysis = (
        df.groupby("discount")["purchase_status"]
        .mean()
        .reset_index()
    )

    discount_analysis["purchase_rate"] *= 100

    print("\nPurchase Rate by Discount:")
    print(discount_analysis)

    plt.figure(figsize=(8, 5))

    plt.plot(
        discount_analysis["discount"],
        discount_analysis["purchase_rate"],
        marker="o"
    )

    plt.title("Purchase Rate by Discount")
    plt.xlabel("Discount (%)")
    plt.ylabel("Purchase Rate (%)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "backend/notebooks/discount_purchase_analysis.png"
    )

    plt.close()


def analyze_purchase_behavior(df):
    purchase_summary = (
        df["purchase_status"]
        .value_counts()
        .sort_index()
    )

    print("\nPurchase Status Summary:")
    print(purchase_summary)

    purchase_rate = df["purchase_status"].mean() * 100

    print(
        f"\nOverall Purchase Rate: "
        f"{purchase_rate:.2f}%"
    )


if __name__ == "__main__":
    df = load_dataset()

    print("Starting EDA...")

    print("\nDataset Shape:")
    print(df.shape)

    print("\nDataset Summary:")
    print(df.describe())

    analyze_discount_behavior(df)
    analyze_purchase_behavior(df)

    print("\nEDA completed successfully.")