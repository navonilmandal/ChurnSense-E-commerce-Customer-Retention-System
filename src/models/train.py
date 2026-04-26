import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import joblib

from src.features.feature_engineering import create_features
from src.config import DATA_PROCESSED, MODEL_PATH


def train_model():
    df = pd.read_csv(f"{DATA_PROCESSED}/customer_data.csv")

    df = create_features(df)

    X = df.drop(columns=[
    "customer_unique_id",
    "churn",
    "recency_days",
    "last_purchase",
    "first_purchase"
])

    y = df["churn"]

    X = X.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = XGBClassifier(
        n_estimators=400,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight = len(y_train[y_train == 0]) / len(y_train[y_train == 1]),
        random_state=42
    )

    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    print("Model trained and saved.")


if __name__ == "__main__":
    train_model()