import pandas as pd

def findHeavyAnimals(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(by='weight', ascending=False).loc[df['weight']>100, ['name']]
    return df
