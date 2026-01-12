import streamlit as st
import pandas as pd
import plotly.express as px

import base64

def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()
logo_base64 = load_image_base64("assets/logo.png")


# PAGE CONFIG

st.set_page_config(
    page_title="Healthcare Infrastructure in India",
    layout="wide"
)


# LOAD CSS

def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("styles/style.css")



# HEADER

st.markdown(
    f"""
    <div class="sticky-header">
        <div class="header-container">
            <img src="data:image/png;base64,{logo_base64}" class="header-logo">
            <h1>
                Healthcare Infrastructure vs Population in India
                <span class="badge">India Dashboard</span>
            </h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# PROBLEM OVERVIEW

st.subheader("📌 Problem Overview")

st.write(
    """
    During the COVID-19 pandemic, the shortage of hospital beds and healthcare facilities
    exposed critical gaps in India's healthcare infrastructure.

    This dashboard analyzes population and healthcare data to evaluate per-capita
    healthcare availability across states and identify regions that may require
    urgent policy attention.
    """
)

# LOAD DATA

@st.cache_data
def load_data():
    return pd.read_excel(
        "data/processed/merged_population_healthcare.xlsx",
        sheet_name="population_india_census2011"
    )


df = load_data()


# SIDEBAR FILTERS

st.sidebar.header("🔎 Filters")

state_category = st.sidebar.selectbox(
    "State Category",
    ["All", "Large Population State", "Low Population State / UT"]
)

region = st.sidebar.selectbox(
    "Region",
    ["All", "North", "South", "East", "West", "Central", "North-East", "UT"]
)

adequacy = st.sidebar.selectbox(
    "Healthcare Adequacy Level",
    ["All", "Low", "Medium", "High"]
)



# FILTER LOGIC

filtered_df = df.copy()

if state_category != "All":
    filtered_df = filtered_df[filtered_df["State Category"] == state_category]

if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]

if adequacy != "All":
    filtered_df = filtered_df[filtered_df["Healthcare Adequacy Level"] == adequacy]



# DATA CLEANING

numeric_columns = [
    "Population",
    "DISTRICT HOSPITAL",
    "SUB DISTRICT/ SUB DIVISIONAL HOSPITAL",
    "Beds per 1 Lakh Population"
]

for col in numeric_columns:
    filtered_df[col] = pd.to_numeric(filtered_df[col], errors="coerce")


# KPI CALCULATIONS

total_population = filtered_df["Population"].sum()

total_hospitals = (
    filtered_df["DISTRICT HOSPITAL"].sum()
    + filtered_df["SUB DISTRICT/ SUB DIVISIONAL HOSPITAL"].sum()
)

avg_beds_per_lakh = filtered_df["Beds per 1 Lakh Population"].mean()

underserved_states = filtered_df[
    filtered_df["Underserved Status"] == "Yes"
].shape[0]


# KPI DISPLAY

st.markdown("## Key Healthcare Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Population", f"{int(total_population):,}")
col2.metric("Total Hospitals", f"{int(total_hospitals):,}")
col3.metric("Avg Beds / 1 Lakh", f"{avg_beds_per_lakh:.2f}")
col4.metric("Underserved States", underserved_states)



# MAP + CHART LAYOUT

st.markdown("## 📌 Key Healthcare Indicators")


left_col, right_col = st.columns([1.2, 1])



# INDIA MAP 

with left_col:
    st.markdown(
        """
        <div class="card map-card">
        <h3>🇮🇳 India Map: Beds per 1 Lakh Population</h3>
        """,
        unsafe_allow_html=True
    )

    map_df = filtered_df.copy()

    map_df["hover_text"] = (
        "State: " + map_df["State /UT"] +
        "<br>Beds per 1 Lakh: " + map_df["Beds per 1 Lakh Population"].round(1).astype(str) +
        "<br>Adequacy Level: " + map_df["Healthcare Adequacy Level"] +
        "<br>Beds Rank: " + map_df["Beds per Lakh Rank"].astype(str)
    )

    fig_map = px.choropleth(
        map_df,
        geojson="https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson",
        featureidkey="properties.NAME_1",
        locations="State /UT",
        color="Beds per 1 Lakh Population",
        color_continuous_scale=["#e63946", "#f4a261", "#457b9d"],
        hover_name="State /UT",
        hover_data={"hover_text": True},
    )

    fig_map.update_traces(hovertemplate="%{customdata[0]}")

    fig_map.update_geos(
        fitbounds="locations",
        visible=True,
        showcountries=False,
        showcoastlines=False,
        center={"lat": 22.9734, "lon": 78.6569}
    )

    fig_map.update_layout(
        height=550,
        dragmode=False,
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True,
        config={"scrollZoom": False, "displayModeBar": True}
    )

    st.markdown("</div>", unsafe_allow_html=True)



# RIGHT SIDE CHARTS

with right_col:

    st.markdown("### 🛏️ Beds per 1 Lakh vs State")

    bar_df = filtered_df.sort_values(
        by="Beds per 1 Lakh Population",
        ascending=False
    )

    st.bar_chart(
        bar_df.set_index("State /UT")["Beds per 1 Lakh Population"],
        height=220
    )

    st.markdown("### 🥧 Healthcare Adequacy Distribution")

    adequacy_counts = (
        filtered_df["Healthcare Adequacy Level"]
        .value_counts()
        .reset_index()
    )
    adequacy_counts.columns = ["Healthcare Adequacy Level", "Count"]

    fig_pie = px.pie(
        adequacy_counts,
        names="Healthcare Adequacy Level",
        values="Count",
        color="Healthcare Adequacy Level",
        color_discrete_map={
            "Low": "#e63946",
            "Medium": "#f4a261",
            "High": "#457b9d"
        },
        height=240
    )

    fig_pie.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
        legend_title_text="Adequacy Level"
    )

    st.plotly_chart(fig_pie, use_container_width=True)



# BEST vs WORST STATES 

st.markdown("## 📌 Best & Worst Performing States")

clean_df = filtered_df.dropna(
    subset=["Beds per 1 Lakh Population"]
)

# Sort by Beds per Lakh
sorted_states = clean_df.sort_values(
    by="Beds per 1 Lakh Population",
    ascending=False
)

top_states = sorted_states[
    ["State /UT", "Beds per 1 Lakh Population"]
].head(5)

bottom_states = sorted_states[
    ["State /UT", "Beds per 1 Lakh Population"]
].tail(5)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟢 Best Performing States")
    st.dataframe(top_states, use_container_width=True)

with col2:
    st.markdown("### 🔴 Most Underserved States")
    st.dataframe(bottom_states, use_container_width=True)


st.markdown("## 📌 Regional & Infrastructure Analysis")

left_col, right_col = st.columns(2)

with left_col:
    st.markdown("### 🌍 Region-wise Healthcare Comparison")

    region_summary = (
        filtered_df
        .dropna(subset=["Beds per 1 Lakh Population"])
        .groupby("Region")["Beds per 1 Lakh Population"]
        .mean()
        .reset_index()
    )

    st.bar_chart(
        region_summary.set_index("Region"),
        height=300
    )

with right_col:
    st.markdown("### 📉 Infrastructure Gap (Benchmark = 100)")

    benchmark = 100

    gap_df = filtered_df.dropna(
        subset=["Beds per 1 Lakh Population"]
    ).copy()

    gap_df["Infrastructure Gap"] = benchmark - gap_df["Beds per 1 Lakh Population"]

    gap_df = gap_df.sort_values(
        by="Infrastructure Gap",
        ascending=False
    )

    gap_display = gap_df[
        ["State /UT", "Beds per 1 Lakh Population", "Infrastructure Gap"]
    ].head(8)

    st.dataframe(gap_display, use_container_width=True)




# AI-STYLE INSIGHTS 

st.markdown("## 🧠 Automated Insights")

insight_df = filtered_df.dropna(subset=["Beds per 1 Lakh Population"])

low_bed_states = insight_df[
    insight_df["Beds per 1 Lakh Population"] < 50
]["State /UT"].tolist()

medium_bed_states = insight_df[
    (insight_df["Beds per 1 Lakh Population"] >= 50) &
    (insight_df["Beds per 1 Lakh Population"] < 100)
]["State /UT"].tolist()

high_bed_states = insight_df[
    insight_df["Beds per 1 Lakh Population"] >= 100
]["State /UT"].tolist()


# 🔴 Low Capacity Insight
if len(low_bed_states) > 0:
    st.warning(
        f"⚠️ **Critical Capacity Alert**: {len(low_bed_states)} states have "
        f"**very low healthcare availability** (below 50 beds per 1 lakh population). "
        f"These states require **urgent infrastructure expansion**.\n\n"
        f"**Examples:** {', '.join(low_bed_states[:3])}"
    )

# 🟡 Medium Capacity Insight
if len(medium_bed_states) > 0:
    st.info(
        f"ℹ️ **Moderate Capacity States**: {len(medium_bed_states)} states fall within "
        f"the **50–100 beds per 1 lakh** range. While not critical, these states "
        f"would benefit from **incremental healthcare investments**."
    )

# 🟢 High Capacity Insight
if len(high_bed_states) > 0:
    st.success(
        f"✅ **Strong Performers**: {len(high_bed_states)} states demonstrate "
        f"**robust healthcare infrastructure** (100+ beds per 1 lakh population). "
        f"These states can serve as **benchmarks for best practices**.\n\n"
        f"**Examples:** {', '.join(high_bed_states[:3])}"
    )




# POLICY RECOMMENDATION 

st.markdown("## 🏛️ Policy Recommendations")

st.info(
    "📌 **Key Recommendations based on the analysis:**\n\n"
    "• **Prioritize underserved states** for rapid expansion of hospital beds and facilities\n"
    "• **Strengthen district and sub-district healthcare** to reduce regional imbalance\n"
    "• **Allocate funding proportionally** based on population pressure and infrastructure gap\n"
    "• **Adopt best practices** from high-performing states to improve efficiency\n\n"
    "📊 This dashboard demonstrates how **data-driven insights** can support "
    "**equitable and evidence-based healthcare planning** across India."
)