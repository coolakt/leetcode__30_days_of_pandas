import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[(employees['employee_id']%2==0) | (employees['name'].str.startswith('M')), 'salary'] = 0
    employees.rename(columns = {'salary':'bonus'}, inplace = True)
    return employees[['employee_id', 'bonus']].sort_values(by = 'employee_id')
