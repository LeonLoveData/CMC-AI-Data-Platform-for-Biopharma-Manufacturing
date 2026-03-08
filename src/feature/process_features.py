import pandas as pd


def create_process_features(sensor_df):

    features = sensor_df.groupby("Batch_ID").agg(
        Temperature_mean=("Temperature", "mean"),
        Temperature_max=("Temperature", "max"),
        Pressure_mean=("Pressure", "mean"),
        Pressure_max=("Pressure", "max"),
        pH_mean=("pH", "mean"),
        pH_std=("pH", "std")
    ).reset_index()

    return features


if __name__ == "__main__":

    sensor = pd.read_csv("data/raw/sensor_timeseries.csv")

    features = create_process_features(sensor)

    features.to_csv("data/processed/process_features.csv", index=False)

    print("Process features generated")
