"""
https://www.codewars.com/kata/522551eee9abb932420004a0/train/python

N-th Fibonacci

I love Fibonacci numbers in general, but I must admit I love some more than others.

I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.

For example:

   nth_fib(4) == 2
Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.

"""

cache = {1:0, 2:1, 3:1, 4:2}
def nth_fib(n):
    if n in cache:
        return cache[n]
    left = cache[n-1] if n-1 in cache else nth_fib(n-1)
    right = cache[n-2] if n-2 in cache else nth_fib(n-2)
    return left + right

"""

Sample Tests

test.assert_equals(nth_fib(1), 0)
test.assert_equals(nth_fib(2), 1)
test.assert_equals(nth_fib(3), 1)
test.assert_equals(nth_fib(4), 2)
test.assert_equals(nth_fib(5), 3)
test.assert_equals(nth_fib(6), 5)
test.assert_equals(nth_fib(7), 8)
test.assert_equals(nth_fib(8), 13)

"""
