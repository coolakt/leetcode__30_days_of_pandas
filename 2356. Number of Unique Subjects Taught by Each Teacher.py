def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Group the dataframe into groups based on teacher_id
    # produces a pandas.DataFrame.groupby object
    result = teacher.groupby(by='teacher_id')

    # pandas.DataFrame.groupby has a .nunique() method - very useful!
    # .nunique() turns pandas.DataFrame.groupby back into a "normal" dataframe
    result = result.nunique()

    # Problem: our teacher_id is used as index not a column. 
    # We can turn it back to a column using
    result['teacher_id'] = result.index

    # Getting rid of index, using inplace to overwrite result
    # Saves us using result = ...
    result.reset_index(drop=True)

    # Gotta rename a column to match the requirements
    result.rename(columns={'subject_id':'cnt'}, inplace=True)

    # Returning just the columns we need.
    return result[['teacher_id','cnt']]
