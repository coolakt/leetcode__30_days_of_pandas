import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    pairs = actor_director['actor_id director_id'.split()].value_counts().reset_index()
    return pairs[pairs['count'] >= 3]['actor_id director_id'.split()]
