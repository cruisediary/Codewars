"""
https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals

List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:

sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19

"""

from functools import reduce
def sum_of_intervals(intervals):
    if not intervals:
        return 0
    sum = 0
    intervals.sort(key = lambda e: e[0])
    cursor = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= cursor[1]:
            cursor = (cursor[0], max(cursor[1], intervals[i][1]))
        else:
            sum += cursor[1] - cursor[0]
            cursor = intervals[i]
    sum += cursor[1] - cursor[0]
    return sum

"""

Sample Tests

Test.assert_equals(sum_of_intervals([(1, 5)]), 4)
Test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
Test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
Test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

"""
