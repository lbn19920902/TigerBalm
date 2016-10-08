'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-10-08
'''

from __future__ import print_function
from __future__ import division

def gangup(char, length):
	return "".join([char for _ in range(length)])

def jumbotron(text, line_width = 80, text_width = 60):
	"""
		print out text wrapped with upper and bottom line breaks
		example:
			import sys
			sys.path.append("C:\Users\Ryan\Documents\GitHub\TigerBalm")
			from rub import jumbotron
			jumbotron("abc")
	"""
	from math import ceil
	from datetime import datetime
	line_break = gangup("-", line_width)
	line_padding = gangup(" ", int(line_width/2 - text_width/2))
	print(line_break)
	num_lines = int(ceil(len(text)/text_width))
	for line_num in range(num_lines):
		if line_num == num_lines - 1:
			print(line_padding + text[line_num*text_width:])
		else:
			print(line_padding + text[line_num*text_width: (line_num +1) * text_width])
	print(line_padding + str(datetime.now()))
	print(line_break)

