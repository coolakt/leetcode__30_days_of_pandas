import pandas as pd

def find_patients(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['conditions'].apply(lambda x: ' DIAB1' in ' ' + ' '.join(x.split()))]
    
