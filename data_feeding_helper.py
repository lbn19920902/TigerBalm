'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-08-17
'''
from __future__ import print_function
from __future__ import division
import numpy as np


def continuous_batches(lst, num_batches):
	"""
		generate contiunes smaller batches from a given list
		
		Examples:
		-------------------------------------
		>>> a = continuous_batches(range(11), 3)
		>>> for i in range(3):
				print(a.next())		
		[0, 1, 2, 3]
		[4, 5, 6, 7]
		[8, 9, 10]
	"""
	num_the_current_batch = np.ceil(len(lst) / num_batches)
	for i in xrange(0, num_batches - 1):
		yield lst[i*num_the_current_batch:(i+1)*num_the_current_batch]
	yield lst[(num_batches -1)* num_the_current_batch:]

def batch_generator(X, y, batch_size, shuffle):
	"""
		modified version, generate batches of X and y rather than just the indices
		also allow random shuffle
		X should be np/scipy matrix
	"""
    number_of_batches = X.shape[0]/batch_size
    current_batch = 0
    sample_index = np.arange(X.shape[0])
    if shuffle:
        np.random.shuffle(sample_index)
    while True:
        batch_index = sample_index[batch_size*current_batch:batch_size*(current_batch+1)]
        X_batch = X[batch_index,:].toarray()
        y_batch = y[batch_index]
        current_batch += 1
        yield X_batch, y_batch
        if (current_batch == number_of_batches):
            if shuffle:
                np.random.shuffle(sample_index)
            current_batch = 0

