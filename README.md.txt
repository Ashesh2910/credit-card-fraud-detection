# 💳 Credit Card Fraud Risk Dashboard

This project is an end-to-end **credit card fraud risk dashboard** built using
machine learning and Streamlit. It demonstrates how transaction-level data
can be transformed into actionable fraud risk insights for business and risk teams.

---

## 🔍 What This Project Does

- Scores transactions using a trained Random Forest model
- Classifies transactions into **Low / Medium / High risk**
- Visualizes fraud risk distribution and high-risk transactions
- Explains *why* a transaction was flagged using SHAP-style feature attribution
- Translates model outputs into **business impact metrics**

---

## 🧠 Why This Matters (Business Context)

Credit card fraud detection is not just about accuracy.
Risk teams must balance:
- Fraud loss prevention
- Customer friction
- Explainability and trust

This dashboard focuses on **interpretability and decision support**, not black-box ML.

---

## 📊 Key Features

- 📈 Risk KPIs (fraud rate, transaction volume, average amount)
- 🔎 Interactive filters (amount range, risk threshold)
- 🚨 High-risk transaction monitoring
- 🧠 Model explainability for individual transactions
- 💰 Estimated business impact of fraud prevention

---

## 🏗️ Architecture Overview

- **Model**: Random Forest (trained offline)
- **Dashboard**: Streamlit
- **Explainability**: SHAP-style feature contribution analysis
- **Data Storage**: External (Google Drive)
- **Deployment**: Streamlit Community Cloud

---

## 📂 Project Structure
fraud-risk-dashboard/
│
├── app.py # Streamlit dashboard
├── rf_model.joblib # Trained fraud detection model
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---


---

## ⚠️ Why the Dataset Is Not in This Repo

The processed fraud dataset exceeds GitHub’s file size limits.

Instead of committing large data files, the dashboard:
- Loads the dataset dynamically from Google Drive
- Caches it using Streamlit for performance
- Follows common cloud deployment best practices

This approach is widely used in production analytics systems.

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py


---

🌐 Live App

The dashboard is deployed on Streamlit Community Cloud
(http://localhost:8501/)

---

🧪 Dataset Source

The original dataset is based on publicly available European credit card
transaction data commonly used for fraud detection research.

---

📌 Disclaimer

This project is for educational and demonstration purposes only.
No real customer data is used.


---

## 4️⃣ How to add this README to GitHub

### Option A (easiest – recommended)

1. Go to your GitHub repo
2. Click on `README.md`
3. Click ✏️ **Edit**
4. Paste the content above
5. Click **Commit changes**

---

### Option B (upload from your computer)

1. Create `README.md` locally
2. Paste the content
3. Upload it along with:
   - `app.py`
   - `rf_model.joblib`
   - `requirements.txt`

---

## ✅ Why this README is strong

- Clear business framing (AmEx-style)
- Explains technical + non-technical choices
- Justifies Google Drive data loading
- Sounds like a real analytics project, not a tutorial

---

## Next (optional, but powerful)

I can:
- Rewrite this README to **match an AmEx job description**
- Add **screenshots section**
- Write a **2-minute interview walkthrough**
- Help you polish your **resume bullet**

Just tell me what you want next.

