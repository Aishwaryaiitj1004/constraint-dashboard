import pandas as pd

def process_excel(uploaded_file):

    df = pd.read_excel(
        uploaded_file,
        sheet_name=0,
        header=4
    )

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    df = df.dropna(how="all")

    return df
