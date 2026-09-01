from pathlib import Path

import pandas as pd


DATA_DIR = Path("data/processed")


def test_customer_360_exists():
    path = DATA_DIR / "customer_360.csv"

    assert path.exists()

    df = pd.read_csv(path)

    assert len(df) == 1000
    assert df["customer_id"].is_unique


def test_customer_references():
    customers = pd.read_csv(
        DATA_DIR / "customer_360.csv"
    )

    assert customers["customer_id"].notna().all()


def test_customer_segments():
    df = pd.read_csv(
        DATA_DIR / "customer_segments.csv"
    )

    expected_segments = {
        "Champions",
        "Loyal Customers",
        "Potential Loyalists",
        "At Risk",
        "Lost Customers",
    }

    assert set(df["segment"]).issubset(
        expected_segments
    )


def test_churn_predictions():
    df = pd.read_csv(
        DATA_DIR / "churn_predictions.csv"
    )

    assert "churn_probability" in df.columns

    assert df["churn_probability"].between(
        0,
        1,
    ).all()


def test_no_negative_revenue():
    df = pd.read_csv(
        DATA_DIR / "customer_360.csv"
    )

    assert (df["monetary_value"] >= 0).all()
