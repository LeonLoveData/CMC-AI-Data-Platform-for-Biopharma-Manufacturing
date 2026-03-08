import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor


def train_model(df):

    X = df.drop(columns=["Total_Impurity"])
    y = df["Total_Impurity"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBRegressor()

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    score = r2_score(y_test, preds)

    print("R2 Score:", score)

    return model


if __name__ == "__main__":

    df = pd.read_csv("data/processed/training_dataset.csv")

    train_model(df)
