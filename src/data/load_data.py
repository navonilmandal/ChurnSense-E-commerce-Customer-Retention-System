import pandas as pd
import os


def load_datasets():
    """
    Load all required datasets from the raw data folder.
    """

    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    data_path = os.path.join(base_path, "data/raw")

    datasets = {}

    files = {
        "customers": "olist_customers_dataset.csv",
        "orders": "olist_orders_dataset.csv",
        "order_items": "olist_order_items_dataset.csv",
        "payments": "olist_order_payments_dataset.csv",
        "products": "olist_products_dataset.csv"
    }

    for name, file in files.items():
        file_path = os.path.join(data_path, file)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file} not found in {data_path}")

        datasets[name] = pd.read_csv(file_path)

    return datasets