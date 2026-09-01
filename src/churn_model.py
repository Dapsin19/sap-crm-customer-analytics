from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score


DATA_PATH = Path(
    "data/processed/customer_segments.csv"
)

OUTPUT_PATH = Path(
    "data/processed/churn_predictions.csv"
)


def train_churn_model():
    df = pd.read_csv(DATA_PATH)

    # Synthetic churn target based on CRM behavior.
    # This is explicitly a demonstration dataset.
    df["churn"] = (
        (
            (df["recency"] > df["recency"].median())
            & (df["avg_satisfaction"] < 3.5)
        )
        | (df["segment"].isin(["At Risk", "Lost Customers"]))
    ).astype(int)

    features = [
        "recency",
        "frequency",
        "monetary_value",
        "interaction_count",
        "avg_satisfaction",
        "avg_resolution_time",
        "complaints",
    ]

    X = df[features]
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced",
    )

    model.fit(X_train, y_train)

    probabilities = model.predict_proba(X_test)[:, 1]

    print("\nChurn Model")
    print("===========")
    print(
        f"ROC-AUC: {roc_auc_score(y_test, probabilities):.3f}"
    )

    predictions = model.predict(X)

    df["churn_probability"] = model.predict_proba(X)[:, 1]
    df["churn_prediction"] = predictions

    df["risk_level"] = pd.cut(
        df["churn_probability"],
        bins=[-0.01, 0.33, 0.66, 1.0],
        labels=["Low", "Medium", "High"],
    )

    df.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print("\nChurn Risk Distribution")
    print(
        df["risk_level"]
        .value_counts()
        .to_string()
    )

    print("\nClassification Report")
    print(
        classification_report(
            y_test,
            model.predict(X_test),
        )
    )


if __name__ == "__main__":
    train_churn_model()
