import streamlit as st
import pandas as pd
import plotly.express as px
from excel_processor import process_excel

st.set_page_config(layout="wide")

st.title("Constraint Dashboard")

uploaded_file = st.file_uploader(
    "Upload Excel",
    type=["xls", "xlsx"]
)

if uploaded_file:

    df = process_excel(uploaded_file)

    # Rename columns
    df = df.rename(columns={
        "Total.3": "IDT",
        "Total.4": "NWT",
        "Total.5": "RWT",
        "Total.6": "TDT"
    })

    # Convert to numbers
    for col in ["IDT", "NWT", "RWT", "TDT"]:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            ).fillna(0)

    # RED - Constraint Operations
    st.subheader("🔴 Constraint Operations")

    fig1 = px.bar(
        df,
        x="Operation",
        y="TDT",
        color="TDT"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # YELLOW - Before Constraint
    st.subheader("🟡 Before Constraint Operations")

    fig2 = px.bar(
        df,
        x="Operation",
        y="NWT",
        color="NWT"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # LOSS VISUALS
    st.subheader("⚫ Loss Time Analysis")

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
