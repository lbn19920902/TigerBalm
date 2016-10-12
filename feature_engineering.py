def two_way_interaction(data, col1, col2):
    """
        generate encoded two way interaction
        example:
        import pandas as pd
        df = pd.DataFrame({ 'col1' : ['a', 'a', 'b', 'b', 'a', 'c'], 'col2' : ['2', '3', '2', '3', '2', '3']})
        two_way_interaction(df, 'col1', 'col2')
        # returned: array([0, 1, 2, 3, 0, 4])
    """
    return  pd.factorize(data[[col1, col2]].apply(lambda row: "_".join(row), axis = 1))[0]


def generate_two_way_interactions(data, cat_feature_list):
    """
        generate all possible two-way interactions and merge them into the dataframe
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
    from itertools import combinations
    for col1, col2 in combinations(cat_feature_list, 2):
        data["_".join([col1, col2])] = two_way_interaction(data, col1, col2)
    return data