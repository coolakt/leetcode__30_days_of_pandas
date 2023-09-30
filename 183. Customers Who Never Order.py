import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result=pd.merge(customers, orders, 
    left_on='id', right_on='customerId', how='left', indicator=True ).\
    query(''' _merge=='left_only' ''' ).\
    filter(['name'])

    result.columns = ['Customers']

    return result 
    
