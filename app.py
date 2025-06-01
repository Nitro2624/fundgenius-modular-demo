
import streamlit as st
from modules.recommender import recommend_funds, get_fund_mix
from modules.amfi_data import get_latest_navs
from modules.manager_notes import get_fund_manager_notes

st.set_page_config(page_title="FundGenius - SBI MF Assistant", layout="wide")

st.title("FundGenius - AI Mutual Fund Assistant (Internal)")
st.caption("For SBI Mutual Fund Employee Use Only")

# Sidebar info
st.sidebar.title("Client Input")
age = st.sidebar.slider("Client Age", 18, 80, 30)
risk = st.sidebar.selectbox("Risk Profile", ["Low", "Moderate", "High"])
goal = st.sidebar.selectbox("Investment Goal", ["Retirement", "Wealth Creation", "Education", "Tax Saving", "General Investment"])
duration = st.sidebar.slider("Investment Duration (Years)", 1, 30, 5)
amount = st.sidebar.number_input("Investment Amount (INR)", 1000, 10000000, 100000)
# Button and Result
if st.button("\U0001F50D Get Fund Recommendations"):
    category = recommend_funds(risk, duration)
    st.subheader(f"Recommended Fund Category: {category}")
    st.success("Suggested Funds:")

# Fund recommendation
st.header("Fund Recommendation")
category, suggested_funds = recommend_funds(risk, duration)
st.success(f"Recommended Category: {category,category,category}")
st.write("Suggested Funds:")
for fund in suggested_funds:
    st.markdown(f"- {fund}")

# Fund mix suggestion
st.header("Suggested Fund Mix")
mix = get_fund_mix(suggested_funds, amount)
st.write("Investment Allocation:")
for item in mix:
    st.markdown(f"- ₹{item['amount']:,} → **{item['fund']}**")

# Fund manager notes
st.header("Fund Manager Insights")
notes = get_fund_manager_notes()
for line in notes:
    st.info(f"🔹 {line}")

# Live NAVs
st.header("SBI Mutual Fund NAVs (Demo Data)")
navs = get_latest_navs()
st.dataframe(navs, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Developed by Nitro2624 | Internal Use Only")
