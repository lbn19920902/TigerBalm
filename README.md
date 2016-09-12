# TigerBalm 万金油

This repo will be a collection of some helper class/function or procedures that I wrote to solve some question but might also be in handy for similar tasks in the future.  

Better keep them in a place so that I can easily find and reuse them. : )  

## How to use them ?

	import sys
	sys.path.append(path_to_the_tiger_balm_repo)
	from pandas_helper import pandas_read_large_csv

## string_processing_helper.py
+ find_nth_occurrence: function to find the nth occurrence of a substring within the string from given oritentation  
+ remove_in_between: remove substrings within a given sub region of a string  

## data_feeding_helper.py
+ continuous_chunks: function to create a generator for continuous indices for small batches  
+ batch_generator: function to create batches of continuous chunks or random samples of the (X, y) pairs  

## pandas_helper.py
+ pandas_read_large_csv: function to read large csv file by concatenate smaller chunks to avoid memory issue  
+ duplicate_columns: find duplicate columns, return column names or return data frame without duplicated columns  

## sklearn_helper.py
+ plot_grid_search_result: function to plot GridSeachCV results by multiple facets  
+ plot_roc_curve: function to plot one or more ROC curves overlay  
+ clf_accuracy_score_by_class: function to classification accuracy by class  


  
