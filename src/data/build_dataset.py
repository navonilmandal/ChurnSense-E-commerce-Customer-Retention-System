# src/data/build_dataset.py

import pandas as pd
from src.data.merge_data import merge_datasets


def build_customer_dataset():
    df = merge_datasets()

    # Convert date column
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

    # Calculate total price per row
    df["total_price"] = df["price"] + df["freight_value"]

    # --- AGGREGATION ---
    customer_df = df.groupby("customer_unique_id").agg(
        total_orders=("order_id", "nunique"),
        total_items=("order_item_id", "count"),
        total_spent=("total_price", "sum"),
        avg_order_value=("total_price", "mean"),
        last_purchase=("order_purchase_timestamp", "max"),
        first_purchase=("order_purchase_timestamp", "min"),
    ).reset_index()

    # --- RECENCY ---
    latest_date = customer_df["last_purchase"].max()
    customer_df["recency_days"] = (latest_date - customer_df["last_purchase"]).dt.days

    # --- CHURN LABEL ---
    # If no purchase in last 90 days → churn
    customer_df["churn"] = customer_df["recency_days"].apply(lambda x: 1 if x > 90 else 0)

    return customer_df


def preview(df):
    print("\nCUSTOMER DATASET")
    print("-" * 50)
    print(df.head())
    print("\nShape:", df.shape)
    print("\nChurn Distribution:\n", df["churn"].value_counts())


if __name__ == "__main__":
    customer_df = build_customer_dataset()
    preview(customer_df)