# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Risk Analysis Dashboard",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("Loan Risk Analysis Dashboard")
st.markdown("Advanced Descriptive & Diagnostic Analytics for Banking Risk")

st.markdown("---")

# ---------------- KPI SECTION ----------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Risk Customers", "25%")
col2.metric("Exposure Ratio", "41%")
col3.metric("Active Customers", "58%")
col4.metric("High Credit Demand", "26%")

st.markdown("---")

# =========================================================
# CREDIT SCORE ANALYSIS
# =========================================================

st.subheader("Risk Distribution by Credit Score Segment")

score_df = pd.DataFrame({
    "Score Bucket": ["Medium_CS", "Low_CS", "High_CS"],
    "Total Customers": [51056, 127, 153],
    "High Risk %": [25.85, 100.00, 4.57]
})

fig1, ax1 = plt.subplots(figsize=(7,4))

ax1.bar(
    score_df["Score Bucket"],
    score_df["High Risk %"]
)

ax1.set_title("High Risk Percentage Across Credit Score Segments")
ax1.set_ylabel("High Risk %")
ax1.set_xlabel("Credit Score Segment")

st.pyplot(fig1)

st.dataframe(score_df)

st.markdown("""
### Business Insight
- Customers with low credit score show extremely high default probability.
- High credit score customers demonstrate very low lending risk.
- Medium credit score customers form the largest exposure segment for the bank.
""")

st.markdown("---")

# =========================================================
# DELINQUENCY ANALYSIS
# =========================================================

st.subheader("Delinquency Behavior vs Risk Level")

delinq_df = pd.DataFrame({
    "Delinquency Bucket": ["High", "Low", "Medium", "No Delinquency"],
    "Total Customers": [4658, 6930, 3799, 35949],
    "Risk %": [33.94, 46.62, 43.24, 19.13]
})

fig2, ax2 = plt.subplots(figsize=(8,4))

# Bar chart
ax2.bar(
    delinq_df["Delinquency Bucket"],
    delinq_df["Total Customers"]
)

# Line chart
ax3 = ax2.twinx()

ax3.plot(
    delinq_df["Delinquency Bucket"],
    delinq_df["Risk %"],
    marker='o'
)

ax2.set_title("Customer Volume & Risk by Delinquency Level")
ax2.set_ylabel("Total Customers")
ax3.set_ylabel("Risk %")

st.pyplot(fig2)

st.dataframe(delinq_df)

st.markdown("""
### Business Insight
- Customers with repeated delinquency history show significantly elevated risk.
- Customers with no delinquency exhibit relatively safer repayment behavior.
- Delinquency acts as a strong early warning indicator for default prediction.
""")

st.markdown("---")

# =========================================================
# ENQUIRY BUCKET ANALYSIS
# =========================================================

st.subheader("Credit Enquiry Behavior Analysis")

enquiry_df = pd.DataFrame({
    "Enquiry Bucket": [
        "High Enquiry",
        "Medium Enquiry",
        "Low Enquiry",
        "No Enquiry"
    ],
    "Risk %": [
        94.38,
        70.68,
        26.63,
        8.88
    ]
})

fig4, ax4 = plt.subplots(figsize=(7,4))

ax4.bar(
    enquiry_df["Enquiry Bucket"],
    enquiry_df["Risk %"]
)

ax4.set_title("Risk Percentage by Credit Enquiry Intensity")
ax4.set_ylabel("Risk %")

st.pyplot(fig4)

st.dataframe(enquiry_df)

st.markdown("""
### Business Insight
- Customers with high enquiry activity exhibit severe credit hunger behavior.
- Increasing enquiry count strongly correlates with rising default probability.
- Low enquiry customers demonstrate financially stable behavior.
""")

st.markdown("---")

# =========================================================
# ENQUIRY TREND ANALYSIS
# =========================================================

st.subheader("Enquiry Count vs Default Risk Trend")

trend_df = pd.DataFrame({
    "Enquiry Count": [0,1,2,3,4,5,6,7,8,9,10],
    "Risk %": [
        8.88,
        20.53,
        46.35,
        64.01,
        75.44,
        85.35,
        91.09,
        91.48,
        94.82,
        97.40,
        100
    ],
    "Total Customers": [
        21116,
        17846,
        5516,
        2865,
        1556,
        799,
        494,
        317,
        232,
        154,
        120
    ]
})

fig5, ax5 = plt.subplots(figsize=(10,5))

# Bar
ax5.bar(
    trend_df["Enquiry Count"],
    trend_df["Total Customers"]
)

# Line
ax6 = ax5.twinx()

ax6.plot(
    trend_df["Enquiry Count"],
    trend_df["Risk %"],
    marker='o'
)

ax5.set_title("Customer Volume & Risk Trend by Enquiry Frequency")
ax5.set_xlabel("Enquiry Count")
ax5.set_ylabel("Total Customers")
ax6.set_ylabel("Risk %")

st.pyplot(fig5)

st.dataframe(trend_df)

st.markdown("""
### Business Insight
- Default probability rises sharply with increasing enquiry frequency.
- Customers with more than 5 enquiries demonstrate extremely high credit risk.
- Enquiry behavior acts as a powerful indicator of financial stress.
""")

st.markdown("---")

# =========================================================
# INTERACTION ANALYSIS
# =========================================================

st.subheader("Interaction Risk Analysis")

interaction_df = pd.DataFrame({
    "Interaction Risk": [
        "Low Risk",
        "Moderate Risk",
        "High Risk"
    ],
    "Default Rate": [
        16,
        24,
        57
    ]
})

fig7, ax7 = plt.subplots(figsize=(6,6))

ax7.pie(
    interaction_df["Default Rate"],
    labels=interaction_df["Interaction Risk"],
    autopct='%1.1f%%'
)

ax7.set_title("Default Distribution Across Interaction Risk Groups")

st.pyplot(fig7)

st.dataframe(interaction_df)

st.markdown("""
### Business Insight
- Customers with combined high enquiry activity and high outstanding balances show severe default tendencies.
- Interaction-based features capture hidden behavioral risk patterns.
""")

st.markdown("---")

# =========================================================
# CORRELATION ANALYSIS
# =========================================================

st.subheader("Top Variables Influencing Default Risk")

corr_df = pd.DataFrame({
    "Variables": [
        "credit_score",
        "enq_l3m",
        "enq_l6m",
        "pct_pl_enq_l6m_of_ever",
        "recent_activity_score",
        "pct_pl_enq_l6m_of_l12m",
        "enq_l12m",
        "pl_enq_l6m",
        "pl_enq_l12m",
        "tot_enq"
    ],
    "Correlation": [
        0.643964,
        0.461950,
        0.422049,
        0.384625,
        0.382085,
        0.378286,
        0.370907,
        0.321441,
        0.283283,
        0.252794
    ]
})

fig8, ax8 = plt.subplots(figsize=(10,5))

ax8.plot(
    corr_df["Variables"],
    corr_df["Correlation"],
    marker='o'
)

ax8.set_title("Top Variables Driving Loan Default Risk")
ax8.set_ylabel("Correlation Strength")
ax8.set_xlabel("Variables")

plt.xticks(rotation=45)

st.pyplot(fig8)

st.dataframe(corr_df)

st.markdown("""
### Business Insight
- Credit score remains the strongest predictor of customer default behavior.
- Recent enquiry activity significantly impacts lending risk.
- Credit-hungry customers demonstrate higher financial instability.
""")