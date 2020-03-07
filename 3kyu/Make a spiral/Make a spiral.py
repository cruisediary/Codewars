"""
https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

Make a spiral

Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


"""

def spiralize(size):
    matrix = list(map(lambda x: list(map(lambda y: 1 if (int(size + 1) / 2) % 2 == 1 else 0, range(0, size))), range(0, size)))
    spiral = 1
    for i in range(0, int(size / 2)):
        for u in range(0, size - i * 2):
            matrix[i][u+i] = spiral
            matrix[u+i][i] = spiral
            matrix[size - i - 1][u+i] = spiral
            matrix[u+i][size - i - 1] = spiral
            
            if size % 4 == 0:
                if i != int(size / 2) - 1:
                    matrix[i+1][i] = 1 - spiral
            else:
                matrix[i+1][i] = 1 - spiral
        spiral = 1 - spiral
    return matrix

"""

Sample Tests

Test.assert_equals(spiralize(5), [[1,1,1,1,1],
                                  [0,0,0,0,1],
                                  [1,1,1,0,1],
                                  [1,0,0,0,1],
                                  [1,1,1,1,1]])
Test.assert_equals(spiralize(6), [[1,1,1,1,1,1],
                                  [0,0,0,0,0,1],
                                  [1,1,1,1,0,1],
                                  [1,0,0,1,0,1],
                                  [1,0,0,0,0,1],
                                  [1,1,1,1,1,1]])
Test.assert_equals(spiralize(7), [[1,1,1,1,1,1,1],
                                  [0,0,0,0,0,0,1],
                                  [1,1,1,1,1,0,1],
                                  [1,0,0,0,1,0,1],
                                  [1,0,1,1,1,0,1],
                                  [1,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,1]])
Test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
                                  [0,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,0,1],
                                  [1,0,0,0,0,1,0,1],
                                  [1,0,1,0,0,1,0,1],
                                  [1,0,1,1,1,1,0,1],
                                  [1,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,1,1]])
"""
