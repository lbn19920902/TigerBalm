'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-08-20
'''

def pandas_read_large_csv(file, chunksize = 10 ** 4):
	'''
		a wrapper function for reading huge csv files by smaller chuncks several times
	'''
	import pandas as pd
	chunks = []
	for chunk in pd.read_csv(file, chunksize = chunksize):
		chunks.append(chunk)
	return pd.concat(chunks)

