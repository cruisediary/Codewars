"""
https://www.codewars.com/kata/5868812b15f0057e05000001/train/python

Tail Swap

You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.

Examples

["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]

"""

def tail_swap(strings):
    left = strings[0].split(":")
    right = strings[1].split(":")
    return list(map(lambda x: ":".join(x), [[left[0], right[1]], [right[0], left[1]]]))

"""

Sample Tests

test.assert_equals(tail_swap(['abc:123', 'cde:456']),
                             ['abc:456', 'cde:123'])
test.assert_equals(tail_swap(['a:12345', '777:xyz']),
                             ['a:xyz',   '777:12345'])

"""
