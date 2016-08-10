'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-08-09
'''


from __future__ import print_function


def find_nth_occurrence(str, substr, n, left = True):
    '''
        find the start position of the nth occurrence of a substring within a string
        the last parameters indicates it is the nth occurrence from left or right 
        my actual uscase: 
            when i was writing code to parse a "\t" sepearted data file which has a data field that is actually
            some transcripts of phone calls. there might be couple of "\t"s within the text field for some rows,
            so a simple row.split("\t") will not give back lists that is desired to form a dataframe. 
            i used this code to find the begining and end of the text field for each row, and then replaced the "\t"s
            within the text field so that afterwards i can split on "\t" to get equal number of elements for every row.   
    '''
    if left:
        start = str.find(substr)
        while start >= 0 and n > 1:
            start = str.find(substr, start+len(substr))
            n -= 1
    else:
        start = str.rfind(substr)
        while start <= len(str) and n > 1:
            start = str.rfind(substr, 0, start)
            n -= 1
    return start

'''
print(find_nth_occurrence("abcdabcdabcdabcd", "bc", 2, True)) # should be 5
print(find_nth_occurrence("abcdabcdabcdabcd", "bc", 1, False)) # should be 13

# imagine a row with 8 fields in a \t seperated format with multiple "\t" s within the text

row = "123\t2\t2016-08-09\t'what\t if\tthere are\t some \t\t\tin the text\t field'\tNEW\tCLIENT\t248"
print(row.split("\t")) # will not give you the ideal result
text_start = find_nth_occurrence(row, "\t", 3, True) + 1 
text_end = find_nth_occurrence(row, "\t", 3, False)
row = row[:text_start] + row[text_start:text_end].replace("\t", " ") + row[text_end:]
print([element for element in row.split("\t")]) # this is more like the result you want
'''
