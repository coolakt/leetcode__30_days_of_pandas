import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sortd = employee['salary'].sort_values(ascending=False).drop_duplicates()
    if len(sortd) >= N:
        nvalue = sortd.iloc[N-1]
    else:
        nvalue = None
    return pd.DataFrame({f'getNthHighestSalary({N})':[nvalue]})
