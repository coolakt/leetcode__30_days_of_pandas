import pandas as pd

def modifySalaryColumn(emp: pd.DataFrame) -> pd.DataFrame:
    emp['salary']=emp['salary']*2
    return emp
