import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(company, on = 'com_id')
    df = df.loc[df['name'] == 'RED']
    return sales_person.loc[~sales_person['sales_id'].isin(df['sales_id'].unique())][['name']]
