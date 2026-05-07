# Import libraries
import streamlit as st
import pickle
import pandas as pd
import statsmodels.api as sm

# Page config
st.set_page_config(page_title="Loan Risk Predictor", page_icon="🏦", layout="wide")

# ----------- STYLE -----------
st.markdown("""
    <style>
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #125a8a;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- LOAD MODEL -----------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ----------- LOGIN SYSTEM -----------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.sidebar.title("🔐 Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Submit button for login
if st.sidebar.button("Submit"):
    if username == "Aslam09" and password == "Shaik09(@)":
        st.session_state.logged_in = True
    else:
        st.sidebar.error("Invalid Username or Password")

# Stop app if not logged in
if not st.session_state.logged_in:
    st.stop()

# ----------- MAIN APP -----------

st.title("🏦 Loan Default Prediction System")
st.markdown("### Predict whether a customer is **High Risk or Low Risk**")

st.markdown("---")

# ----------- INPUT FIELDS -----------

col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", min_value=0)
    enq_l3m = st.number_input("Enquiries (Last 3 Months)", min_value=0)
    pct_pl_enq_l6m_of_ever = st.number_input("PL Enquiry % (Last 6M)", min_value=0.0)
    time_since_recent_enq = st.number_input("Time Since Recent Enquiry", min_value=0)
    age_oldest_tl = st.number_input("Age of Oldest TL", min_value=0)

with col2:
    last_prod_enq2_others = st.number_input("Last Product Enquiry (Others)", min_value=0)
    pl_enq = st.number_input("PL Enquiries", min_value=0)
    num_std = st.number_input("Standard Accounts", min_value=0)
    pct_tl_open_l12m = st.number_input("TL Open % (Last 12M)", min_value=0.0)
    num_std_6mts = st.number_input("Std Accounts (Last 6M)", min_value=0)
    recent_level_of_deliq = st.number_input("Recent Delinquency Level", min_value=0)

st.markdown("---")

# ----------- PREDICT BUTTON -----------

if st.button("🔍 Predict"):

    input_data = pd.DataFrame({
        "credit_score": [credit_score],
        "enq_l3m": [enq_l3m],
        "pct_pl_enq_l6m_of_ever": [pct_pl_enq_l6m_of_ever],
        "time_since_recent_enq": [time_since_recent_enq],
        "age_oldest_tl": [age_oldest_tl],
        "last_prod_enq2_others": [last_prod_enq2_others],
        "pl_enq": [pl_enq],
        "num_std": [num_std],
        "pct_tl_open_l12m": [pct_tl_open_l12m],
        "num_std_6mts": [num_std_6mts],
        "recent_level_of_deliq": [recent_level_of_deliq]
    })

    # Add constant for statsmodels
    input_data = sm.add_constant(input_data)

    # Prediction
    probability = model.predict(input_data)[0]

    threshold = 0.40
    prediction = 1 if probability >= threshold else 0

    # ----------- RESULT -----------

    st.markdown("## 📊 Prediction Result")

    st.write(f"**Probability of Default:** {probability:.2f}")

    if prediction == 1:
        st.error("🔴 High Risk Customer")
    else:
        st.success("🟢 Low Risk Customer")