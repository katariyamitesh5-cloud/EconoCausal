import numpy as np
import pandas as pd


def generate_retail_dataset(
    n_samples=1000,
    random_state=42
):
    np.random.seed(random_state)

    customer_id = np.arange(
        10001, 10001 + n_samples
    )

    age = np.random.randint(
        18, 65, n_samples
    )

    gender = np.random.choice(
        ["Male", "Female"],
        size=n_samples
    )

    income = np.random.normal(
        50000, 15000, n_samples
    ).clip(15000, 120000).round(2)

    previous_purchases = np.random.poisson(
        5, n_samples
    ).clip(0, 20)

    discount = np.random.choice(
        [0, 5, 10, 15, 20, 25, 30],
        size=n_samples
    )

    base_sales = (
        50
        + income * 0.0005
        + previous_purchases * 8
    )

    discount_effect = discount * 2.5

    noise = np.random.normal(
        0, 10, n_samples
    )

    sales = (
        base_sales
        + discount_effect
        + noise
    ).clip(10).round(2)

    data = pd.DataFrame({
        "customer_id": customer_id,
        "age": age,
        "gender": gender,
        "income": income,
        "previous_purchases":
            previous_purchases,
        "discount": discount,
        "sales": sales
    })

    return data


if __name__ == "__main__":

    df = generate_retail_dataset()

    df.to_csv(
        "data/retail_dataset.csv",
        index=False
    )

    print("Dataset generated successfully!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Saved: data/retail_dataset.csv")
    print(df.head())