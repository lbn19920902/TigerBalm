'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-10-08
'''
from __future__ import print_function

def pandas_read_large_csv(file, chunksize = 10 ** 5, verbose = False, **kwargs):
    '''
        a wrapper function for reading huge csv files by smaller chuncks several times
        updated Sept-22-16 can specify dtype, also increased chunksize by 10 
        example:
        data = pandas_read_large_csv("data/train_numeric.csv", chunksize = 100000, dtype = np.float32)
    '''
    import pandas as pd
    chunks = []
    i = 1
    for chunk in pd.read_csv(file, chunksize = chunksize, **kwargs):
        if verbose:
            print("reading chunk number {} of size {}".format(i, chunksize))
        chunks.append(chunk)
    if verbose:
        print("all data read, concatnating them together")
    return pd.concat(chunks)

def duplicate_columns(df, return_dataframe = False, verbose = False):
    '''
        a function to detect and possibly remove duplicated columns for a pandas dataframe
        as for now, it will drop the column more towards the left side
    '''
    from pandas.core.common import array_equivalent
    # group columns by dtypes, only the columns of the same dtypes can be duplicate of each other
    groups = df.columns.to_series().groupby(df.dtypes).groups
    duplicated_columns = []

    for dtype, col_names in groups.items():
        column_values = df[col_names]
        num_columns = len(col_names)

        # find duplicated columns by checking pairs of columns, store first column name if duplicate exist 
        for i in range(num_columns):
            if verbose:
                print("checking column number {}".format(i+1))
            column_i = column_values.iloc[:,i].values
            for j in range(i + 1, num_columns):
                column_j = column_values.iloc[:,j].values
                if array_equivalent(column_i, column_j):
                    if verbose: 
                        print("column {} is a duplicate of column {}".format(col_names[i], col_names[j]))
                    duplicated_columns.append(col_names[i])
                    break
    if not return_dataframe:
        # return the column names of those duplicated exists
        return duplicated_columns
    else:
        # return a dataframe with duplicated columns dropped 
        return df.drop(labels = duplicated_columns, axis = 1), duplicated_columns

