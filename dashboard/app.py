import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="SAP CRM Customer Analytics",
    layout="wide",
)

st.title("SAP CRM Customer Analytics")

df = pd.read_csv(
    "data/processed/churn_predictions.csv"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    f"{len(df):,}",
)

col2.metric(
    "Total Customer Revenue",
    f"€{df['monetary_value'].sum():,.0f}",
)

col3.metric(
    "Average Satisfaction",
    f"{df['avg_satisfaction'].mean():.2f}/5",
)

high_risk = (
    df["risk_level"] == "High"
).sum()

col4.metric(
    "High Churn Risk",
    f"{high_risk:,}",
)

st.divider()

st.subheader("Customer Segmentation")

segment_counts = (
    df["segment"]
    .value_counts()
)

st.bar_chart(segment_counts)

st.subheader("Revenue by Customer Segment")

revenue_by_segment = (
    df.groupby("segment")["monetary_value"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(revenue_by_segment)

st.subheader("Churn Risk")

risk_counts = (
    df["risk_level"]
    .value_counts()
)

st.bar_chart(risk_counts)

st.subheader("High-Risk Customers")

high_risk_customers = (
    df[df["risk_level"] == "High"]
    [
        [
            "customer_id",
            "industry",
            "segment",
            "monetary_value",
            "avg_satisfaction",
            "churn_probability",
            "risk_level",
        ]
    ]
    .sort_values(
        "churn_probability",
        ascending=False,
    )
)

st.dataframe(
    high_risk_customers.head(25),
    use_container_width=True,
)
