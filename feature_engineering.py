'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-10-14
'''
import pandas as pd
from itertools import combinations

def two_way_interaction(col1, col2, data = None):
    """
        generate encoded two way interaction
        input:
            can be either data as a dataframe and col1 and col2 are two strings for column names
            or 
            col1 and col2 are two pandas Series
        example:
        import pandas as pd
        df = pd.DataFrame({ 'col1' : ['a', 'a', 'b', 'b', 'a', 'c'], 'col2' : ['2', '3', '2', '3', '2', '3']})
        two_way_interaction('col1', 'col2', df)
        # returned: array([0, 1, 2, 3, 0, 4])
    """
    if data is not None and type(col1) == str and type(col2) == str:
        return  pd.factorize(data[[col1, col2]].apply(lambda row: "_".join(row), axis = 1))[0]
    else:
        temp = pd.DataFrame({'col1':col1, 'col2':col2})
        return  pd.factorize(temp.apply(lambda row: "_".join(row), axis = 1))[0]

def generate_two_way_interactions(data, cat_feature_list):
    """
        generate all possible two-way interactions and return them as a dataframe
        import pandas as pd
        df = pd.DataFrame({ 'col1' : ['a', 'a', 'b', 'b', 'a', 'c'], 'col2' : ['2', '3', '2', '3', '2', '3']})
        df = generate_two_way_interactions(df, ['col1', 'col2'])
        df
        # output:
        #  col1 col2  col1_col2
        #0    a    2          0
        #1    a    3          1
        #2    b    2          2
        #3    b    3          3
        #4    a    2          0
        #5    c    3          4
    """
    if verbose:
        counter = 0
    returnDF = pd.DataFrame()
    for col1, col2 in combinations(cat_feature_list, 2):
        returnDF["_".join([col1, col2])] = two_way_interaction(data[col1], data[col2])
        if verbose:
            counter +=1
            if counter % 100 == 0:
                print("{} generated {}".format(counter, datetime.now()))
    return returnDF

def generate_two_way_interactions_from_pairs(data, pair_list, verbose = False):
    """
        generate two way interactions only on specified categorical variable pairs
    """
    returnDF = pd.DataFrame()
    if verbose:
        counter = 0
    for col1, col2 in pair_list:
        returnDF["_".join([col1, col2])] = two_way_interaction(data[col1], data[col2])
        if verbose:
            counter +=1
            if counter % 100 == 0:
                print("{} generated {}".format(counter, datetime.now()))
    return returnDF  
