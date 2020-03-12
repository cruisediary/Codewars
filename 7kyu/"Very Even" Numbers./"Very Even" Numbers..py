/*
https://www.codewars.com/kata/58c9322bedb4235468000019/train/python

"Very Even" Numbers.

Description:

#Task:

Write a function that returns true if the number is a "Very Even" number.

If a number is a single digit, then it is simply "Very Even" if it itself is even.

If it has 2 or more digits, it is "Very Even" if the sum of it's digits is "Very Even".

#Examples:

input(88) => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd 

input(222) => returns true

input(5) => returns false

input(841) => returns true -> 8 + 4 + 1 = 13 -> 1 + 3 => 4 is even

*/

def is_very_even_number(n):
    if n < 10:
        return n % 2 == 0
    return is_very_even_number(sum(list(map(lambda x: int(x), str(n)))))

/*

Sample Tests

@test.describe('Sample tests')
def sample_tests():
  sample_tests = [
    [0,    True ],
    [4,    True ],
    [12,   False],
    [222,  True ],
    [5,    False],
    [45,   False],
    [4554, False],
    [1234, False],
    [88,   False],
    [24,   True ],
    [400000220, True]
  ]
    
  for n, expected in sample_tests:
    test.assert_equals(is_very_even_number(n), expected, 'Testing for n = ' + str(n))

*/
