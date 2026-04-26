import pandas as pd

def assign_risk(df):
    df["risk_segment"] = pd.cut(
        df["churn_probability"],
        bins=[0, 0.2, 0.5, 0.8, 1],
        labels=["Very Low", "Low", "Medium", "High"]
    )
    return df