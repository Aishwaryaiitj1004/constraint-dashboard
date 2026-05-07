import pandas as pd

def process_excel(uploaded_file):

    df = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=4
    )

    # Remove unwanted rows
    df = df[df["Group"] != "Seq.No"]

    # Convert KPI columns
    kpi_cols = ["IDT", "NWT", "RWT", "TDT"]

    for col in kpi_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        ).fillna(0)

    return df
