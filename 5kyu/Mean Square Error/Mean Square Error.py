"""
https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python

Mean Square Error

Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair.
Examples

[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2

"""

def solution(array_a, array_b):
    return sum([((array_b[i] - array_a[i]) ** 2) for i in range(len(array_a))]) / len(array_a)

"""

Sample Tests

  
a1 = [1,2,3]
a2 = [4,5,6]
  
Test.assert_approx_equals(solution(a1, a2), 9)

b1 = [10, 20, 10, 2]
b2 = [10, 25, 5, -2]

Test.assert_approx_equals(solution(b1, b2), 16.5)

c1 = [0, -1]
c2 = [-1, 0]

Test.assert_approx_equals(solution(c1, c2), 1)

d1 = [10, 10]
d2 = [10, 10]

Test.assert_approx_equals(solution(d1, d2), 0)
"""
