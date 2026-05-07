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
    df.columns = df.columns.astype(str).str.strip()

    # Show columns for debugging
    st.write("Detected Columns:", df.columns.tolist())

    return df
