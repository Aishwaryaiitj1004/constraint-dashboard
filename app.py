import streamlit as st
import plotly.express as px
from excel_processor import process_excel

st.set_page_config(layout="wide")

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

    # TDT VISUAL
    st.subheader("TDT by Line")

    fig1 = px.bar(
        df,
        x="LINE",
        y="TDT",
        color="ROW_TYPE",
        text="Operation",
        barmode="group"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # EFFICIENCY VISUAL
    st.subheader("Efficiency Comparison")

    fig2 = px.bar(
        df,
        x="LINE",
        y="Eff",
        color="ROW_TYPE",
        text="Operation",
        barmode="group"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # LOSS TIME VISUAL
    st.subheader("Loss Time Analysis")

    loss_df = df[
        ["IDT", "NWT", "RWT", "TDT"]
    ].sum().reset_index()

    loss_df.columns = ["Loss Type", "Value"]

    fig3 = px.pie(
        loss_df,
        names="Loss Type",
        values="Value"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
