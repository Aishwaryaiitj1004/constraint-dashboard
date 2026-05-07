import streamlit as st
import plotly.express as px
from excel_processor import process_excel

st.set_page_config(
    page_title="Constraint Dashboard",
    layout="wide"
)

st.title("Constraint Operations Dashboard")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xls", "xlsx"]
)

if uploaded_file:

    df = process_excel(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df)

    # KPIs
    col1, col2, col3, col4 = st.columns(4)

    if "IDT" in df.columns:
        col1.metric("Total IDT", round(df["IDT"].sum(), 2))

    if "NWT" in df.columns:
        col2.metric("Total NWT", round(df["NWT"].sum(), 2))

    if "RWT" in df.columns:
        col3.metric("Total RWT", round(df["RWT"].sum(), 2))

    if "TDT" in df.columns:
        col4.metric("Total TDT", round(df["TDT"].sum(), 2))

    # Loss Time Chart
    loss_cols = ["IDT", "NWT", "RWT", "TDT"]

    available_cols = [c for c in loss_cols if c in df.columns]

    if available_cols:

        chart_df = df[available_cols].sum().reset_index()

        chart_df.columns = ["Loss Type", "Time"]

        fig = px.bar(
            chart_df,
            x="Loss Type",
            y="Time",
            color="Loss Type",
            title="Loss Time Analysis"
        )

        st.plotly_chart(fig, use_container_width=True)

    # Table
    st.subheader("Processed Data")
    st.dataframe(df)
