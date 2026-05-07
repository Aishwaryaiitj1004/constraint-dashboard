import pandas as pd
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

    # IMPORTANT BUSINESS LOGIC
    # ONLY KEEP:
    # 1. RED ROWS -> CONSTRAINT OPERATIONS
    # 2. YELLOW ROWS -> BEFORE CONSTRAINT OPERATIONS
    #
    # Since pandas cannot directly read Excel colors
    # from xls reliably on Streamlit Cloud,
    # we approximate the same logic using:
    #
    # LOW EFFICIENCY = CONSTRAINT
    # HIGH NWT = BEFORE CONSTRAINT

    filtered_df = df[
        (df["Eff"] <= 10) |
        (df["NWT"] >= 350)
    ].copy()

    # REMOVE EMPTY OPERATIONS
    filtered_df = filtered_df[
        filtered_df["Operation"].notna()
    ]

    # KEEP ONLY IMPORTANT COLUMNS
    required_cols = [
        "Operation",
        "Operator",
        "SAM",
        "Target",
        "IDT",
        "NWT",
        "RWT",
        "TDT",
        "Eff"
    ]

    final_cols = [
        c for c in required_cols
        if c in filtered_df.columns
    ]

    filtered_df = filtered_df[final_cols]

    return filtered_df
