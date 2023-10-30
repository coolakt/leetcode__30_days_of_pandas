import pandas as pd

def total_time(df: pd.DataFrame) -> pd.DataFrame:
    df = df.assign(total_time=df['out_time'] - df['in_time'])
    df_new = df.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    df_new.columns = ['day', 'emp_id', 'total_time']
    return df_new
