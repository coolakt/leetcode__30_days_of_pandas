import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    aggs = {
        'num_sold': pd.NamedAgg('product', 'nunique'),
        'products': pd.NamedAgg('product', lambda s: ','.join(sorted(s.unique()))) 
    }
    return activities.groupby('sell_date', as_index=False).agg(**aggs)
