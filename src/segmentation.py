from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


DATA_PATH = Path("data/processed/customer_360.csv")
OUTPUT_PATH = Path("data/processed/customer_segments.csv")


def segment_customers():
    df = pd.read_csv(DATA_PATH)

    features = [
        "recency",
        "frequency",
        "monetary_value",
    ]

    X = df[features].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10,
    )

    df["cluster"] = model.fit_predict(X_scaled)

    cluster_summary = (
        df.groupby("cluster")
        .agg(
            customers=("customer_id", "count"),
            avg_recency=("recency", "mean"),
            avg_frequency=("frequency", "mean"),
            avg_revenue=("monetary_value", "mean"),
        )
        .reset_index()
    )

    # Rank clusters by revenue/frequency/recency
    cluster_summary["score"] = (
        cluster_summary["avg_frequency"]
        + cluster_summary["avg_revenue"]
        - cluster_summary["avg_recency"]
    )

    cluster_summary = cluster_summary.sort_values(
        "score",
        ascending=False,
    )

    labels = [
        "Champions",
        "Loyal Customers",
        "Potential Loyalists",
        "At Risk",
        "Lost Customers",
    ]

    label_map = {}

    for cluster, label in zip(
        cluster_summary["cluster"],
        labels,
    ):
        label_map[cluster] = label

    df["segment"] = df["cluster"].map(label_map)

    df.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print("\nCustomer Segmentation")
    print("=====================")
    print(
        df["segment"]
        .value_counts()
        .to_string()
    )

    return df


if __name__ == "__main__":
    segment_customers()
