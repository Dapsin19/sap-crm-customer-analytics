import json
from pathlib import Path

import pandas as pd


RAW_DIR = Path("data/raw")
OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    with open(RAW_DIR / "customers.json") as f:
        customers = pd.DataFrame(json.load(f))

    with open(RAW_DIR / "orders.json") as f:
        orders = pd.DataFrame(json.load(f))

    with open(RAW_DIR / "interactions.json") as f:
        interactions = pd.DataFrame(json.load(f))

    return customers, orders, interactions


def build_customer_360():
    customers, orders, interactions = load_data()

    orders = orders[orders["order_status"] == "Completed"].copy()

    orders["order_date"] = pd.to_datetime(
        orders["order_date"]
    )

    interactions["interaction_date"] = pd.to_datetime(
        interactions["interaction_date"]
    )

    reference_date = orders["order_date"].max()

    rfm = (
        orders.groupby("customer_id")
        .agg(
            recency=(
                "order_date",
                lambda x: (reference_date - x.max()).days,
            ),
            frequency=("order_id", "nunique"),
            monetary_value=("revenue", "sum"),
        )
        .reset_index()
    )

    interaction_summary = (
        interactions.groupby("customer_id")
        .agg(
            interaction_count=("interaction_id", "count"),
            avg_satisfaction=("satisfaction_score", "mean"),
            avg_resolution_time=("resolution_time_hours", "mean"),
            complaints=(
                "interaction_type",
                lambda x: (x == "Complaint").sum(),
            ),
        )
        .reset_index()
    )

    customer_360 = (
        customers
        .merge(rfm, on="customer_id", how="left")
        .merge(
            interaction_summary,
            on="customer_id",
            how="left",
        )
    )

    numeric_columns = [
        "recency",
        "frequency",
        "monetary_value",
        "interaction_count",
        "avg_satisfaction",
        "avg_resolution_time",
        "complaints",
    ]

    customer_360[numeric_columns] = customer_360[
        numeric_columns
    ].fillna(0)

    customer_360["customer_lifetime_value"] = (
        customer_360["monetary_value"]
    )

    customer_360.to_csv(
        OUTPUT_DIR / "customer_360.csv",
        index=False,
    )

    print("\nCustomer 360 created")
    print("====================")
    print(f"Customers: {len(customer_360)}")

    return customer_360


if __name__ == "__main__":
    build_customer_360()
