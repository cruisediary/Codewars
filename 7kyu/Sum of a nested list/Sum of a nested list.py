"""
https://www.codewars.com/kata/5a15a4db06d5b6d33c000018/train/python

Sum of a nested list

Implement a function to calculate the sum of the numerical values in a nested list. For example :

sum_nested([1, [2, [3, [4]]]]) -> 10

"""

def sum_nested(lst):
    if isinstance(lst, int):
        return lst
    return sum(list(map(lambda x: sum_nested(x), lst)))

"""
test.describe('Should handle non-nested lists')
test.assert_equals(sum_nested([1]), 1)
test.assert_equals(sum_nested([1, 2, 3, 4]), 10)
test.assert_equals(sum_nested(list(range(11))), 55)
test.describe('Non-nested edge case')
test.assert_equals(sum_nested([]), 0)

test.describe('Should handle simple nestings')
test.assert_equals(sum_nested([[1], []]), 1)
test.assert_equals(sum_nested([[1, 2, 3, 4]]), 10)

test.describe('Simple nesting edge case')
test.assert_equals(sum_nested([[], []]), 0)

test.describe('Should handle more complex nestings')
test.assert_equals(sum_nested([1, [1], [[1]], [[[1]]]]), 4)
test.assert_equals(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]), 8)

test.describe('Complex nesting edge case')
test.assert_equals(sum_nested([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]), 0)
"""
