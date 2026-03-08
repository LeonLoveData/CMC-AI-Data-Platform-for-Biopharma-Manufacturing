import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(df):

    model = IsolationForest(contamination=0.05)

    features = df.select_dtypes(include=["float64", "int64"])

    model.fit(features)

    df["anomaly"] = model.predict(features)

    return df


if __name__ == "__main__":

    df = pd.read_csv("data/processed/training_dataset.csv")

    result = detect_anomalies(df)

    result.to_csv("data/processed/anomaly_results.csv", index=False)

    print("Anomaly detection completed")
