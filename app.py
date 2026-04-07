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

# --- TAXONOMY LIST (Updated with all categories) ---
SPEND_CATEGORIES = [
    "Construction",
    "Financial Services",
    "Fleet & Vehicles",
    "Goods",
    "Human Resources (HR)",
    "Information Technology (IT)",
    "Information Technology (IT) > Cloud Services",
    "Information Technology (IT) > Hardware",
    "Information Technology (IT) > IT Consulting",
    "Information Technology (IT) > IT Support & Maintenance",
    "Logistics",
    "Logistics > Air",
    "Logistics > Ocean",
    "Logistics > Ocean > Full Container Load (FCL)",
    "Logistics > Ocean > Less than Container Load (LCL)",
    "Logistics > Parcel",
    "Logistics > Warehousing",
    "Marketing",
    "Marketing > Creative Agencies",
    "Marketing > Digital Marketing",
    "Marketing > Events & Sponsorships",
    "Materials",
    "Materials > Chemicals",
    "Materials > Electronic Components",
    "Materials > Metals",
    "Materials > Other Direct",
    "Materials > Other Indirect",
    "Materials > Other Raw",
    "Materials > Plastics",
    "Materials > Textiles",
    "Real Estate & Facilities > Heating, Ventilation and Air Conditioning (HVAC)",
    "Real Estate & Facilities > Janitorial Services",
    "Real Estate & Facilities > Landscaping",
    "Real Estate & Facilities > Leasing & Rental",
    "Real Estate & Facilities > Security Services",
    "Utilities"
]

# --- INPUT SECTION (Global) ---
st.header("1. Prospect Profile")
col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Company Name", "e.g., Tirlán or Musgrave")
    turnover = st.number_input("Annual Turnover ($ Billions)", min_value=0.1, value=2.5, step=0.5)

with col2:
    # The selectbox naturally allows users to type to search/filter the list
    industry = st.selectbox("Primary Spend Category (Click & Type to Search)", SPEND_CATEGORIES)
    volatility =
