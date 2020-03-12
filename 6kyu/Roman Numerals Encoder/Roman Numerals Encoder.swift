/*
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/swift

Roman Numerals Encoder

Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) // should return "M"
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

*/

func solution(_ number:Int) -> String {
    func convert(number: Int, ten: String, five: String, one: String) -> String {
        switch number {
        case 4:
            return one + five
        case 9:
            return one + ten
        default:
            return number >= 5 ? five + (0..<(number - 5)).map { _ in one }.joined() : (0..<number).map { _ in one }.joined()
        }
    }

    var roman = ""
    roman += convert(number: (number / 1000), ten: "", five: "", one: "M")
    roman += convert(number: (number % 1000) / 100, ten: "M", five: "D", one: "C")
    roman += convert(number: ((number % 100) / 10), ten: "C", five: "L", one: "X")
    roman += convert(number: (number % 10), ten: "X", five: "V", one: "I")
    return roman
}

/*

Sample Tests

import XCTest

class SolutionTest: XCTestCase {
    static var allTests = [
        ("testOneThroughTen", testOneThroughTen),
        ("testBigNumbers", testBigNumbers),
    ]

    func testOneThroughTen() {
        XCTAssertEqual(solution(1), "I")
        XCTAssertEqual(solution(2), "II")
        XCTAssertEqual(solution(3), "III")
        XCTAssertEqual(solution(4), "IV")
        XCTAssertEqual(solution(5), "V")
        XCTAssertEqual(solution(6), "VI")
        XCTAssertEqual(solution(7), "VII")
        XCTAssertEqual(solution(8), "VIII")
        XCTAssertEqual(solution(9), "IX")
        XCTAssertEqual(solution(10), "X")
    }
    
    func testBigNumbers() {
        XCTAssertEqual(solution(100), "C")
        XCTAssertEqual(solution(444), "CDXLIV")
        XCTAssertEqual(solution(1000), "M")
        XCTAssertEqual(solution(1954), "MCMLIV")
        XCTAssertEqual(solution(1990), "MCMXC")
        XCTAssertEqual(solution(1999), "MCMXCIX")
        XCTAssertEqual(solution(2000), "MM")
        XCTAssertEqual(solution(2008), "MMVIII")
        XCTAssertEqual(solution(3000), "MMM")
        XCTAssertEqual(solution(3900), "MMMCM")
        XCTAssertEqual(solution(3914), "MMMCMXIV")
    }
}

XCTMain([
    testCase(SolutionTest.allTests)
])

*/
