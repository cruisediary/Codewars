"""
https://www.codewars.com/kata/536a155256eb459b8700077e/train/python

The Clockwise Spiral

Do you know how to make a spiral? Let's test it!

Classic definition: A spiral is a curve which emanates from a central point, getting progressively farther away as it revolves around the point.

Your objective is to complete a function createSpiral(N) that receives an integer N and returns an NxN two-dimensional array with numbers 1 through NxN represented as a clockwise spiral.

Return an empty array if N < 1 or N is not int / number

Examples:

N = 3 Output: [[1,2,3],[8,9,4],[7,6,5]]

1    2    3    
8    9    4    
7    6    5    
N = 4 Output: [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
N = 5 Output: [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]

1   2   3   4   5    
16  17  18  19  6    
15  24  25  20  7    
14  23  22  21  8    
13  12  11  10  9

"""

def create_spiral(n):
    if not isinstance(n, int):
        return ""
    matrix = [[1 for i in range(n)] for j in range(n)]
    width = n
    i = 0
    number = 1
    while 0 < width:
        if width == 1:
            matrix[i][i] = number
        else:
            for x in range(0, width - 1):
                matrix[i][i+x] = number + x
                matrix[i+x][i + width - 1] = (width - 1) + number + x
                matrix[i + width - 1][i + width - 1 - x] = 2 * (width - 1) + number + x
                matrix[i + width - 1 - x][i] = 3 * (width - 1) + number + x
            number = matrix[i+1][i] + 1
        width -= 2
        i += 1
    return matrix

"""

Sample Tests

Test.assert_equals(sout(create_spiral(3)), '[1, 2, 3][8, 9, 4][7, 6, 5]')

"""
