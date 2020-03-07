/*
https://www.codewars.com/kata/585894545a8a07255e0002f1/train/swift

Screen Locking Patterns

You might already be familiar with many smartphones that allow you to use a geometric pattern as a security measure. To unlock the device, you need to connect a sequence of dots/points in a grid by swiping your finger without lifting it as you trace the pattern through the screen. The image below has an example pattern of 7 dots/points: [A, B, I, E, D, G, C].

lock_example.png

For this kata, your job is to implement the function countPatternsFrom(firstPoint, length); where firstPoint is a single-character string corresponding to the point in the grid (i.e.: 'A') and length is an integer indicating the length of the pattern. The function must return the number of combinations starting from the given point, that have the given length.

Take into account that dots can only be connected with straight directed lines either:

horizontally (like A to B)
vertically (like D to G),
diagonally (like I and E, as well as B and I), or
passing over a point that has already been 'used' like (G and C passing over E).
The sample tests have some examples of the number of combinations for some cases to help you check your code.

Optional Extra:

Out of curiosity, in case you're wondering, for the Android lock screen, valid patterns must have between 4 and 9 dots, and there are 389112 possible valid combinations in total.

*/

let matrix = [[-1,0,1,0,0,0,3,0,4],
              [0,-1,0,0,0,0,0,4,0],
              [1,0,-1,0,0,0,4,0,5],
              [0,0,0,-1,0,4,0,0,0],
              [0,0,0,0,-1,0,0,0,0],
              [0,0,0,4,0,-1,0,0,0],
              [3,0,4,0,0,0,-1,0,7],
              [0,4,0,0,0,0,0,-1,0],
              [4,0,5,0,0,0,7,0,-1]]

extension Dot {
    static var allCases: [Dot] = [.a, .b, .c, .d, .e, .f, .g, .h, .i]

    var index: Int {
        return Dot.allCases.firstIndex(of: self)!
    }
}

func countPattern(from start: Int, locked: [Int], length: Int) -> Int {
    guard length > 0 else { return 1 }
    let indexs = matrix[start]
        .map { n in return n > 0 && locked.contains(n) ? 0 : n }
        .enumerated()
        .filter { $0.1 == 0 }
        .map { $0.0 }
        .filter { !locked.contains($0) }
    var sum = 0
    for index in indexs {
        sum += countPattern(from: index, locked: locked + [index], length: length - 1)
    }
    return sum
}

func countPatterns(from firstDot: Dot, length: Int) -> Int {
    guard (1...9).contains(length) else { return 0 }
    return countPattern(from: firstDot.index, locked: [firstDot.index], length: length - 1)
}

/*

Sample Tests

import XCTest

class ExampleTest: XCTestCase {
	static let testcases: [(start: Dot, length: Int, numPatterns: Int)] = [
		(.a, 0, 0),
		(.a, 10, 0),
		(.b, 1, 1),
		(.c, 2, 5),
		(.d, 3, 37),
    (.f, 3, 37),
		(.e, 4, 256),
		(.e, 8, 23280)
	]
	
	static var allTests = [
		("Example Testcases", example),
	]
	
	func example() {
		for test in ExampleTest.testcases {
			XCTAssertEqual(countPatterns(from: test.start, length: test.length), test.numPatterns)
		}
	}
}

XCTMain([
    testCase(ExampleTest.allTests)
])

/*
