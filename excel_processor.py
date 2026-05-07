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

    # MAKE COLUMN NAMES UNIQUE
    cols = []
    count = {}

    for col in df.columns:

        col = str(col).strip()

        if col in count:
            count[col] += 1
            new_col = f"{col}_{count[col]}"
        else:
            count[col] = 0
            new_col = col

        cols.append(new_col)

    df.columns = cols

    # RENAME IMPORTANT COLUMNS
    rename_map = {
        "Operator.1": "Operator",
        "Total.3": "IDT",
        "Total.4": "NWT",
        "Total.5": "RWT",
        "Total.6": "TDT"
    }

    df = df.rename(columns=rename_map)

    # CONVERT NUMERIC COLUMNS
    numeric_cols = [
        "IDT",
        "NWT",
        "RWT",
        "TDT",
        "Eff"
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            ).fillna(0)

    # FILTER IMPORTANT ROWS
    filtered_df = df[
        (df["Eff"] <= 10) |
        (df["NWT"] >= 350)
    ]

    return filtered_df
