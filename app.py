import pandas as pd

def process_excel(uploaded_file):

    filename = uploaded_file.name.lower()

    # READ XLSX
    if filename.endswith(".xlsx"):

        df = pd.read_excel(
            uploaded_file,
            header=4,
            engine="openpyxl"
        )

    # READ XLS
    else:

        df = pd.read_excel(
            uploaded_file,
            header=4,
            engine="xlrd"
        )

    # FORCE UNIQUE COLUMN NAMES
    df.columns = [
        "Group",
        "Operation",
        "Operator_No",
        "Operator_Name",
        "WIP",
        "SAM",
        "Target",
        "Machine_Type",
        "Pcs_1",
        "Pcs_2",
        "Pcs_3",
        "Pcs_4",
        "Pcs_5",
        "Pcs_6",
        "Pcs_7",
        "Pcs_8",
        "Pcs_9",
        "Total_Pcs",
        "EM",
        "AM",
        "IDT",
        "NWT",
        "RWT",
        "TDT",
        "Prodn",
        "Eff"
    ]

    # KEEP ONLY IMPORTANT COLUMNS
    df = df[
        [
            "Operation",
            "Operator_Name",
            "SAM",
            "Target",
            "IDT",
            "NWT",
            "RWT",
            "TDT",
            "Eff"
        ]
    ]

    # REMOVE EMPTY ROWS
    df = df[
        df["Operation"].notna()
    ]

    # NUMERIC CONVERSION
    numeric_cols = [
        "IDT",
        "NWT",
        "RWT",
        "TDT",
        "Eff"
    ]

    for col in numeric_cols:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        ).fillna(0)

    # ONLY CONSTRAINT + BEFORE CONSTRAINT
    filtered_df = df[
        (df["Eff"] <= 10) |
        (df["NWT"] >= 350)
    ]

    return filtered_df
