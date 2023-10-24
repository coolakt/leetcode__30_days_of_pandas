import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, how = 'inner', left_on = 'departmentId', right_on = 'id')
    df = df[df.salary == df.groupby('id_y')['salary'].transform(max)][['name_y','name_x', 'salary']]
    df = df.rename(columns = {'name_y':'Department', 'name_x':'Employee','salary':'Salary'})
    return df
