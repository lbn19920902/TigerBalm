
def continuous_chunks(indices, num_chunks):
	"""

	"""
	num_the_current_chunk = int(1.0 * len(indices) / num_chunks + 0.5)

	for i in xrange(0, num_chunks - 1):
		yield indices[i*num_the_current_chunk:(i+1)*num_the_current_chunk]
	yield indices[(num_chunks -1)* num_the_current_chunk:]


a = continuous_chunks(range(11), 3)
print(a.next())
print(a.next())
print(a.next())