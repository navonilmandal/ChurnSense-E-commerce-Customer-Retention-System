import numpy as np
from scipy.stats import ttest_ind


def run_ab_test(df):
    np.random.seed(42)

    df["group"] = np.random.choice(["control", "treatment"], size=len(df))

    df["adjusted_churn"] = df["churn_probability"]

    df.loc[
        (df["group"] == "treatment") & (df["risk_segment"] == "High"),
        "adjusted_churn"
    ] *= 0.7

    control = df[df["group"] == "control"]["adjusted_churn"]
    treatment = df[df["group"] == "treatment"]["adjusted_churn"]

    _, p_value = ttest_ind(control, treatment)

    return p_value