# 💳 Credit Card Fraud Risk Dashboard

An interactive fraud risk monitoring dashboard built using machine learning and explainable AI.
Designed to simulate how fraud analytics teams identify high-risk transactions, monitor fraud trends, and balance fraud loss prevention with customer experience.

🔍 Project Overview

Credit card fraud is a low-frequency but high-impact problem. This project analyzes transaction-level data to:

Identify fraud patterns and high-risk behaviors
Score transactions using a machine learning model
Visualize fraud risk distribution
Explain individual fraud predictions using SHAP

The dashboard is built with Streamlit and is suitable for real-world fraud analytics and decisioning use cases.

🧠 Key Features

Fraud Risk Scoring
   Uses a trained Random Forest model to assign fraud probability to each transaction
Interactive Filters
   Filter transactions by amount and risk threshold
Risk Tier Segmentation
   Low / Medium / High risk categorization for operational decisioning
Business Impact Metrics
   Estimated fraud loss prevented
   Estimated customer friction cost from false alerts
Explainable AI (SHAP)
   Feature-level explanation of why a transaction was flagged as high risk

📊 Dashboard Metrics
Total number of transactions
Fraud rate (%)
Average transaction amount
Risk tier distribution
High-risk transaction table
SHAP-based fraud explanations

🛠️ Tech Stack
Python
Streamlit – interactive dashboard
Pandas / NumPy – data processing
Scikit-learn – machine learning model
SHAP – model explainability
Matplotlib – visualizations
Google Drive – large dataset hosting

📁 Project Structure
Fraud_Dashboard/
│
├── app.py                 # Streamlit application
├── rf_model.joblib        # Trained Random Forest model
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation


⚠️ The dataset is not stored in the repository due to size constraints.
It is securely downloaded from Google Drive at runtime.

▶️ How to Run Locally
1️⃣ Clone the repository
    git clone <your-repo-url>
    cd Fraud_Dashboard

2️⃣ Install dependencies
    pip install -r requirements.txt

3️⃣ Run the app
    streamlit run app.py

The dashboard will open in your browser at:
http://localhost:8501

☁️ Deployment
  This app is compatible with Streamlit Community Cloud.
  To deploy:
  Push app.py, rf_model.joblib, requirements.txt, and README.md to GitHub
  Connect the repository to Streamlit Cloud
  Deploy directly from GitHub
The dataset is downloaded dynamically, so no large files are required in the repo.

📈 Business Use Case
  This project mirrors how financial institutions:
  Monitor transaction-level fraud risk
  Optimize fraud thresholds
  Reduce fraud losses
  Minimize customer friction
  Explain model decisions to stakeholders
