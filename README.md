# SAP CRM Customer Analytics & Segmentation

A customer analytics prototype demonstrating SAP CRM-oriented customer analysis, segmentation, predictive analytics, reporting, data quality testing, and ABAP Objects concepts.

> **Important:** This is a portfolio/learning project using synthetic CRM data. It was not developed against a production SAP CRM or SAP S/4HANA system.

## Project Overview

Customer Relationship Management (CRM) systems generate valuable information about customers, purchases, interactions, and service experiences.

This project simulates a CRM analytics workflow in which customer, sales-order, and interaction data are integrated into a **Customer 360** dataset and analyzed to support customer segmentation, churn-risk identification, and CRM decision-making.

```text
CRM Customer Data
       │
       ├── Customers
       ├── Sales Orders
       └── Interactions
              │
              ▼
       Data Integration
              │
              ▼
        Customer 360
              │
       ┌──────┴─────────┐
       ▼                ▼
  RFM Analysis     Interaction
       │             Analysis
       ▼                │
 Customer          Customer
 Segmentation      Experience
       │                │
       └──────┬─────────┘
              ▼
       Churn Prediction
              │
              ▼
      CRM Reporting
              │
              ▼
       Business Actions
```

## Business Objectives

The project addresses common CRM analytics questions:

* Which customers generate the most revenue?
* Which customers are the most valuable?
* Which customers are at risk of churn?
* Which customer segments should receive retention or upselling campaigns?
* Which CRM interaction channels produce better customer satisfaction?
* Does customer service performance relate to customer risk?
* How can CRM data be transformed into actionable reports?

## Key Features

### Customer 360

Combines:

* Customer demographics
* Customer type
* Industry
* Region
* Sales activity
* Revenue
* Purchase frequency
* Recency
* Customer interactions
* Satisfaction
* Complaints
* Resolution time

### RFM Customer Segmentation

Customers are segmented using:

* **Recency** — how recently the customer purchased
* **Frequency** — how often the customer purchased
* **Monetary Value** — how much revenue the customer generated

K-Means clustering is used to identify customer groups.

Example segments:

* Champions
* Loyal Customers
* Potential Loyalists
* At Risk
* Lost Customers

### Predictive Analytics

A Random Forest model estimates customer churn risk using CRM behavior and customer-experience features.

Example features:

```text
recency
frequency
monetary_value
interaction_count
avg_satisfaction
avg_resolution_time
complaints
```

The resulting dataset includes:

```text
customer_id
churn_probability
risk_level
```

Customers are classified into:

* Low risk
* Medium risk
* High risk

### CRM Process Analysis

Customer interactions are analyzed using:

* Interaction channel
* Interaction type
* Resolution time
* Satisfaction score
* Complaints

This supports analysis of customer experience and CRM service processes.

## Dashboard

The Streamlit dashboard provides:

* Total customers
* Customer revenue
* Average satisfaction
* High-risk customer count
* Customer segment distribution
* Revenue by segment
* Churn-risk distribution
* High-risk customer table

Run the dashboard with:

```bash
streamlit run dashboard/app.py
```

## SAP / ABAP Component

The project includes an ABAP Objects-style customer analysis component:

```text
abap/
├── zcrm_customer_report.abap
└── README.md
```

The ABAP component demonstrates:

* ABAP report structure
* ABAP Objects
* Local classes
* Methods
* Importing parameters
* Returning parameters
* Structured types
* Conditional business logic
* Customer classification
* CRM reporting concepts

The ABAP component uses customer revenue, purchase frequency, and recency to classify customers into CRM segments.

### Important

The ABAP implementation is a learning artifact demonstrating ABAP Objects concepts. It was not executed against a production SAP system.

## Data Model

### Customers

```text
customer_id
customer_type
industry
region
registration_date
annual_revenue
customer_status
```

### Sales Orders

```text
order_id
customer_id
order_date
product_id
quantity
revenue
order_status
```

### Customer Interactions

```text
interaction_id
customer_id
interaction_date
channel
interaction_type
resolution_time_hours
satisfaction_score
```

## Technology Stack

