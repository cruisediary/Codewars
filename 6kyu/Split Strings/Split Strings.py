"""
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

Split Strings

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

"""

def solution(s):
    s = s + "_" if len(s) % 2 == 1 else s
    return list(map(lambda x: s[x:x+2], range(0, len(s), 2)))

"""
test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
"""

