import pandas as pd

def process_excel(uploaded_file):

    # Read Excel (.xls supported)
    df = pd.read_excel(
        uploaded_file,
        header=4,
        engine="xlrd"
    )

    # Clean columns
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    # Rename columns
    rename_map = {
        "Operator.1": "Operator",
        "Total.3": "IDT",
        "Total.4": "NWT",
        "Total.5": "RWT",
        "Total.6": "TDT"
    }

    df = df.rename(columns=rename_map)

    # Numeric conversion
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

    # ONLY RED + YELLOW TYPE LOGIC
    filtered_df = df[
        (df["Eff"] <= 10) |
        (df["NWT"] >= 350)
    ]

    return filtered_df
