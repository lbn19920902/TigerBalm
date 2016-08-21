'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-08-17
'''
from __future__ import print_function
from __future__ import division

def continuous_chunks(lst, num_chunks):
	"""
		generate contiunes smaller chunks from a given list
		
		Examples:
		-------------------------------------
		>>> a = continuous_chunks(range(11), 3)
		>>> for i in range(3):
				print(a.next())		
		[0, 1, 2, 3]
		[4, 5, 6, 7]
		[8, 9, 10]
	"""
	num_the_current_chunk = int(len(lst) / num_chunks + 0.5)
	for i in xrange(0, num_chunks - 1):
		yield lst[i*num_the_current_chunk:(i+1)*num_the_current_chunk]
	yield lst[(num_chunks -1)* num_the_current_chunk:]


