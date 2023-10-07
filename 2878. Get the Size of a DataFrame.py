import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df=pd.DataFrame(players)
    lt=[len(df),len(df.columns)]
    return lt
