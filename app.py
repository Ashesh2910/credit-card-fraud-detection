import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import matplotlib.pyplot as plt
import shap
import gdown
import os

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Credit Card Fraud Risk Dashboard",
    layout="wide"
)

# ---------------- Load Data ----------------
@st.cache_data(show_spinner=True)
def load_data():
    file_id = "149oBfaal1fWGH2UyAmy7gucByIqsP5lD"
    output = "fraud_processed.csv"

    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)

    return pd.read_csv(output)

# ---------------- Load Model ----------------
@st.cache_resource(show_spinner=True)
def load_model():
    return load("rf_model.joblib")

df = load_data()
model = load_model()

# ---------------- Detect Target Column ----------------
possible_targets = ["Class", "class", "is_fraud", "fraud", "target", "label"]
TARGET_COL = next((c for c in possible_targets if c in df.columns), None)

if TARGET_COL is None:
    st.error("❌ No fraud target column found in dataset.")
    st.write("Available columns:", list(df.columns))
    st.stop()

# ---------------- Feature Consistency ----------------
MODEL_FEATURES = list(model.feature_names_in_)

# ---------------- Header ----------------
st.title("💳 Credit Card Fraud Risk Dashboard")
st.caption(
    "Interactive risk monitoring dashboard using machine learning. "
    "Designed for fraud analytics and decisioning teams."
)

st.divider()

# ---------------- KPI SECTION ----------------
k1, k2, k3 = st.columns(3)
k1.metric("Total Transactions", f"{len(df):,}")
k2.metric("Fraud Rate (%)", f"{df[TARGET_COL].mean() * 100:.3f}")
k3.metric("Avg Transaction Amount", f"{df['Amount'].mean():.2f}")

st.divider()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("🔍 Filters")

amount_range = st.sidebar.slider(
    "Transaction Amount Range",
    float(df["Amount"].min()),
    float(df["Amount"].max()),
    (0.0, float(df["Amount"].quantile(0.95)))
)

risk_threshold = st.sidebar.slider(
    "High Risk Threshold",
    0.1, 0.9, 0.3
)

filtered_df = df[
    (df["Amount"] >= amount_range[0]) &
    (df["Amount"] <= amount_range[1])
].copy()

# ---------------- Risk Scoring ----------------
filtered_df["risk_score"] = model.predict_proba(
    filtered_df[MODEL_FEATURES]
)[:, 1]

filtered_df["risk_tier"] = pd.cut(
    filtered_df["risk_score"],
    bins=[0, risk_threshold, 0.6, 1],
    labels=["Low", "Medium", "High"]
)

# ---------------- Risk Distribution ----------------
st.subheader("📊 Risk Tier Distribution")

risk_counts = filtered_df["risk_tier"].value_counts().sort_index()

fig, ax = plt.subplots()
risk_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Risk Tier")
ax.set_ylabel("Number of Transactions")
st.pyplot(fig)

st.divider()

# ---------------- High Risk Transactions ----------------
st.subheader("🚨 High Risk Transactions")

high_risk = filtered_df[filtered_df["risk_tier"] == "High"]

st.dataframe(
    high_risk[["Time", "Amount", "risk_score"]]
    .sort_values("risk_score", ascending=False)
    .head(20),
    use_container_width=True
)

# ---------------- Business Impact ----------------
st.subheader("💰 Estimated Business Impact")

FRAUD_COST = 1000
FALSE_ALERT_COST = 20

tp = len(high_risk[high_risk[TARGET_COL] == 1])
fp = len(high_risk[high_risk[TARGET_COL] == 0])

c1, c2 = st.columns(2)
c1.metric("Fraud Loss Prevented", f"${tp * FRAUD_COST:,}")
c2.metric("Customer Friction Cost", f"${fp * FALSE_ALERT_COST:,}")

st.divider()

# ---------------- SHAP EXPLANATION ----------------
st.subheader("🧠 Why was this transaction flagged?")

if not high_risk.empty:
    idx = st.selectbox(
        "Select high-risk transaction index:",
        high_risk.index
    )

    explainer = shap.TreeExplainer(model)
    shap_vals = explainer.shap_values(
        filtered_df.loc[[idx], MODEL_FEATURES]
    )

    # Handle SHAP output safely
    if isinstance(shap_vals, list):
        shap_contrib = shap_vals[-1][0]  # fraud class
    else:
        shap_contrib = shap_vals[0]

    shap_contrib = np.asarray(shap_contrib).flatten()

    # HARD SAFETY: align feature & SHAP lengths
    min_len = min(len(MODEL_FEATURES), len(shap_contrib))

    shap_df = (
        pd.DataFrame({
            "Feature": MODEL_FEATURES[:min_len],
            "Impact": shap_contrib[:min_len]
        })
        .assign(abs_val=lambda x: x["Impact"].abs())
        .sort_values("abs_val", ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots()
    ax.barh(
        shap_df["Feature"],
        shap_df["Impact"],
        color=["red" if v > 0 else "green" for v in shap_df["Impact"]]
    )
    ax.invert_yaxis()
    ax.set_xlabel("Impact on Fraud Risk")
    ax.set_title("Top Drivers of Fraud Risk")
    st.pyplot(fig)

else:
    st.info("No high-risk transactions available for explanation.")

st.divider()

# ---------------- Decision Logic ----------------
st.markdown("""
### 🧠 Decision Strategy
- **Low Risk** → Auto-approve  
- **Medium Risk** → Step-up authentication  
- **High Risk** → Block or manual review  

Threshold tuning balances fraud loss prevention and customer experience.
""")
