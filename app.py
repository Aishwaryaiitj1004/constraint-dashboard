import streamlit as st
import pandas as pd
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

    # Rename columns
    df = df.rename(columns={
        "Total.3": "IDT",
        "Total.4": "NWT",
        "Total.5": "RWT",
        "Total.6": "TDT",
        "Operator.1": "Operator"
    })

    # Numeric conversion
    for col in ["IDT", "NWT", "RWT", "TDT", "Eff"]:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            ).fillna(0)

    # =========================
    # KPI CARDS
    # =========================

    st.subheader("Loss Time Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("IDT", int(df["IDT"].sum()))
    c2.metric("NWT", int(df["NWT"].sum()))
    c3.metric("RWT", int(df["RWT"].sum()))
    c4.metric("TDT", int(df["TDT"].sum()))

    # =========================
    # RED - CONSTRAINT
    # =========================

    st.subheader("🔴 Constraint Operations")

    constraint_df = df.nsmallest(10, "Eff")

    fig1 = px.bar(
        constraint_df,
        x="Operation",
        y="Eff",
        color="Eff",
        text="Eff",
        title="Constraint Operations Efficiency"
    )

    fig1.update_layout(
        xaxis_title="Operation",
        yaxis_title="Efficiency"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # =========================
    # YELLOW - BEFORE CONSTRAINT
    # =========================

    st.subheader("🟡 Before Constraint Operations")

    fig2 = px.bar(
        df.head(10),
        x="Operation",
        y="NWT",
        color="NWT",
        text="NWT",
        title="Before Constraint Operations"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # =========================
    # GREY - LOSS TIME
    # =========================

    st.subheader("⚫ Loss Time Analysis")

    loss_df = pd.DataFrame({
        "Loss Type": ["IDT", "NWT", "RWT"],
        "Value": [
            df["IDT"].sum(),
            df["NWT"].sum(),
            df["RWT"].sum()
        ]
    })

    fig3 = px.pie(
        loss_df,
        names="Loss Type",
        values="Value",
        title="Loss Time Distribution"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # =========================
    # GREEN - TOTAL LOSS
    # =========================

    st.subheader("🟢 Total Loss Time")

    fig4 = px.bar(
        df,
        x="Operation",
        y="TDT",
        color="TDT",
        title="Total Downtime by Operation"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # =========================
    # TABLE
    # =========================

    st.subheader("Production Data")

    st.dataframe(
        df,
        use_container_width=True
    )
