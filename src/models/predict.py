import pandas as pd
import joblib

from src.config import MODEL_PATH
from src.features.feature_engineering import create_features


def predict(df):
    model = joblib.load(MODEL_PATH)

    df = create_features(df)

    X = df.drop(columns=[
        "customer_unique_id",
        "churn",
        "recency_days",
        "last_purchase",
        "first_purchase"
    ])

    X = X.fillna(0)

    df["churn_probability"] = model.predict_proba(X)[:, 1]

    return df