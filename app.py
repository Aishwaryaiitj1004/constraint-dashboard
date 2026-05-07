import streamlit as st
import plotly.express as px
import pandas as pd
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

    st.subheader("Constraint Related Operations")

    st.dataframe(
        df,
        use_container_width=True
    )

    # KPI
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("IDT", int(df["IDT"].sum()))
    c2.metric("NWT", int(df["NWT"].sum()))
    c3.metric("RWT", int(df["RWT"].sum()))
    c4.metric("TDT", int(df["TDT"].sum()))

    # TDT VISUAL
    st.subheader("Total Downtime Analysis")

    fig1 = px.bar(
        df,
        x="Operation",
        y="TDT",
        color="TDT",
        text="TDT"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # EFF VISUAL
    st.subheader("Efficiency Analysis")

    fig2 = px.bar(
        df,
        x="Operation",
        y="Eff",
        color="Eff",
        text="Eff"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # LOSS VISUAL
    st.subheader("Loss Time Distribution")

    loss_df = pd.DataFrame({
        "Loss": ["IDT", "NWT", "RWT", "TDT"],
        "Value": [
            df["IDT"].sum(),
            df["NWT"].sum(),
            df["RWT"].sum(),
            df["TDT"].sum()
        ]
    })

    fig3 = px.pie(
        loss_df,
        names="Loss",
        values="Value"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
