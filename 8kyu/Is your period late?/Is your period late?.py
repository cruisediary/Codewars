"""
https://www.codewars.com/kata/578a8a01e9fd1549e50001f1/train/python

Is your period late?

In this kata, we will make a function to test whether a period is late.

Our function will take three parameters:

last - The Date object with the date of the last period

today - The Date object with the date of the check

cycleLength - Integer representing the length of the cycle in days

If the today is later from last than the cycleLength, the function should return true. We consider it to be late if the number of passed days is larger than the cycleLength. Otherwise return false.

"""

from datetime import *
def period_is_late(last,today,cycle_length):
    return last + timedelta(days = cycle_length) < today

"""

Sample Tests

Test.describe("Basic tests")
Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28), True)
Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28), False)
Test.assert_equals(period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28), False)
Test.assert_equals(period_is_late(date(2016, 7, 12), date(2016, 8, 10), 28), True)
Test.assert_equals(period_is_late(date(2016, 7, 1), date(2016, 8, 1), 30), True)
Test.assert_equals(period_is_late(date(2016, 6, 1), date(2016, 6, 30), 30), False)
Test.assert_equals(period_is_late(date(2016, 1, 1), date(2016, 1, 31), 30), False)
Test.assert_equals(period_is_late(date(2016, 1, 1), date(2016, 2, 1), 30), True)

"""
