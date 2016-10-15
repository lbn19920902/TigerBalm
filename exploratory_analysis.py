'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-10-14
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
custom_style = {
        'axes.labelcolor': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white'
    }
sns.set_style("whitegrid", rc=custom_style)
plt.rcParams["figure.figsize"] = (16, 9)

def SP_cat_feature_vs_cont_target(data, cat_feature, target, context = 'IPython', upper_std = 1.64, lower_std = 1.64):
	"""
		this function print out summary table for continuous target variables by levels of a categorical variable
		also plot violin plots with x as the levels of the categorical variable and y as the continuous target variable
	"""
    summary_table = data[target].groupby(data[cat_feature]).describe().unstack().reset_index()
    if context == 'IPython':
    	from IPython.display import display
	    display(summary_table)
	else:
		from pprint import pprint
		pprint(summary_table)
    lower_y = summary_table['25%'].min() - lower_std * summary_table['std'].median()
    upper_y = summary_table['75%'].max() + upper_std * summary_table['std'].median()
    ax = sns.violinplot(x=cat_feature, y= target, data=data);
    ax.set(ylim=(lower_y, upper_y))
    plt.show()

