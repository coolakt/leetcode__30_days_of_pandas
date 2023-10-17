import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    reshaped_df = report.melt(id_vars='product')
    reshaped_df = reshaped_df.rename(columns={
        "variable":"quarter",
        "value":"sales"
    })
    return reshaped_df
