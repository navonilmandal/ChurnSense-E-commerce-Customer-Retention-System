import pandas as pd

def create_features(df):

    # 🔥 FIX: Convert to datetime
    df["last_purchase"] = pd.to_datetime(df["last_purchase"])
    df["first_purchase"] = pd.to_datetime(df["first_purchase"])

    df["customer_lifetime_days"] = (df["last_purchase"] - df["first_purchase"]).dt.days

    df["orders_per_month"] = df["total_orders"] / (df["customer_lifetime_days"] / 30 + 1)

    df["avg_spent_per_order"] = df["total_spent"] / df["total_orders"]

    df["items_per_day"] = df["total_items"] / (df["customer_lifetime_days"] + 1)

    df["value_density"] = df["total_spent"] / (df["total_items"] + 1)

    return df