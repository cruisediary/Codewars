"""
https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python

Reverse List Order

In this kata you will create a function that takes in a list and returns a list with the reverse order.

"""

def reverse_list(l):
    return l[::-1]

"""

Sample Tests

test.assert_equals(reverse_list([1,2,3,4]), [4,3,2,1])
test.assert_equals(reverse_list([3,1,5,4]), [4,5,1,3])

"""
