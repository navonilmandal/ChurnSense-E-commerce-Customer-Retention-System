
import pandas as pd

from src.models.train import train_model
from src.models.predict import predict
from src.business.strategy import assign_risk
from src.experiments.ab_testing import run_ab_test
from src.config import DATA_PROCESSED


def main():
    train_model()

    df = pd.read_csv(f"{DATA_PROCESSED}/customer_data.csv")

    df = predict(df)
    df = assign_risk(df)

    p_value = run_ab_test(df)

    print("Final P-value:", p_value)


if __name__ == "__main__":
       main()