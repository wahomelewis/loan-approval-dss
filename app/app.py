import streamlit as st
import pickle
import numpy as np
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Loan DSS", layout="wide")

# ---------------- DARK THEME ----------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    h1, h2, h3 {
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model_path = os.path.join(os.path.dirname(__file__), "..", "loan_model.pkl")
model = pickle.load(open(model_path, "rb"))

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align: center;'>🏦 Loan Risk Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'> Loan Decision Support System</p>", unsafe_allow_html=True)

st.divider()

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("📊 Applicant Inputs")

income = st.sidebar.number_input("💰 Income", min_value=1)
loan = st.sidebar.number_input("🏦 Loan Amount", min_value=0)
credit = st.sidebar.number_input("📊 Credit Score", min_value=300, max_value=900)
interest = st.sidebar.number_input("📈 Interest Rate", min_value=0.0)
emp_years = st.sidebar.number_input("💼 Employment Years", min_value=0)
credit_hist_years = st.sidebar.number_input("📚 Credit History Length", min_value=0)

# ---------------- MAIN ----------------
if st.sidebar.button("🚀 Analyze Risk"):

    # Create feature
    loan_to_income = loan / (income + 1)

    input_data = np.array([[
        loan_to_income,
        credit,
        interest,
        emp_years,
        credit_hist_years
    ]])

    prob = model.predict_proba(input_data)[0][1] * 100

    st.subheader("📊 Decision Outcome")

    if prob > 30:
        st.error(f"❌ HIGH RISK ({prob:.2f}%)")
    else:
        st.success(f"✅ LOW RISK ({prob:.2f}%)")

    # Risk level
    if prob > 70:
        st.error("🔴 Risk Level: HIGH")
    elif prob > 30:
        st.warning("🟠 Risk Level: MEDIUM")
    else:
        st.success("🟢 Risk Level: LOW")

    st.subheader("📉 Risk Visualization")
    st.progress(int(prob))

    st.subheader("📌 Risk Summary")

    if prob > 70:
        st.error("The applicant demonstrates a high likelihood of default.")
    elif prob > 30:
        st.warning("The applicant presents moderate risk. Further review recommended.")
    else:
        st.success("The applicant shows low likelihood of default.")

    st.subheader("📈 Key Indicator")
    st.metric("Loan-to-Income Ratio", f"{loan_to_income:.2f}")