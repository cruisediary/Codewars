"""
https://www.codewars.com/kata/5845e6a7ae92e294f4000315/train/python

Sum of nested numbers

Build a function sumNestedNumbers/sum_nested_numbers that finds the sum of all numbers in a series of nested arrays raised to the power of their respective nesting levels. Numbers in the outer most array should be raised to the power of 1.

For example,

sumNestedNumbers([1, [2], 3, [4, [5]]])
should return 1 + 2*2 + 3 + 4*4 + 5*5*5 === 149

"""

def sum_nested(arr, depth):
    if isinstance(arr, int):
        return arr ** depth
    return sum(list(map(lambda x: sum_nested(x, depth + 1), arr)))

def sum_nested_numbers(arr):
    if not arr:
        return None
    return sum_nested(arr, 0)

"""

Sample Tests

Test.describe("Basic tests")
Test.assert_equals(sum_nested_numbers([0]), 0)
Test.assert_equals(sum_nested_numbers([1, 2, 3, 4, 5]), 15)
Test.assert_equals(sum_nested_numbers([1, [2], 3, [4, [5]]]), 149)
Test.assert_equals(sum_nested_numbers([6, [5], [[4]], [[[3]]], [[[[2]]]], [[[[[1]]]]]]), 209)
Test.assert_equals(sum_nested_numbers([1, [-1], [[1]], [[[-1]]], [[[[1]]]]]), 5)

"""
