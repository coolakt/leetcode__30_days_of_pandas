import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    if students.empty or subjects.empty:
        return pd.DataFrame(columns=('student_id','student_name','subject_name','attended_exams'))
    students['key']=1
    subjects['key']=1
    a=pd.merge(students,subjects,on='key',how='inner')
    a.drop(columns='key',inplace=True)
    b=examinations.groupby(['student_id','subject_name'])['subject_name'].count().reset_index(name='attended_exams')
    c=pd.merge(a,b,on=('student_id','subject_name'),how='left')
    return c.sort_values(['student_id','subject_name']).fillna(0)
