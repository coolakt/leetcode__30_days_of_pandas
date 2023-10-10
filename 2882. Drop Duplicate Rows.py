import pandas as pd

def dropDuplicateEmails(c: pd.DataFrame) -> pd.DataFrame:
    return c.drop_duplicates(subset='email')
