import pandas as pd

def dropMissingData(s: pd.DataFrame) -> pd.DataFrame:
    return s.dropna()
