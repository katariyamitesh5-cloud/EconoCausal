import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = "backend/data/retail_dataset.csv"


def load_dataset():
    return pd.read_csv(DATA_PATH)


def plot_age_distribution(df):
    plt.figure(figsize=(8, 5))

    plt.hist(df["age"], bins=15)

    plt.title("Customer Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.savefig("backend/notebooks/age_distribution.png")
    plt.close()


def plot_income_distribution(df):
    plt.figure(figsize=(8, 5))

    plt.hist(df["income"], bins=20)

    plt.title("Customer Income Distribution")
    plt.xlabel("Income")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.savefig("backend/notebooks/income_distribution.png")
    plt.close()


if __name__ == "__main__":
    df = load_dataset()

    plot_age_distribution(df)
    plot_income_distribution(df)

    print("Customer distribution plots created successfully.")