"""
https://www.codewars.com/kata/5a1e1b69697598459d000057/train/python

Get recursion limit

In the sys module there is a function sys.setrecursionlimit and sys.getrecursionlimit. These two functions set and get the recursion limit. If function calls stack is larger than this limit it will raise a RuntimeError

Examples of these two functions:

import sys
sys.setrecursionlimit(905)
sys.getrecursionlimit() # returns 905
sys.setrecursionlimit(89)
sys.getrecursionlimit() # returns 89
Task

Write a function `fetch_recursion_limit` that acts the same as `sys.getrecursionlimit` without importing any libraries.

`10 >= Recursion Limit <= 20000`
Hint: Write a recursive function

"""

def getrecursionlimit(n):
    try:
        return getrecursionlimit(n+1)
    except RuntimeError:
        return n+2

def fetch_recursion_limit():
    return getrecursionlimit(1)

"""

Sample Tests

import sys

tests = [200, 899, 1000, 89, 567, 390, 768]

for expected in tests:
    sys.setrecursionlimit(expected)
    test.assert_equals(fetch_recursion_limit(), expected)

"""
