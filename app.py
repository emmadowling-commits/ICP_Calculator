import streamlit as st

# Set up the page formatting
st.set_page_config(page_title="AS Ideal Customer Profile", layout="centered")

st.title("Autonomous Sourcing: ICP Engine")
st.markdown("### Evaluate and Qualify the Ideal Customer Profile")
st.write("Use this tool to determine if a prospect fits the Autonomous Sourcing ICP based on spend density and market volatility.")
st.divider()

# --- INPUT SECTION ---
st.header("1. Prospect Profile")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Company Name", "e.g., Tirlán or Musgrave")
    industry = st.selectbox("Business Model", ["Make (Manufacturing/Agri)", "Move (Logistics/Retail)", "Services/Other"])

with col2:
    turnover = st.number_input("Annual Turnover ($ Billions)", min_value=0.1, value=2.5, step=0.5)
    volatility = st.radio("Market Volatility", ["Low (Stable)", "Medium", "High (Rapidly changing prices)"])

st.divider()

# --- LOGIC & CALCULATION SECTION ---
# 1. Determine Direct Spend % based on the 'Make or Move' rule
if "Make" in industry or "Move" in industry:
    spend_pct = 0.60  # 60% of turnover goes to direct materials/freight
else:
    spend_pct = 0.20  # 20% for services

# 2. Determine the AS Efficiency Gain based on volatility
if "High" in volatility:
    gain_pct = 0.05  # 5% savings because AI beats humans in chaotic markets
elif "Medium" in volatility:
    gain_pct = 0.03  # 3% standard savings
else:
    gain_pct = 0.015 # 1.5% savings in highly stable/fixed markets

# 3. Calculate EBITDA Lift (Math: Turnover in Billions * 1000 to get Millions)
ebitda_lift = (turnover * 1000) * spend_pct * gain_pct 

# --- RESULTS SECTION ---
st.header("2. ICP Qualification Result")

# Display the massive dollar amount
st.metric(label=f"Estimated Annual EBITDA Lift for {name}", value=f"${ebitda_lift:,.1f} Million")

# Dynamic Kearney-style insights based on the result
if ebitda_lift >= 40:
    st.success("**🔥 EXACT ICP MATCH (Tier 1):** This prospect is a perfect fit. Their spend density and volatility mean Autonomous Sourcing will deliver massive, immediate ROI.")
elif ebitda_lift >= 15:
    st.warning("**⚡ STRATEGIC ICP FIT (Tier 2):** Strong value potential. They may have a smaller turnover, but their 'Make/Move' complexity justifies an AS pilot.")
else:
    st.error("**💤 OUTSIDE ICP:** Spend scale or market stability does not currently justify a full-scale Autonomous Sourcing implementation.")