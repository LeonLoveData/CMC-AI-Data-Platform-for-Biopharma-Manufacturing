import pandas as pd


def load_lims_data(file_path):

    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    return df


def clean_lims_data(df):

    df = df.dropna()

    df["Total_Impurity"] = pd.to_numeric(df["Total_Impurity"], errors="coerce")

    return df


if __name__ == "__main__":

    df = load_lims_data("data/raw/hplc_results.csv")

    df = clean_lims_data(df)

    df.to_csv("data/processed/lims_clean.csv", index=False)

    print("LIMS data processed")
