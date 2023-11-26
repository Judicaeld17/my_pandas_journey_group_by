# TASK: Create a function which receive a pandas dataframe and a column to group by with as parameter. It returns a the result of the group by().
import pandas as pd
def my_pandas_journey_group_by(df,col_to_group_by):
    return df.groupby([col_to_group_by])
