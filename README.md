# SAP CRM Customer Analytics & Segmentation

A hands-on SAP CRM-oriented customer analytics project combining **customer data modeling, CRM process analysis, customer segmentation, predictive analytics, reporting, and ABAP Objects development**.

The project simulates an enterprise CRM environment using synthetic customer, sales, and interaction data and demonstrates how CRM data can be transformed into actionable insights for customer experience, retention, and business decision-making.

---

## Project Objectives

The project was built to demonstrate practical understanding of CRM analytics workflows and SAP-oriented development concepts, including:

* Customer 360 analysis
* Customer segmentation
* RFM analysis
* Predictive customer churn analytics
* CRM process and customer-experience analysis
* Customer reporting
* Data integration and transformation
* ABAP Objects
* Structured business logic
* Automated testing
* Analytics dashboards

---

## Architecture

```text
             CRM Customer Data
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   Customers      Orders    Interactions
       │            │            │
       └────────────┼────────────┘
                    ▼
             Data Integration
                    │
                    ▼
              Customer 360
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     RFM Analysis       CRM Experience
          │                Analysis
          ▼                   │
     Segmentation             │
          │                   │
          └─────────┬─────────┘
                    ▼
             Churn Prediction
                    │
                    ▼
             CRM Reporting
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Dashboard          ABAP Objects
                         Reporting
```

---

# 1. Customer 360 Analytics

The project integrates three CRM-style datasets:

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

These datasets are linked through `customer_id` to create a consolidated **Customer 360 view**.

The resulting dataset contains:

* Purchase recency
* Purchase frequency
* Monetary value
* Customer lifetime value
* Number of interactions
* Average satisfaction
* Resolution time
* Complaint frequency

This provides the analytical foundation for CRM decision-making.

---

# 2. Customer Segmentation

Customers are segmented using **RFM analysis** and K-Means clustering.

### RFM dimensions

**Recency**

How recently did the customer purchase?

**Frequency**

How frequently does the customer purchase?

**Monetary Value**

How much revenue does the customer generate?

The resulting customer groups include:

```text
Champions
Loyal Customers
Potential Loyalists
At Risk
Lost Customers
```

The segmentation can support CRM activities such as:

* Customer retention
* Cross-selling
* Upselling
* Win-back campaigns
* High-value customer management

---

# 3. Predictive Customer Analytics

A Random Forest classification model is used to estimate customer churn risk.

Features include:

```text
recency
frequency
monetary_value
interaction_count
avg_satisfaction
avg_resolution_time
complaints
```

The model generates:

```text
customer_id
churn_probability
risk_level
```

Customers are classified as:

```text
Low Risk
Medium Risk
High Risk
```

This allows CRM teams to prioritize customers who may require proactive engagement.

> The churn target is synthetically generated from customer behavior because the dataset does not contain historical real-world churn labels.

---

# 4. CRM Process & Customer Experience Analysis

CRM interactions are analyzed to understand customer experience and service performance.

The project examines:

* Interaction channels
* Support requests
* Complaints
* Resolution times
* Satisfaction scores
* Customer segments
* Churn risk

This allows questions such as:

* Which interaction channels produce higher satisfaction?
* Which customers generate the most support activity?
* Does longer resolution time coincide with lower satisfaction?
* Are customers with more complaints more likely to be high-risk?
* Which customer segments require additional CRM attention?

The objective is to connect **operational CRM processes with customer outcomes**.

---

# 5. CRM Reporting Dashboard

A Streamlit dashboard provides an interactive CRM management view.

### Dashboard KPIs

* Total customers
* Total customer revenue
* Average customer satisfaction
* High-risk customer count

### Dashboard analyses

* Customer segment distribution
* Revenue by customer segment
* Churn-risk distribution
* High-risk customer identification

Run the dashboard:

```bash
streamlit run dashboard/app.py
```

---

# 6. ABAP Objects Customer Analysis

The project includes an ABAP Objects implementation of customer classification logic.

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
* Structured types
* Importing parameters
* Returning parameters
* Conditional business logic
* Customer segmentation
* CRM reporting logic

The customer-analysis class applies business rules using:

```text
Revenue
Purchase Frequency
Recency
```

to classify customers into CRM segments.

Example structure:

```abap
CLASS lcl_customer_analysis DEFINITION.

  PUBLIC SECTION.

    METHODS:
      calculate_segment
        IMPORTING
          iv_revenue TYPE p
          iv_frequency TYPE i
          iv_recency TYPE i
        RETURNING
          VALUE(rv_segment) TYPE string.

ENDCLASS.
```

