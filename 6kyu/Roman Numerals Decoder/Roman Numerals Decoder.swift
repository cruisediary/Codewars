/*
https://www.codewars.com/kata/51b6249c4612257ac0000005/train/swift

Roman Numerals Decoder

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution("XXI") // should return 21
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

*/

import Foundation

let romanToNumber = ["M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1]

func solution(_ string: String) -> Int {
    let convert = ["CD": "CCCC", "CM": "CCCCCCCCC", "XL": "XXXX", "XC": "XXXXXXXXX", "IV": "IIII", "IX": "IIIIIIIII"]
    var convertedRoman = string
    for (key, value) in convert {
        convertedRoman = convertedRoman.replacingOccurrences(of: key, with: value)
    }
    return convertedRoman.compactMap { romanToNumber[String($0)] }.reduce(0, +)
}

/*

Sample Tests

import XCTest
// XCTest Spec Example:
// TODO: replace with your own tests (TDD), these are just how-to examples to get you started

class SolutionTest: XCTestCase {
    static var allTests = [
        ("testOneThroughTen", testOneThroughTen),
        ("testBigNumbers", testBigNumbers),
    ]

    func testOneThroughTen() {
        XCTAssertEqual(solution("I"), 1)
        XCTAssertEqual(solution("II"), 2)
        XCTAssertEqual(solution("III"), 3)
        XCTAssertEqual(solution("IV"), 4)
        XCTAssertEqual(solution("V"), 5)
        XCTAssertEqual(solution("VI"), 6)
        XCTAssertEqual(solution("VII"), 7)
        XCTAssertEqual(solution("VIII"), 8)
        XCTAssertEqual(solution("IX"), 9)
        XCTAssertEqual(solution("X"), 10)
    }
    
    func testBigNumbers() {
        XCTAssertEqual(solution("C"), 100)
        XCTAssertEqual(solution("CDXLIV"), 444)
        XCTAssertEqual(solution("M"), 1000)
        XCTAssertEqual(solution("MCMLIV"), 1954)
        XCTAssertEqual(solution("MCMXC"), 1990)
        XCTAssertEqual(solution("MCMXCIX"), 1999)
        XCTAssertEqual(solution("MM"), 2000)
        XCTAssertEqual(solution("MMVIII"), 2008)
        XCTAssertEqual(solution("MMM"), 3000)
        XCTAssertEqual(solution("MMMCM"), 3900)
        XCTAssertEqual(solution("MMMCMXIV"), 3914)
    }
    
}

XCTMain([
    testCase(SolutionTest.allTests)
])

*/
