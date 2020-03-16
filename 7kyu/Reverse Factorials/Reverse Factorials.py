"""
https://www.codewars.com/kata/58067088c27998b119000451/train/python

Reverse Factorials

I'm sure you're familiar with factorials – that is, the product of an integer and all the integers below it.

For example, 5! = 120, as 5 * 4 * 3 * 2 * 1 = 120

Your challenge is to create a function that takes any number and returns the number that it is a factorial of. So, if your function receives 120, it should return "5!" (as a string).

Of course, not every number is a factorial of another. In this case, your function would return "None" (as a string).

Examples

120 will return "5!"
24 will return "4!"
150 will return "None"

"""

def reverse_factorial(num):
    f = num
    n = 1
    while n <= f:
        f /= n
        n += 1
    return "None" if f != 1 else str(n-1) + "!"
    
"""

Sample Tests

test.assert_equals(reverse_factorial(120), '5!')
test.assert_equals(reverse_factorial(3628800), '10!')
test.assert_equals(reverse_factorial(150), 'None')

"""
