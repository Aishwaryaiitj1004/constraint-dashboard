import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader(
    "Upload Excel",
    type=["xls", "xlsx"]
)

if uploaded_file:

    filename = uploaded_file.name.lower()

    if filename.endswith(".xlsx"):
        df = pd.read_excel(
            uploaded_file,
            header=4,
            engine="openpyxl"
        )
    else:
        df = pd.read_excel(
            uploaded_file,
            header=4,
            engine="xlrd"
        )

    st.write(df.columns.tolist())
