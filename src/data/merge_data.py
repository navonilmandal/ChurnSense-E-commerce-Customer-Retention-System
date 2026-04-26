# src/data/merge_data.py

import pandas as pd
from src.data.load_data import load_datasets


def merge_datasets():
    data = load_datasets()

    customers = data["customers"]
    orders = data["orders"]
    order_items = data["order_items"]
    payments = data["payments"]

    # Merge customers with orders
    df = orders.merge(customers, on="customer_id", how="left")

    # Merge with order items
    df = df.merge(order_items, on="order_id", how="left")

    # Merge with payments
    df = df.merge(payments, on="order_id", how="left")

    return df


def basic_checks(df):
    print("\nMERGED DATA")
    print("-" * 50)
    print(df.head())
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns)


if __name__ == "__main__":
    df = merge_datasets()
    basic_checks(df)