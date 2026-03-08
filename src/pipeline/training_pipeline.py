import pandas as pd

from src.models.impurity_prediction import train_model
from src.models.batch_failure_prediction import train_classifier


def load_training_data():

    df = pd.read_csv("data/processed/training_dataset.csv")

    return df


def run_pipeline():

    df = load_training_data()

    print("Training impurity model")

    train_model(df)

    print("Training batch failure model")

    train_classifier(df)


if __name__ == "__main__":

    run_pipeline()
