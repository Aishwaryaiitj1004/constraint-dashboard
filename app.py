import streamlit as st
import pandas as pd
import plotly.express as px

from excel_processor import process_excel

# Page config
st.set_page_config(
    page_title="Constraint Dashboard",
    layout="wide"
)

st.title("Constraint Operations Dashboard")

# Upload file
uploaded_file = st.file_uploader(
    "Upload Daily Excel File",
    type=["xls", "xlsx"]
)

if uploaded_file:

    # Process excel
    df = process_excel(uploaded_file)

    st.success("File Uploaded Successfully")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total IDT", round(df["IDT"].sum(), 2))
    col2.metric("Total NWT", round(df["NWT"].sum(), 2))
    col3.metric("Total RWT", round(df["RWT"].sum(), 2))
    col4.metric("Total TDT", round(df["TDT"].sum(), 2))

    # Chart Data
    kpi_data = {
        "KPI": ["IDT", "NWT", "RWT", "TDT"],
        "Value": [
            df["IDT"].sum(),
            df["NWT"].sum(),
            df["RWT"].sum(),
            df["TDT"].sum()
        ]
    }

    chart_df = pd.DataFrame(kpi_data)

    # Create chart
    fig = px.bar(
        chart_df,
        x="KPI",
        y="Value",
        title="Loss Time Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Show dataframe
    st.subheader("Processed Data")
    st.dataframe(df)
