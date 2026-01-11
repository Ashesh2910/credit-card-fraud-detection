💳 Credit Card Fraud Risk Dashboard

An end-to-end fraud analytics project combining machine learning, risk monitoring, business impact analysis, and explainable AI — delivered through an interactive Streamlit dashboard.

📌 Table of Contents

Overview

Business Problem

Solution Approach

Key Features

Dashboard Preview

Data

Modeling

Explainability (SHAP)

Business Impact

Project Structure

Tech Stack

Installation & Setup

Running the Application

Deployment

Design Decisions

Limitations

Future Improvements



🔍 Overview

Credit card fraud is a low-frequency, high-severity risk that requires accurate detection, interpretability, and operational decisioning.

This project builds a fraud risk monitoring dashboard that:

Scores transactions using a machine learning model

Segments transactions into risk tiers

Estimates business impact of fraud controls

Explains individual fraud predictions using SHAP

The result is a real-world simulation of how fraud analytics teams operate inside financial institutions.

💼 Business Problem

Financial institutions must:

Detect fraudulent transactions early

Minimize fraud losses

Reduce false positives that harm customer experience

Explain model decisions to regulators and stakeholders

This project focuses on balancing fraud prevention and customer friction, not just model accuracy.

🧠 Solution Approach

Transaction-level risk scoring using a Random Forest classifier

Risk tier segmentation (Low / Medium / High) for operational use

Interactive filtering to simulate analyst workflows

Explainable AI (SHAP) for transparency and trust

Business impact estimation to quantify decision trade-offs

✨ Key Features

📊 KPI monitoring (Fraud Rate, Transaction Volume, Avg Amount)

🎚️ Dynamic filters for transaction amount and risk threshold

🚨 High-risk transaction identification

🧠 SHAP-based feature attribution for individual transactions

💰 Fraud loss vs customer friction estimation

☁️ Cloud-ready deployment with large dataset handling

🖥️ Dashboard Preview

The dashboard includes:

Summary KPIs

Risk tier distribution chart

High-risk transaction table

SHAP explanation bar chart

Decision strategy recommendations

Built with Streamlit for fast, interactive analytics.

📂 Data

Public credit card transaction dataset

Highly imbalanced fraud vs non-fraud classes

Dataset size exceeds GitHub limits

📌 Note:
The dataset is not stored in the repository.
It is downloaded securely from Google Drive at runtime.

🤖 Modeling

Algorithm: Random Forest Classifier

Objective: Fraud probability estimation

Focus: Interpretability over complex modeling

Output: Transaction-level fraud risk score

Model artifacts are stored as serialized files (.joblib) for reuse.

🧠 Explainability (SHAP)

To ensure transparency:

SHAP is used to explain individual fraud predictions

Feature contributions are visualized for high-risk transactions

Positive SHAP values increase fraud risk

Negative SHAP values reduce fraud risk

This mirrors real-world regulatory and stakeholder requirements.

💰 Business Impact

The dashboard estimates:

Fraud loss prevented from blocking true fraud

Customer friction cost from false positives

This helps simulate:

Threshold tuning decisions

Risk appetite trade-offs

Operational strategy

📁 Project Structure
Fraud_Dashboard/
│
├── app.py                 # Streamlit dashboard application
├── rf_model.joblib        # Trained Random Forest model
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

🧰 Tech Stack

Python

Streamlit

Pandas

NumPy

Scikit-learn

SHAP

Matplotlib

Joblib

Google Drive (dataset hosting)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <your-repo-url>
cd Fraud_Dashboard

2️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the Application
streamlit run app.py


Open your browser at:

http://localhost:8501

☁️ Deployment

The app is compatible with Streamlit Community Cloud.

Deployment steps:

Push code to GitHub

Connect the repository to Streamlit Cloud

Deploy directly from the main branch

Large datasets are handled dynamically and do not block deployment.

🧩 Design Decisions

Used Random Forest for interpretability and stability

Prioritized explainability over complex ML models

Focused on business metrics, not just accuracy

Built modular, cloud-friendly architecture

⚠️ Limitations

Uses historical transaction data

No real-time streaming

Assumes static model (no retraining pipeline)

These trade-offs were intentional for clarity and interpretability.

🚀 Future Improvements

Real-time fraud scoring simulation

Customer-level risk aggregation

Time-series fraud trend monitoring

Model retraining pipeline

Alert workflow integration

