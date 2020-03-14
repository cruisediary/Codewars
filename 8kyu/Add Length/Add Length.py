"""
https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python

Add Length

What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.

"""

def add_length(str_):
    return list(map(lambda x: " ".join([x, str(len(x))]) , str_.split(" ")))

"""

Sample Tests

Test.assert_equals(add_length('apple ban'),["apple 5", "ban 3"])
Test.assert_equals(add_length('you will win'),["you 3", "will 4", "win 3"])
Test.assert_equals(add_length('you'),["you 3"])
Test.assert_equals(add_length('y'),["y 1"])

"""