| Technology   | Purpose                                        |
| ------------ | ---------------------------------------------- |
| Python       | Data processing and analytics                  |
| Pandas       | Data transformation                            |
| NumPy        | Numerical processing                           |
| Scikit-learn | Customer segmentation and predictive analytics |
| Streamlit    | CRM analytics dashboard                        |
| Matplotlib   | Visualization                                  |
| Pytest       | Automated testing                              |
| ABAP         | SAP-oriented reporting demonstration           |
| ABAP Objects | Object-oriented customer analysis              |
| JSON         | CRM data ingestion                             |
| Git/GitHub   | Version control                                |

## Project Structure

```text
sap-crm-customer-analytics/
│
├── data/
│   ├── raw/
│   │   ├── customers.json
│   │   ├── orders.json
│   │   └── interactions.json
│   │
│   └── processed/
│       ├── customer_360.csv
│       ├── customer_segments.csv
│       └── churn_predictions.csv
│
├── src/
│   ├── __init__.py
│   ├── generate_data.py
│   ├── customer_analytics.py
│   ├── segmentation.py
│   └── churn_model.py
│
├── dashboard/
│   └── app.py
│
├── abap/
│   ├── zcrm_customer_report.abap
│   └── README.md
│
├── tests/
│   └── test_crm_pipeline.py
│
├── notebooks/
│   └── customer_analytics.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Running the Project

### 1. Clone

```bash
git clone https://github.com/Dapsin19/sap-crm-customer-analytics.git
cd sap-crm-customer-analytics
```

### 2. Create environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate CRM data

```bash
python src/generate_data.py
```

### 5. Build Customer 360

```bash
python src/customer_analytics.py
```

### 6. Segment customers

```bash
python src/segmentation.py
```

### 7. Predict churn risk

```bash
python src/churn_model.py
```

### 8. Run tests

```bash
python -m pytest -v
```

### 9. Launch dashboard

```bash
streamlit run dashboard/app.py
```

## Data Quality & Testing

Automated tests verify:

* Customer dataset availability
* Customer ID uniqueness
* Valid customer references
* Valid segmentation labels
* Churn probabilities between 0 and 1
* Non-negative customer revenue

Run:

```bash
python -m pytest -v
```

## Example Business Applications

The resulting CRM analytics could support:

### Customer Retention

Identify high-value customers with elevated churn risk and prioritize them for retention campaigns.

### Upselling

Identify loyal or high-value customers with opportunities for additional products or services.

### Customer Experience

Investigate relationships between resolution time, satisfaction, complaints, and customer risk.

### CRM Reporting

Provide management with customer KPIs, segment distributions, revenue analysis, and risk indicators.

## Limitations

This project uses synthetic data and therefore does not represent the complexity of a production SAP CRM environment.

It does not claim production experience with:

* SAP CRM
* SAP S/4HANA
* SAP BW
* SAP HANA
* SAP ABAP development systems

The purpose is to demonstrate transferable CRM analytics, data engineering, predictive analytics, testing, reporting, and introductory ABAP Objects concepts.

## Future Improvements

Potential extensions include:

* SAP OData integration
* SAP HANA integration
* SAP BW analytics
* SAP S/4HANA customer data integration
* Production Fiori reporting
* Real ABAP development-system execution
* ABAP CDS Views
* SQL-based CRM analytics
* Power BI dashboard
* REST API integration
* Docker deployment
* CI/CD with GitHub Actions

## Skills Demonstrated

**CRM & Business Analytics**

* Customer 360
* Customer segmentation
* RFM analysis
* Customer lifetime value
* Churn analysis
* Customer experience analytics
* CRM reporting

**Data Science**

* Feature engineering
* K-Means clustering
* Random Forest
* Predictive analytics
* Model evaluation

**Data Engineering**

* JSON ingestion
* Data transformation
* Data quality checks
* Analytics-ready datasets

**SAP / ABAP**

* SAP CRM concepts
* ABAP fundamentals
* ABAP Objects
* Customer reporting logic
* SAP-oriented business process modeling

**Software Engineering**

* Modular Python
* Automated testing
* Virtual environments
* Git/GitHub

