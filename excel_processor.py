import pandas as pd
import xlrd

def process_excel(uploaded_file):

    # Read xls file
    df = pd.read_excel(
        uploaded_file,
        header=4
    )

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    # Rename important columns
    df = df.rename(columns={
        "Operator.1": "Operator",
        "Total.3": "IDT",
        "Total.4": "NWT",
        "Total.5": "RWT",
        "Total.6": "TDT"
    })

    # Numeric conversion
    for col in ["IDT", "NWT", "RWT", "TDT", "Eff"]:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            ).fillna(0)

    # FILTER ONLY RED/YELLOW LIKE ROWS
    filtered_df = df[
        (df["Eff"] <= 10) |
        (df["NWT"] >= 350)
    ]

    return filtered_df
