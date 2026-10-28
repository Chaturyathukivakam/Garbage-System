import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import os
import io

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="EcoTrack - Smart Garbage Management System",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Styling
# ---------------------------------------------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #065F46;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .guide-card {
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        color: #1F2937;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Default Embedded Realistic Dataset
# ---------------------------------------------------------
DEFAULT_RECORDS = [
    {"Record_ID": "WM-2026-001", "Date": "2026-01-02", "Zone": "Zone A - North", "Category": "Organic / Compostable", "Weight_Tons": 14.5, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "GreenLeaf Composting Yard", "Cost_USD": 725},
    {"Record_ID": "WM-2026-002", "Date": "2026-01-03", "Zone": "Zone B - South", "Category": "Plastic Waste", "Weight_Tons": 8.2, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Commercial Dumpster", "Disposal_Facility": "Apex Polymer Recyclers", "Cost_USD": 574},
    {"Record_ID": "WM-2026-003", "Date": "2026-01-03", "Zone": "Zone C - East", "Category": "Paper & Cardboard", "Weight_Tons": 6.4, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Drop-off Depot", "Disposal_Facility": "EcoPaper Mills", "Cost_USD": 320},
    {"Record_ID": "WM-2026-004", "Date": "2026-01-04", "Zone": "Zone D - West", "Category": "Hazardous Waste", "Weight_Tons": 1.8, "Recyclable": "No", "Status": "Incinerated", "Collection_Method": "Special Pickup", "Disposal_Facility": "SafetyFirst Bio-Incinerator", "Cost_USD": 450},
    {"Record_ID": "WM-2026-005", "Date": "2026-01-05", "Zone": "Zone E - Central", "Category": "Glass Waste", "Weight_Tons": 4.9, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Street Sweep", "Disposal_Facility": "ClearGlass Processing", "Cost_USD": 245},
    {"Record_ID": "WM-2026-006", "Date": "2026-01-06", "Zone": "Zone A - North", "Category": "E-Waste", "Weight_Tons": 2.3, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Drop-off Depot", "Disposal_Facility": "CircuitCycle Recovery", "Cost_USD": 690},
    {"Record_ID": "WM-2026-007", "Date": "2026-01-07", "Zone": "Zone B - South", "Category": "Organic / Compostable", "Weight_Tons": 16.1, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "GreenLeaf Composting Yard", "Cost_USD": 805},
    {"Record_ID": "WM-2026-008", "Date": "2026-01-08", "Zone": "Zone C - East", "Category": "Metal Scrap", "Weight_Tons": 5.5, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Commercial Dumpster", "Disposal_Facility": "Metro Metal Salvage", "Cost_USD": 385},
    {"Record_ID": "WM-2026-009", "Date": "2026-01-09", "Zone": "Zone D - West", "Category": "Mixed Municipal Solid Waste", "Weight_Tons": 18.7, "Recyclable": "No", "Status": "Landfilled", "Collection_Method": "Door-to-door", "Disposal_Facility": "Valley Sanitary Landfill", "Cost_USD": 1122},
    {"Record_ID": "WM-2026-010", "Date": "2026-01-10", "Zone": "Zone E - Central", "Category": "Plastic Waste", "Weight_Tons": 9.4, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Commercial Dumpster", "Disposal_Facility": "Apex Polymer Recyclers", "Cost_USD": 658},
    {"Record_ID": "WM-2026-011", "Date": "2026-01-11", "Zone": "Zone A - North", "Category": "Paper & Cardboard", "Weight_Tons": 7.1, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "EcoPaper Mills", "Cost_USD": 355},
    {"Record_ID": "WM-2026-012", "Date": "2026-01-12", "Zone": "Zone B - South", "Category": "Hazardous Waste", "Weight_Tons": 2.1, "Recyclable": "No", "Status": "Incinerated", "Collection_Method": "Special Pickup", "Disposal_Facility": "SafetyFirst Bio-Incinerator", "Cost_USD": 525},
    {"Record_ID": "WM-2026-013", "Date": "2026-01-13", "Zone": "Zone C - East", "Category": "Organic / Compostable", "Weight_Tons": 13.8, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "GreenLeaf Composting Yard", "Cost_USD": 690},
    {"Record_ID": "WM-2026-014", "Date": "2026-01-14", "Zone": "Zone D - West", "Category": "Glass Waste", "Weight_Tons": 3.6, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Street Sweep", "Disposal_Facility": "ClearGlass Processing", "Cost_USD": 180},
    {"Record_ID": "WM-2026-015", "Date": "2026-01-15", "Zone": "Zone E - Central", "Category": "E-Waste", "Weight_Tons": 3.0, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Drop-off Depot", "Disposal_Facility": "CircuitCycle Recovery", "Cost_USD": 900},
    {"Record_ID": "WM-2026-016", "Date": "2026-01-16", "Zone": "Zone A - North", "Category": "Plastic Waste", "Weight_Tons": 7.8, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "Apex Polymer Recyclers", "Cost_USD": 546},
    {"Record_ID": "WM-2026-017", "Date": "2026-01-17", "Zone": "Zone B - South", "Category": "Mixed Municipal Solid Waste", "Weight_Tons": 21.3, "Recyclable": "No", "Status": "Landfilled", "Collection_Method": "Door-to-door", "Disposal_Facility": "Valley Sanitary Landfill", "Cost_USD": 1278},
    {"Record_ID": "WM-2026-018", "Date": "2026-01-18", "Zone": "Zone C - East", "Category": "Metal Scrap", "Weight_Tons": 6.2, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Commercial Dumpster", "Disposal_Facility": "Metro Metal Salvage", "Cost_USD": 434},
    {"Record_ID": "WM-2026-019", "Date": "2026-01-19", "Zone": "Zone D - West", "Category": "Organic / Compostable", "Weight_Tons": 15.2, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "GreenLeaf Composting Yard", "Cost_USD": 760},
    {"Record_ID": "WM-2026-020", "Date": "2026-01-20", "Zone": "Zone E - Central", "Category": "Paper & Cardboard", "Weight_Tons": 8.0, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Commercial Dumpster", "Disposal_Facility": "EcoPaper Mills", "Cost_USD": 400},
    {"Record_ID": "WM-2026-021", "Date": "2026-01-21", "Zone": "Zone A - North", "Category": "Hazardous Waste", "Weight_Tons": 1.5, "Recyclable": "No", "Status": "Incinerated", "Collection_Method": "Special Pickup", "Disposal_Facility": "SafetyFirst Bio-Incinerator", "Cost_USD": 375},
    {"Record_ID": "WM-2026-022", "Date": "2026-01-22", "Zone": "Zone B - South", "Category": "Plastic Waste", "Weight_Tons": 8.9, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "Apex Polymer Recyclers", "Cost_USD": 623},
    {"Record_ID": "WM-2026-023", "Date": "2026-01-23", "Zone": "Zone C - East", "Category": "Glass Waste", "Weight_Tons": 4.2, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Street Sweep", "Disposal_Facility": "ClearGlass Processing", "Cost_USD": 210},
    {"Record_ID": "WM-2026-024", "Date": "2026-01-24", "Zone": "Zone D - West", "Category": "Mixed Municipal Solid Waste", "Weight_Tons": 19.5, "Recyclable": "No", "Status": "Landfilled", "Collection_Method": "Door-to-door", "Disposal_Facility": "Valley Sanitary Landfill", "Cost_USD": 1170},
    {"Record_ID": "WM-2026-025", "Date": "2026-01-25", "Zone": "Zone E - Central", "Category": "Organic / Compostable", "Weight_Tons": 17.4, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Commercial Dumpster", "Disposal_Facility": "GreenLeaf Composting Yard", "Cost_USD": 870},
    {"Record_ID": "WM-2026-026", "Date": "2026-01-26", "Zone": "Zone A - North", "Category": "Metal Scrap", "Weight_Tons": 4.8, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "Metro Metal Salvage", "Cost_USD": 336},
    {"Record_ID": "WM-2026-027", "Date": "2026-01-27", "Zone": "Zone B - South", "Category": "E-Waste", "Weight_Tons": 2.7, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Drop-off Depot", "Disposal_Facility": "CircuitCycle Recovery", "Cost_USD": 810},
    {"Record_ID": "WM-2026-028", "Date": "2026-01-28", "Zone": "Zone C - East", "Category": "Plastic Waste", "Weight_Tons": 7.5, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "Apex Polymer Recyclers", "Cost_USD": 525},
    {"Record_ID": "WM-2026-029", "Date": "2026-01-29", "Zone": "Zone D - West", "Category": "Paper & Cardboard", "Weight_Tons": 6.9, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Drop-off Depot", "Disposal_Facility": "EcoPaper Mills", "Cost_USD": 345},
    {"Record_ID": "WM-2026-030", "Date": "2026-01-30", "Zone": "Zone E - Central", "Category": "Hazardous Waste", "Weight_Tons": 2.4, "Recyclable": "No", "Status": "Incinerated", "Collection_Method": "Special Pickup", "Disposal_Facility": "SafetyFirst Bio-Incinerator", "Cost_USD": 600},
    {"Record_ID": "WM-2026-031", "Date": "2026-02-01", "Zone": "Zone A - North", "Category": "Organic / Compostable", "Weight_Tons": 15.8, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Door-to-door", "Disposal_Facility": "GreenLeaf Composting Yard", "Cost_USD": 790},
    {"Record_ID": "WM-2026-032", "Date": "2026-02-02", "Zone": "Zone B - South", "Category": "Glass Waste", "Weight_Tons": 5.1, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Street Sweep", "Disposal_Facility": "ClearGlass Processing", "Cost_USD": 255},
    {"Record_ID": "WM-2026-033", "Date": "2026-02-03", "Zone": "Zone C - East", "Category": "Mixed Municipal Solid Waste", "Weight_Tons": 20.2, "Recyclable": "No", "Status": "Landfilled", "Collection_Method": "Door-to-door", "Disposal_Facility": "Valley Sanitary Landfill", "Cost_USD": 1212},
    {"Record_ID": "WM-2026-034", "Date": "2026-02-04", "Zone": "Zone D - West", "Category": "Metal Scrap", "Weight_Tons": 5.8, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Commercial Dumpster", "Disposal_Facility": "Metro Metal Salvage", "Cost_USD": 406},
    {"Record_ID": "WM-2026-035", "Date": "2026-02-05", "Zone": "Zone E - Central", "Category": "Plastic Waste", "Weight_Tons": 9.1, "Recyclable": "Yes", "Status": "Processed / Recycled", "Collection_Method": "Commercial Dumpster", "Disposal_Facility": "Apex Polymer Recyclers", "Cost_USD": 637}
]

def get_default_data():
    df = pd.DataFrame(DEFAULT_RECORDS)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

if 'waste_df' not in st.session_state:
    st.session_state.waste_df = get_default_data()

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    st.title("♻️ EcoTrack System")
    st.caption("Municipal & Enterprise Waste Intelligence")

    menu = st.radio(
        "Navigation",
        [
            "🏠 Home Dashboard",
            "📊 Waste Data Management",
            "🌱 Environmental Impact",
            "📖 Segregation & Rules Guide",
            "🚀 Deployment Guide"
        ]
    )

    st.markdown("---")
    st.caption("⚙️ **Dataset Quick Controls**")
    if st.button("🔄 Reset to Default Dataset", use_container_width=True):
        st.session_state.waste_df = get_default_data()
        st.success("Reset to default dataset successfully!")

    # Download current dataset template
    csv_buffer = io.StringIO()
    st.session_state.waste_df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="📥 Download Template / Data (CSV)",
        data=csv_buffer.getvalue(),
        file_name="waste_management_records.csv",
        mime="text/csv",
        use_container_width=True
    )

# Reference dataset from session state
df = st.session_state.waste_df.copy()
if not pd.api.types.is_datetime64_any_dtype(df['Date']):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Color palette for charts
ECO_COLORS = ['#10B981', '#3B82F6', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899', '#6B7280']

# ---------------------------------------------------------
# 1. HOME DASHBOARD
# ---------------------------------------------------------
if menu == "🏠 Home Dashboard":
    st.markdown("<div class='main-header'>♻️ Garbage Management & Analytics Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Monitor urban waste generation, recovery metrics, and category trends in real time.</div>", unsafe_allow_html=True)

    # Key Metrics
    total_waste = df['Weight_Tons'].sum()
    recyclable_waste = df[df['Recyclable'].astype(str).str.lower() == 'yes']['Weight_Tons'].sum()
    recycling_rate = (recyclable_waste / total_waste * 100) if total_waste > 0 else 0
    total_cost = df['Cost_USD'].sum() if 'Cost_USD' in df.columns else 0
    top_category = df.groupby('Category')['Weight_Tons'].sum().idxmax() if not df.empty else "N/A"
    active_zones = df['Zone'].nunique()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Waste Collected", value=f"{total_waste:,.1f} Tons", delta=f"{len(df)} logs")
    with col2:
        st.metric(label="Recycling / Diversion Rate", value=f"{recycling_rate:.1f}%", delta="Target: >65%")
    with col3:
        st.metric(label="Total Management Cost", value=f"${total_cost:,.0f}", delta="Operational")
    with col4:
        st.metric(label="Top Waste Category", value=top_category, delta=f"{active_zones} Zones Active")

    st.markdown("---")

    # Visualizations Row 1
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("📦 Waste Generation by Category")
        cat_df = df.groupby('Category')['Weight_Tons'].sum().reset_index()
        fig_donut = px.pie(
            cat_df,
            values='Weight_Tons',
            names='Category',
            hole=0.45,
            color_discrete_sequence=ECO_COLORS
        )
        fig_donut.update_layout(margin=dict(t=10, b=10, l=10, r=10), legend=dict(orientation="h", y=-0.1))
        st.plotly_chart(fig_donut, use_container_width=True)

    with chart_col2:
        st.subheader("📈 Collection Trend Over Time")
        daily_df = df.groupby(df['Date'].dt.date)['Weight_Tons'].sum().reset_index()
        daily_df.rename(columns={'Date': 'Collection Date', 'Weight_Tons': 'Tons Collected'}, inplace=True)
        fig_trend = px.area(
            daily_df,
            x='Collection Date',
            y='Tons Collected',
            markers=True,
            color_discrete_sequence=['#10B981']
        )
        fig_trend.update_layout(margin=dict(t=10, b=10, l=10, r=10))
        st.plotly_chart(fig_trend, use_container_width=True)

    # Visualizations Row 2
    chart_col3, chart_col4 = st.columns(2)

    with chart_col3:
        st.subheader("🏙️ Waste Tonnage by Zone")
        zone_df = df.groupby(['Zone', 'Recyclable'])['Weight_Tons'].sum().reset_index()
        fig_zone = px.bar(
            zone_df,
            x='Zone',
            y='Weight_Tons',
            color='Recyclable',
            barmode='stack',
            color_discrete_map={'Yes': '#10B981', 'No': '#EF4444'},
            labels={'Weight_Tons': 'Weight (Tons)'}
        )
        fig_zone.update_layout(margin=dict(t=10, b=10, l=10, r=10), legend=dict(title="Recyclable"))
        st.plotly_chart(fig_zone, use_container_width=True)

    with chart_col4:
        st.subheader("🏭 Disposal & Facility Status")
        status_df = df.groupby('Status')['Weight_Tons'].sum().reset_index()
        fig_status = px.bar(
            status_df,
            x='Status',
            y='Weight_Tons',
            text_auto=True,
            color='Status',
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_status.update_layout(margin=dict(t=10, b=10, l=10, r=10), showlegend=False)
        st.plotly_chart(fig_status, use_container_width=True)

# ---------------------------------------------------------
# 2. WASTE DATA MANAGEMENT
# ---------------------------------------------------------
elif menu == "📊 Waste Data Management":
    st.markdown("<div class='main-header'>📊 Waste Data Management & Logs</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Upload custom datasets, inspect records, apply multi-criteria filters, and log new collections.</div>", unsafe_allow_html=True)

    # Upload section
    with st.expander("📁 Upload New Dataset (.CSV or .XLSX)", expanded=False):
        uploaded_file = st.file_uploader("Upload a waste collection spreadsheet", type=["csv", "xlsx"])
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith(".csv"):
                    new_df = pd.read_csv(uploaded_file)
                else:
                    new_df = pd.read_excel(uploaded_file)
                
                # Check for critical columns
                if 'Weight_Tons' in new_df.columns:
                    if 'Date' in new_df.columns:
                        new_df['Date'] = pd.to_datetime(new_df['Date'], errors='coerce')
                    st.session_state.waste_df = new_df
                    st.success(f"Successfully loaded '{uploaded_file.name}' with {len(new_df)} records!")
                    st.rerun()
                else:
                    st.error("Uploaded file must contain at least a 'Weight_Tons' column. Please check the template format.")
            except Exception as e:
                st.error(f"Error reading file: {e}")

    # Add new record section
    with st.expander("➕ Log New Waste Collection Entry", expanded=False):
        with st.form("new_entry_form", clear_on_submit=True):
            f_col1, f_col2, f_col3 = st.columns(3)
            with f_col1:
                entry_id = st.text_input("Record ID", value=f"WM-2026-{len(df)+1:03d}")
                entry_date = st.date_input("Collection Date", value=date.today())
                entry_zone = st.selectbox("Zone / Area", sorted(list(df['Zone'].unique()) if 'Zone' in df.columns else ["Zone A - North", "Zone B - South", "Zone C - East"]))
            with f_col2:
                entry_category = st.selectbox("Category", sorted(list(df['Category'].unique()) if 'Category' in df.columns else ["Organic / Compostable", "Plastic Waste", "Paper & Cardboard", "Hazardous Waste", "E-Waste"]))
                entry_weight = st.number_input("Weight (Tons)", min_value=0.1, max_value=500.0, value=5.0, step=0.1)
                entry_recyclable = st.selectbox("Recyclable?", ["Yes", "No"])
            with f_col3:
                entry_status = st.selectbox("Status", ["Processed / Recycled", "Landfilled", "Incinerated", "In-Transit"])
                entry_method = st.selectbox("Collection Method", ["Door-to-door", "Commercial Dumpster", "Drop-off Depot", "Street Sweep", "Special Pickup"])
                entry_cost = st.number_input("Estimated Cost ($)", min_value=0, max_value=10000, value=250, step=10)

            submitted = st.form_submit_button("💾 Save Collection Entry", use_container_width=True)
            if submitted:
                new_row = {
                    "Record_ID": entry_id,
                    "Date": pd.to_datetime(entry_date),
                    "Zone": entry_zone,
                    "Category": entry_category,
                    "Weight_Tons": entry_weight,
                    "Recyclable": entry_recyclable,
                    "Status": entry_status,
                    "Collection_Method": entry_method,
                    "Disposal_Facility": "Designated Hub",
                    "Cost_USD": entry_cost
                }
                st.session_state.waste_df = pd.concat([st.session_state.waste_df, pd.DataFrame([new_row])], ignore_index=True)
                st.success("New waste collection record appended successfully!")
                st.rerun()

    st.markdown("### 🔍 Filter and Explore Records")
    
    # Filter Controls
    filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)
    
    with filter_col1:
        zones_list = ["All Zones"] + sorted(list(df['Zone'].dropna().unique())) if 'Zone' in df.columns else ["All Zones"]
        selected_zone = st.selectbox("Filter by Zone", zones_list)

    with filter_col2:
        categories_list = ["All Categories"] + sorted(list(df['Category'].dropna().unique())) if 'Category' in df.columns else ["All Categories"]
        selected_cat = st.selectbox("Filter by Category", categories_list)

    with filter_col3:
        recyclable_opts = ["All", "Yes", "No"]
        selected_recyc = st.selectbox("Recyclable Only", recyclable_opts)

    with filter_col4:
        min_date = df['Date'].min().date() if pd.notnull(df['Date'].min()) else date(2026, 1, 1)
        max_date = df['Date'].max().date() if pd.notnull(df['Date'].max()) else date(2026, 12, 31)
        date_range = st.date_input("Date Range", value=(min_date, max_date))

    # Apply filters
    filtered_df = df.copy()
    if selected_zone != "All Zones" and 'Zone' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Zone'] == selected_zone]
    if selected_cat != "All Categories" and 'Category' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Category'] == selected_cat]
    if selected_recyc != "All" and 'Recyclable' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Recyclable'].astype(str).str.lower() == selected_recyc.lower()]
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_d, end_d = date_range
        filtered_df = filtered_df[(filtered_df['Date'].dt.date >= start_d) & (filtered_df['Date'].dt.date <= end_d)]

    # Display stats of filtered results
    st.info(f"Showing **{len(filtered_df)}** of **{len(df)}** records | Total Weight: **{filtered_df['Weight_Tons'].sum():,.2f} Tons**")

    # Data Table
    st.dataframe(
        filtered_df.sort_values(by="Date", ascending=False),
        use_container_width=True,
        hide_index=True
    )

    # Download filtered CSV
    filt_csv = io.StringIO()
    filtered_df.to_csv(filt_csv, index=False)
    st.download_button(
        label="📥 Export Filtered Table as CSV",
        data=filt_csv.getvalue(),
        file_name="filtered_waste_data.csv",
        mime="text/csv"
    )

# ---------------------------------------------------------
# 3. ENVIRONMENTAL IMPACT ANALYTICS
# ---------------------------------------------------------
elif menu == "🌱 Environmental Impact":
    st.markdown("<div class='main-header'>🌱 Environmental Impact & Carbon Calculator</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Estimated greenhouse gas emission reductions and resource conservation achieved through recycling.</div>", unsafe_allow_html=True)

    recycled_tons = df[df['Recyclable'].astype(str).str.lower() == 'yes']['Weight_Tons'].sum()
    organic_tons = df[df['Category'].str.contains('Organic', case=False, na=False)]['Weight_Tons'].sum()
    paper_tons = df[df['Category'].str.contains('Paper', case=False, na=False)]['Weight_Tons'].sum()
    plastic_tons = df[df['Category'].str.contains('Plastic', case=False, na=False)]['Weight_Tons'].sum()

    # Environmental coefficients (industry averages per ton recycled)
    co2_saved = recycled_tons * 1.54 # ~1.54 metric tons CO2e avoided per ton recycled
    trees_saved = int(paper_tons * 17) # ~17 trees saved per ton of paper recycled
    energy_saved_kwh = (plastic_tons * 5774) + (paper_tons * 4100) # kWh
    landfill_m3_saved = recycled_tons * 2.3 # cubic meters

    ec1, ec2, ec3, ec4 = st.columns(4)
    with ec1:
        st.markdown(f"""
        <div class='metric-card'>
            <h4 style='color:#065F46;margin:0;'>☁️ CO2e Avoided</h4>
            <h2 style='color:#047857;margin:0.2rem 0;'>{co2_saved:,.1f} MT</h2>
            <small style='color:#6B7280;'>Equivalent to {int(co2_saved * 2.5)} cars off the road for a month</small>
        </div>
        """, unsafe_allow_html=True)

    with ec2:
        st.markdown(f"""
        <div class='metric-card'>
            <h4 style='color:#065F46;margin:0;'>🌲 Trees Preserved</h4>
            <h2 style='color:#047857;margin:0.2rem 0;'>{trees_saved:,} Trees</h2>
            <small style='color:#6B7280;'>Through {paper_tons:.1f} tons of recycled paper</small>
        </div>
        """, unsafe_allow_html=True)

    with ec3:
        st.markdown(f"""
        <div class='metric-card'>
            <h4 style='color:#065F46;margin:0;'>⚡ Energy Conserved</h4>
            <h2 style='color:#047857;margin:0.2rem 0;'>{energy_saved_kwh:,.0f} kWh</h2>
            <small style='color:#6B7280;'>Powers ~{int(energy_saved_kwh/900)} households for a month</small>
        </div>
        """, unsafe_allow_html=True)

    with ec4:
        st.markdown(f"""
        <div class='metric-card'>
            <h4 style='color:#065F46;margin:0;'>🏞️ Landfill Space Saved</h4>
            <h2 style='color:#047857;margin:0.2rem 0;'>{landfill_m3_saved:,.1f} m³</h2>
            <small style='color:#6B7280;'>Diverted from city landfills</small>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("💡 Eco Diversion Performance Gauge")
    
    total_waste = df['Weight_Tons'].sum()
    rate = (recycled_tons / total_waste * 100) if total_waste > 0 else 0

    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = rate,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Diversion & Recycling Rate (%)", 'font': {'size': 20}},
        delta = {'reference': 60.0, 'increasing': {'color': "green"}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#10B981"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#D1D5DB",
            'steps': [
                {'range': [0, 40], 'color': '#FEE2E2'},
                {'range': [40, 70], 'color': '#FEF3C7'},
                {'range': [70, 100], 'color': '#D1FAE5'}
            ],
            'threshold': {
                'line': {'color': "green", 'width': 4},
                'thickness': 0.75,
                'value': 75.0
            }
        }
    ))
    fig_gauge.update_layout(height=350, margin=dict(t=30, b=10, l=20, r=20))
    st.plotly_chart(fig_gauge, use_container_width=True)

# ---------------------------------------------------------
# 4. SEGREGATION & RULES GUIDE
# ---------------------------------------------------------
elif menu == "📖 Segregation & Rules Guide":
    st.markdown("<div class='main-header'>📖 Waste Segregation & Classification Guide</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Standard operating procedures and color-coded segregation guidelines for municipal waste.</div>", unsafe_allow_html=True)

    g1, g2 = st.columns(2)
    with g1:
        st.markdown("""
        <div class='guide-card' style='background-color: #ECFDF5; border-left: 6px solid #10B981;'>
            <h3 style='color:#065F46; margin-top:0;'>🟢 Organic & Wet Waste (Green Bin)</h3>
            <ul>
                <li><b>Items included:</b> Vegetable & fruit peels, leftover cooked food, egg shells, coffee grounds, garden clippings, dried leaves.</li>
                <li><b>Disposal destination:</b> Aerobic composting facility or biomethanation plant.</li>
                <li><b>Best Practice:</b> Never mix plastic liners or cutlery into wet bins.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='guide-card' style='background-color: #EFF6FF; border-left: 6px solid #3B82F6;'>
            <h3 style='color:#1E40AF; margin-top:0;'>🔵 Dry Recyclables (Blue Bin)</h3>
            <ul>
                <li><b>Items included:</b> Cardboard boxes, office paper, clean PET plastic bottles, HDPE containers, beverage cans, aluminum foil, glass bottles.</li>
                <li><b>Disposal destination:</b> Materials Recovery Facility (MRF) for sorting and mechanical recycling.</li>
                <li><b>Best Practice:</b> Rinse containers to remove residual milk, oil, or food before disposal.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with g2:
        st.markdown("""
        <div class='guide-card' style='background-color: #FEF2F2; border-left: 6px solid #EF4444;'>
            <h3 style='color:#991B1B; margin-top:0;'>🔴 Domestic Hazardous Waste (Red Bin)</h3>
            <ul>
                <li><b>Items included:</b> Expired medications, insecticides, paint cans, solvent tins, aerosol sprays, batteries, broken fluorescent tubes.</li>
                <li><b>Disposal destination:</b> High-temperature bio-incineration & secure hazardous landfilling.</li>
                <li><b>Best Practice:</b> Keep hazardous containers tightly closed in original labeled containers.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='guide-card' style='background-color: #FAF5FF; border-left: 6px solid #8B5CF6;'>
            <h3 style='color:#6B21A8; margin-top:0;'>🟣 Electronic Waste / E-Waste (Special Drop-off)</h3>
            <ul>
                <li><b>Items included:</b> Mobile phones, chargers, laptops, circuit boards, cables, defective home appliances.</li>
                <li><b>Disposal destination:</b> Authorized e-waste dismantling and precious metal recovery centers.</li>
                <li><b>Best Practice:</b> Hand over directly to certified e-waste drives; never hand to uncertified scrap dealers.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. DEPLOYMENT GUIDE (STREAMLIT COMMUNITY CLOUD)
# ---------------------------------------------------------
elif menu == "🚀 Deployment Guide":
    st.markdown("<div class='main-header'>🚀 How to Deploy to Streamlit Community Cloud</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Step-by-step instructions for beginners to deploy this app publicly with a live URL.</div>", unsafe_allow_html=True)

    st.markdown("""
    ### 3 Simple Steps to Deploy:
    
    #### Step 1: Create a GitHub Repository
    1. Go to [github.com](https://github.com) and log in.
    2. Click **New Repository** (e.g. named `garbage-management-system`).
    3. Choose **Public** and click **Create repository**.
    4. Upload or push the files from this `garbage_management_system` folder:
       - `app.py`
       - `requirements.txt`

    #### Step 2: Sign in to Streamlit Community Cloud
    1. Visit [share.streamlit.io](https://share.streamlit.io).
    2. Click **Continue with GitHub** to connect your account.

    #### Step 3: Deploy the App
    1. Click the **"New app"** button.
    2. Select your repository: `<your-username>/Garbage-System`.
    3. Branch: `main` (or `master`).
    4. Main file path: `app.py`.
    5. Click **"Deploy!"** 🚀

    Within 1–2 minutes, your app will be live with a public URL!
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #9CA3AF; font-size: 0.85rem;'>"
    "EcoTrack Garbage Management System • Built with Python, Streamlit, Pandas & Plotly • Ready for Streamlit Cloud"
    "</div>",
    unsafe_allow_html=True
)
