import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    return scores.assign(rank = scores['score'].rank(method='dense',ascending=False))[['score','rank']].sort_values(by='rank',ascending=True)
    