This demonstrates how CRM business rules can be encapsulated using **object-oriented ABAP concepts**.

---

# 7. Data Integration

The Python pipeline demonstrates an ETL-style CRM workflow:

```text
Raw CRM Data
     ↓
Data Validation
     ↓
Data Integration
     ↓
Customer 360
     ↓
Analytics
     ↓
Reporting
```

The pipeline transforms JSON-based CRM data into structured, analytics-ready CSV datasets.

Output datasets include:

```text
customer_360.csv
customer_segments.csv
churn_predictions.csv
```

---

# 8. Data Quality & Testing

Automated tests are implemented with Pytest.

The tests verify:

* Customer dataset availability
* Customer ID uniqueness
* Valid customer references
* Valid segmentation labels
* Churn probability ranges
* Non-negative revenue

Run:

```bash
python -m pytest -v
```

---

# Technology Stack

| Technology   | Purpose                               |
| ------------ | ------------------------------------- |
| Python       | CRM data processing and analytics     |
| Pandas       | Data transformation                   |
| NumPy        | Numerical processing                  |
| Scikit-learn | Segmentation and predictive analytics |
| Streamlit    | CRM dashboard                         |
| Matplotlib   | Visualization                         |
| Pytest       | Automated testing                     |
| ABAP         | SAP-oriented business logic           |
| ABAP Objects | Object-oriented CRM analysis          |
| JSON         | Data interchange                      |
| Git/GitHub   | Version control                       |

---

# Project Structure

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

---

# Running the Project

## Clone

```bash
git clone https://github.com/Dapsin19/sap-crm-customer-analytics.git
cd sap-crm-customer-analytics
```

## Create environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Generate CRM data

```bash
python src/generate_data.py
```

## Build Customer 360

```bash
python src/customer_analytics.py
```

## Run segmentation

```bash
python src/segmentation.py
```

## Run predictive analytics

```bash
python src/churn_model.py
```

## Run tests

```bash
python -m pytest -v
```

## Launch dashboard

```bash
streamlit run dashboard/app.py
```

---

# Business Applications

The project demonstrates how CRM analytics can support:

### Customer Retention

Identify high-value customers with elevated churn risk.

### Customer Segmentation

Group customers according to purchasing behavior and value.

### Customer Experience Management

Analyze service interactions, satisfaction, complaints, and resolution times.

### Sales Optimization

Identify customers suitable for cross-selling and upselling.

### Management Reporting

Provide customer KPIs, revenue analysis, segmentation, and risk indicators.

---

# SAP & ABAP Learning Scope

This project is deliberately designed as a **hands-on SAP CRM and ABAP learning project** rather than a claim of production SAP consulting experience.

The implementation focuses on understanding how:

```text
CRM Business Requirements
        ↓
Customer Data
        ↓
Business Logic
        ↓
ABAP Objects
        ↓
Analytics & Reporting
```

can work together in an enterprise environment.

The Python components provide the data-engineering and analytics layer, while the ABAP component demonstrates how customer-classification business logic can be represented using ABAP Objects.

---

# Limitations

The CRM datasets are synthetic and created specifically for this project.

The project does not use confidential customer information or production SAP data.

The ABAP component is a portfolio implementation and should be considered a demonstration of ABAP Objects concepts rather than evidence of production SAP ABAP development experience.

Similarly, the project simulates SAP CRM-oriented processes rather than claiming implementation experience with a live SAP CRM system.

---

# Future SAP Extensions

The project can be extended toward a more complete SAP environment through:

* SAP S/4HANA integration
* SAP CRM APIs
* OData services
* SAP HANA
* SAP BW
* ABAP CDS Views
* SAP Fiori reporting
* SAP Business Technology Platform
* Real SAP development-system implementation
* Integration with external CRM systems

---

# Skills Demonstrated

### CRM & Customer Analytics

* Customer 360
* RFM analysis
* Customer segmentation
* Customer lifetime value
* Churn prediction
* Customer experience analytics
* CRM reporting

### SAP / ABAP

* SAP CRM concepts
* ABAP fundamentals
* ABAP Objects
* Object-oriented business logic
* Customer reporting
* CRM-oriented business processes

### Data Science

* Feature engineering
* K-Means clustering
* Random Forest
* Predictive modeling
* Model evaluation

### Data Engineering

* JSON ingestion
* Data transformation
* Data integration
* Data quality validation
* Analytics-ready datasets

### Software Engineering

* Modular Python
* Automated testing
* Git/GitHub
* Reproducible development workflows

---

## Author

**Dapsin19**

Data Science · Healthcare AI · Customer Analytics · SAP/ABAP Learning · Data Engineering
