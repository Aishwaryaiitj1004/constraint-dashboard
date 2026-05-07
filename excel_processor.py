import pandas as pd
import streamlit as st

def process_excel(uploaded_file):

    # Read Excel
    df = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=4
    )

    # Clean column names
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    # Remove empty rows
    df = df.dropna(how="all")

    # Convert numeric columns
    numeric_cols = ["IDT", "NWT", "RWT", "TDT"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Debug
    st.write("Detected Columns:", df.columns.tolist())

    return df
