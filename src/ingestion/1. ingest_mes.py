import pandas as pd

def load_mes_data(file_path):

    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    return df


def clean_mes_data(df):

    df = df.dropna()

    df["Yield"] = pd.to_numeric(df["Yield"], errors="coerce")

    return df


if __name__ == "__main__":

    df = load_mes_data("data/raw/batch_process.csv")

    df = clean_mes_data(df)

    df.to_csv("data/processed/mes_clean.csv", index=False)

    print("MES data processed")
