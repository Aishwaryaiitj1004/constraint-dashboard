import pandas as pd
from openpyxl import load_workbook

def process_excel(uploaded_file):

    wb = load_workbook(uploaded_file)
    ws = wb.active

    records = []

    current_line = None

    for row in ws.iter_rows():

        values = [cell.value for cell in row]

        # Detect LINE
        first_cell = str(values[0]) if values[0] else ""

        if "LINE NO." in first_cell:
            current_line = first_cell
            continue

        # Skip empty rows
        if all(v is None for v in values):
            continue

        try:
            operation = values[1]
            operator = values[3]

            idt = values[22]
            nwt = values[23]
            rwt = values[24]
            tdt = values[25]
            eff = values[27]

        except:
            continue

        # Detect row color
        fill_color = row[1].fill.start_color.rgb

        row_type = "NORMAL"

        if fill_color:

            fill_color = str(fill_color)

            if "FF0000" in fill_color:
                row_type = "CONSTRAINT"

            elif "FFFF00" in fill_color:
                row_type = "BEFORE_CONSTRAINT"

        # Keep only red/yellow rows
        if row_type != "NORMAL":

            records.append({
                "LINE": current_line,
                "ROW_TYPE": row_type,
                "Operation": operation,
                "Operator": operator,
                "IDT": idt,
                "NWT": nwt,
                "RWT": rwt,
                "TDT": tdt,
                "Eff": eff
            })

    df = pd.DataFrame(records)

    # Numeric conversion
    for col in ["IDT", "NWT", "RWT", "TDT", "Eff"]:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        ).fillna(0)

    return df
