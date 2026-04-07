import streamlit as st

# Set up the page formatting
st.set_page_config(page_title="AS ICP Engine", layout="wide")

# --- SIDEBAR: KEARNEY ASSUMPTIONS ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Kearney_logo.svg/512px-Kearney_logo.svg.png", width=150)
st.sidebar.header("Project Assumptions")
st.sidebar.write("Adjust internal variables here.")
pilot_cost = st.sidebar.slider("Est. Pilot Cost ($M)", min_value=0.2, max_value=1.5, value=0.5, step=0.1)
st.sidebar.divider()
st.sidebar.info("This engine uses a standard value-tree to filter top-line turnover down to addressable spend.")

# --- HEADER ---
st.title("Autonomous Sourcing: ICP Engine")
st.markdown("Evaluate prospect fit and generate a defensible, ROI-driven business case for an AS Pilot.")
st.divider()

# --- INPUT SECTION (Global) ---
st.header("1. Prospect Profile")
col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Company Name", "e.g., Tirlán or Musgrave")
    turnover = st.number_input("Annual Turnover ($ Billions)", min_value=0.1, value=2.5, step=0.5)

with col2:
    industry = st.selectbox("Business Model", ["Make (Manufacturing/Agri)", "Move (Logistics/Retail)", "Services/Other"])
    volatility = st.radio("Market Volatility", ["Low (Stable)", "Medium", "High (Rapid price changes)"])

with col3:
    maturity = st.selectbox("Current Sourcing Tech", ["Manual (Excel/Emails)", "Basic e-Sourcing Tools", "Advanced ERP/Digital"])

# --- CORE MATH LOGIC ---
# 1. Direct Spend % 
spend_pct = 0.60 if "Make" in industry or "Move" in industry else 0.20

# 2. Base AS Efficiency Gain 
if "High" in volatility:
    base_gain = 0.05
elif "Medium" in volatility:
    base_gain = 0.03
else:
    base_gain = 0.015

# 3. Maturity Multiplier 
if "Manual" in maturity:
    gain_pct = base_gain * 1.2
elif "Basic" in maturity:
    gain_pct = base_gain * 1.0
else:
    gain_pct = base_gain * 0.8

# 4. Final Math Calculations
addressable_spend = (turnover * 1000) * spend_pct
projected_savings = addressable_spend * gain_pct 
roi_multiplier = projected_savings / pilot_cost

st.divider()

# --- TABS SECTION ---
st.header("2. Engine Outputs")
tab1, tab2 = st.tabs(["📊 Executive Business Case", "🧠 Logic & Calculations"])

# --- TAB 1: The Executive View ---
with tab1:
    st.subheader(f"Projected Return Profile for {name}")
    
    # Display the core metrics
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    metric_col1.metric(label="Addressable Spend", value=f"${addressable_spend:,.0f}M")
    metric_col2.metric(label="Projected Savings", value=f"${projected_savings:,.1f}M")
    metric_col3.metric(label="Projected ROI", value=f"{roi_multiplier:,.0f}x")

    # Dynamic Insights (Fixed to use projected_savings)
    st.write("")
    if projected_savings >= 40:
        st.success(f"**🔥 EXACT ICP MATCH (Tier 1):** Moving from {maturity} to Autonomous Sourcing will yield game-changing EBITDA expansion. Recommend pitching an immediate 8-12 week Pilot.")
    elif projected_savings >= 15:
        st.warning(f"**⚡ STRATEGIC ICP FIT (Tier 2):** Strong value. Addressing their {maturity} processes with an AS pilot will yield a highly defensible return on investment.")
    else:
        st.error("**💤 OUTSIDE ICP:** Spend scale or market stability does not currently justify a full AS implementation. Pivot to strategic sourcing advisory.")

# --- TAB 2: The Consultant View (The Math) ---
with tab2:
    st.subheader("Value Tree Breakdown")
    st.markdown("This tab details the exact mathematical logic used to calculate the ROI based on the inputs selected above. It acts as a defensible baseline for client conversations.")
    
    st.write("---")
    st.markdown("### Step 1: Calculate Addressable Spend")
    st.write("We do not target 100% of turnover. We isolate the 'Make or Move' COGS (Cost of Goods Sold).")
    st.code(f"Total Turnover (${turnover}B) * Industry Spend Intensity ({spend_pct*100}%) = ${addressable_spend:,.0f}M Addressable Spend")
    
    st.write("---")
    st.markdown("### Step 2: Determine AI Efficiency Gain")
    st.write("We establish a base savings % based on market volatility, then adjust it based on the whitespace left by their current tech stack.")
    st.code(f"Base Volatility Gain ({base_gain*100}%) * Tech Maturity Multiplier ({gain_pct/base_gain:.1f}x) = {gain_pct*100:.1f}% Total Efficiency Gain")
    
    st.write("---")
    st.markdown("### Step 3: Projected Savings")
    st.write("Applying the total efficiency gain to the addressable spend to find the absolute dollar value generated.")
    st.code(f"Addressable Spend (${addressable_spend:,.0f}M) * Total Efficiency Gain ({gain_pct*100:.1f}%) = ${projected_savings:,.1f}M Projected Savings")
    
    st.write("---")
    st.markdown("### Step 4: ROI Calculation")
    st.write("Comparing the total projected savings against the estimated investment required for a Kearney Autonomous Sourcing Pilot.")
    st.code(f"Projected Savings (${projected_savings:,.1f}M) / Estimated Pilot Cost (${pilot_cost}M) = {roi_multiplier:,.0f}x ROI")
