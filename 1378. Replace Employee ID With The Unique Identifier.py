import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    ans=employees.merge(employee_uni, on='id', how='left')
    return ans[['unique_id', 'name']]
  
