import numpy as np
import pandas as pd


def generate_retail_dataset(n_samples=1000, random_state=42):
    np.random.seed(random_state)

    customer_id = np.arange(10001, 10001 + n_samples)

    age = np.random.randint(18, 65, n_samples)

    gender = np.random.choice(
        ["Male", "Female"],
        size=n_samples
    )

    income = np.random.normal(
        loc=50000,
        scale=15000,
        size=n_samples
    ).clip(15000, 120000).round(2)

    previous_purchases = np.random.poisson(
        lam=5,
        size=n_samples
    ).clip(0, 20)

    discount = np.random.choice(
        [0, 5, 10, 15, 20, 25, 30],
        size=n_samples
    )

    data = pd.DataFrame({
        "customer_id": customer_id,
        "age": age,
        "gender": gender,
        "income": income,
        "previous_purchases": previous_purchases,
        "discount": discount
    })

    return data


if __name__ == "__main__":
    df = generate_retail_dataset()

    print("Dataset generated successfully!")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(df.head())
