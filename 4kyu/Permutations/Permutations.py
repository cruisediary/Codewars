"""
https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

Permutations

In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.

"""

def permutations(string):
    if len(string) == 1:
        return string
    answer = []
    for x in string:
        answer = answer + list(map(lambda p: x + p, permutations(string.replace(x,'',1))))
    return set(answer)

"""

Sample Tests

Test.assert_equals(sorted(permutations('a')), ['a']);
Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
Test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

"""
