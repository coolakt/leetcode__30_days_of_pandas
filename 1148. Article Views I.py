import pandas as pd

def article_views(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['author_id'] == df['viewer_id']][['author_id']]
    df = df.drop_duplicates().sort_values(by=['author_id'])
    df.columns = ['id']
    return df
