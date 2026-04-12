"""
app.py - Streamlit Web App
EV Range Estimation & Energy Consumption Analyzer
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="EV Range Analyzer", page_icon="⚡", layout="wide")

st.title("⚡ EV Range Estimation & Energy Consumption Analyzer")
st.markdown("---")

# ---------- SIDEBAR INPUTS ----------
st.sidebar.header("🔧 Configuration")

battery_capacity = st.sidebar.number_input(
    "Battery Capacity (kWh)", min_value=10.0, max_value=150.0, value=40.0, step=1.0
)

soc_percent = st.sidebar.slider(
    "State of Charge - SOC (%)", min_value=10, max_value=100, value=80, step=5
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Project by:**")
st.sidebar.markdown("Prajwal P Kaboji")
st.sidebar.markdown("Sameeksha R Kava")
st.sidebar.markdown("Sharadhi B Aithal")
st.sidebar.markdown("Srushti Paramashetti")
st.sidebar.markdown("Tejasvi D Acharya")
st.sidebar.markdown("Yashaswini A")

# ---------- LOAD DATA ----------
@st.cache_data
def load_raw_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "data", "ev_data.csv")
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    return df

df = load_raw_data().copy()

# ---------- CALCULATIONS ----------
usable_energy = battery_capacity * (soc_percent / 100)
df["Range_km"] = df["Consumption"].apply(
    lambda c: round(usable_energy / c, 2) if c > 0 else 0
)
df["Energy_per_km"] = df["Consumption"] / df["Distance"]
df["Efficiency"] = df["Distance"] / df["Consumption"]

avg_range = round(df["Range_km"].mean(), 2)
max_range = round(df["Range_km"].max(), 2)
min_range = round(df["Range_km"].min(), 2)
avg_consumption = round(df["Consumption"].mean(), 4)
avg_speed = round(df["Speed"].mean(), 2)
avg_efficiency = round(df["Efficiency"].mean(), 3)

# ---------- METRIC CARDS ----------
st.subheader("📊 Range Calculation Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("⚡ Usable Energy", f"{usable_energy:.1f} kWh")
col2.metric("📍 Average Range", f"{avg_range} km")
col3.metric("🔺 Max Range", f"{max_range} km")
col4.metric("🔻 Min Range", f"{min_range} km")

col5, col6, col7 = st.columns(3)
col5.metric("⛽ Avg Consumption", f"{avg_consumption} kWh/km")
col6.metric("🚗 Avg Speed", f"{avg_speed} km/h")
col7.metric("📈 Avg Efficiency", f"{avg_efficiency} km/unit")

st.markdown("---")

# ---------- GRAPHS ----------
st.subheader("📈 Visualizations")

col_left, col_right = st.columns(2)

# Speed vs Consumption
with col_left:
    st.markdown("**Speed vs Energy Consumption**")
    speed_data = df.groupby("Speed")["Consumption"].mean().reset_index()
    fig1, ax1 = plt.subplots()
    ax1.plot(speed_data["Speed"], speed_data["Consumption"], marker='o', color='steelblue')
    ax1.set_xlabel("Speed (km/h)")
    ax1.set_ylabel("Consumption (kWh/km)")
    ax1.set_title("Speed vs Energy Consumption")
    ax1.grid(True)
    st.pyplot(fig1)

# Distance vs Consumption
with col_right:
    st.markdown("**Distance vs Energy Consumption**")
    dist_data = df.groupby("Distance")["Consumption"].mean().reset_index()
    fig2, ax2 = plt.subplots()
    ax2.plot(dist_data["Distance"], dist_data["Consumption"], marker='o', color='coral')
    ax2.set_xlabel("Distance (km)")
    ax2.set_ylabel("Consumption (kWh/km)")
    ax2.set_title("Distance vs Energy Consumption")
    ax2.grid(True)
    st.pyplot(fig2)

# Range Distribution
st.markdown("**Range Distribution across trips**")
fig3, ax3 = plt.subplots()
ax3.hist(df["Range_km"], bins=15, color='mediumseagreen', edgecolor='black')
ax3.set_xlabel("Range (km)")
ax3.set_ylabel("Number of Trips")
ax3.set_title(f"Range Distribution (SOC: {soc_percent}%, Battery: {battery_capacity} kWh)")
ax3.set_xlim(0, max_range * 1.2)
ax3.axvline(avg_range, color='red', linestyle='--', linewidth=2, label=f'Avg Range: {avg_range} km')
ax3.legend()
ax3.grid(True)
st.pyplot(fig3)

st.markdown("---")

# ---------- DATA TABLE ----------
st.subheader("📋 Raw Data Preview")
st.dataframe(df[["Speed", "Distance", "Consumption", "Range_km", "Efficiency"]])
