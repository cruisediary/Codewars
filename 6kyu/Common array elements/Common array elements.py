"""
https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/python

Common array elements

Given three arrays of integers, return the sum of elements that are common in all three arrays.

For example:

common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays
Array lengths in random tests run from 5000 to 10000 elements.

More examples in the test cases.

Good luck!

"""

from collections import Counter
def common(a,b,c):
    ca = Counter(a)
    cb = Counter(b)
    cc = Counter(c)
    keys = Counter(a+b+c).keys()
    return sum(list(map(lambda x: x * min(ca[x], cb[x], cc[x]), keys)))
    
"""

Sample Tests

Test.it("Basic tests")
Test.assert_equals(common([1,2,3],[5,3,2],[7,3,2]),5)
Test.assert_equals(common([1,2,2,3],[5,3,2,2],[7,3,2,2]),7)

"""
