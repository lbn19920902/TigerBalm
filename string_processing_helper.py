'''
    @ Ren Zhang : ryanzjlib@gmail.com 
    last update : 2016-08-09
'''


from __future__ import print_function


def find_nth_occurrence(fullstr, substr, n, left = True):
    '''
        find the start position of the nth occurrence of a substring within a string
        the last parameters indicates it is the nth occurrence from left or right 
    '''
    if left:
        start = fullstr.find(substr)
        while start >= 0 and n > 1:
            start = fullstr.find(substr, start+len(substr))
            n -= 1
    else:
        start = fullstr.rfind(substr)
        while start <= len(fullstr) and n > 1:
            start = fullstr.rfind(substr, 0, start)
            n -= 1
    return start


def remove_in_between(fullstr, substr, start_location, end_location):
    '''
        remove substring within a string but only in a specified region
    '''
    return fullstr[:start_location] + fullstr[start_location:end_location].replace(substr, " ") + fullstr[end_location:]


'''
print(find_nth_occurrence("abcdabcdabcdabcd", "bc", 2, True)) # should be 5
print(find_nth_occurrence("abcdabcdabcdabcd", "bc", 1, False)) # should be 13

# imagine a row with 8 fields in a \t seperated format with multiple "\t" s within the text

row = "123\t2\t2016-08-09\t'what\t if\tthere are\t some \t\t\tin the text\t field'\tNEW\tCLIENT\t248"
print(row.split("\t")) # will not give you the ideal result
text_start = find_nth_occurrence(row, "\t", 3, True) + 1 
text_end = find_nth_occurrence(row, "\t", 3, False)
row = remove_in_between(row, "\t", text_start, text_end)
print([element for element in row.split("\t")]) # this is more like the result you want
'''
