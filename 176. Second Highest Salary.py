import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    us = list(employee['salary'].unique())
    us=sorted(us)
    if(len(us)<2):
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        return pd.DataFrame({'SecondHighestSalary':[us[-2]]})
