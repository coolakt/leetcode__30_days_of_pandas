import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(courses.value_counts('class')).reset_index()
    return df[df['count'] >= 5][['class']]

