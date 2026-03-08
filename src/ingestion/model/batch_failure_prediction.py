import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train_classifier(df):

    X = df.drop(columns=["Batch_Status"])
    y = df["Batch_Status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print("Accuracy:", acc)

    return model


if __name__ == "__main__":

    df = pd.read_csv("data/processed/training_dataset.csv")

    train_classifier(df)
