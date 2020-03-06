/*
https://www.codewars.com/kata/51b66044bce5799a7f000003/train/swift

Roman Numerals Helper

Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Examples

RomanNumerals.toRoman(1000); // should return 'M'
RomanNumerals.fromRoman('M'); // should return 1000
Help

| Symbol | Value | |----------------| | I | 1 | | V | 5 | | X | 10 | | L | 50 | | C | 100 | | D | 500 | | M | 1000 |
*/

class RomanNumerals {
    static let numberToRoman = [1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"]
    static let romanToNumber = ["M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1]

    static func toRoman(_ number: Int) -> String {
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

    static func fromRoman(_ roman: String) -> Int {
        let convert = ["CD": "CCCC", "CM": "CCCCCCCCC", "XL": "XXXX", "XC": "XXXXXXXXX", "IV": "IIII", "IX": "IIIIIIIII"]
        var convertedRoman = roman
        for (key, value) in convert {
            convertedRoman = convertedRoman.replacingOccurrences(of: key, with: value)
        }
        return convertedRoman.compactMap { romanToNumber[String($0)] }.reduce(0, +)
    }
}

import XCTest
// XCTest Spec Example:
// TODO: replace with your own tests (TDD), these are just how-to examples to get you started

class SolutionTest: XCTestCase {
    static var allTests = [
        ("1000 should equal M", testRoman1000),
        ("999 should equal CMXCIX", testRoman999),
        ("4 should equal IV", testRoman4),
        ("1 should equal I", testRoman1),
        ("1991 should equal MCMXCI", testRoman1991),
        ("2006 should equal MMVI", testRoman2006), 
        ("2020 should equal MMXX", testRoman2020), 
        
        ("XXI should equal 21", testInteger21),
        ("I should equal 1", testInteger1),
        ("III should equal 3", testInteger3),
        ("IV should equal 4", testInteger4),
        ("MMVII should equal 2007", testInteger2007),
        ("MDCLXIX should equal 1669", testInteger1669),
    ]

    func testRoman1000() {
        XCTAssertEqual(RomanNumerals.toRoman(1000), "M")
    }
    
    func testRoman999() {
        XCTAssertEqual(RomanNumerals.toRoman(999), "CMXCIX")
    }
    
    func testRoman4() {
        XCTAssertEqual(RomanNumerals.toRoman(4), "IV")
    }
    
    func testRoman1() {
        XCTAssertEqual(RomanNumerals.toRoman(1), "I")
    }
    
    func testRoman1991() {
        XCTAssertEqual(RomanNumerals.toRoman(1991), "MCMXCI")
    }
    
    func testRoman2006() {
        XCTAssertEqual(RomanNumerals.toRoman(2006), "MMVI")
    }
    
    func testRoman2020() {
        XCTAssertEqual(RomanNumerals.toRoman(2020), "MMXX")
    }

    func testInteger21() {
        XCTAssertEqual(RomanNumerals.fromRoman("XXI"), 21)
    }
    
    func testInteger1() {
        XCTAssertEqual(RomanNumerals.fromRoman("I"), 1)
    }
    
    func testInteger3() {
        XCTAssertEqual(RomanNumerals.fromRoman("III"), 3)
    }
    
    func testInteger4() {
        XCTAssertEqual(RomanNumerals.fromRoman("IV"), 4)
    }
    
    func testInteger2007() {
        XCTAssertEqual(RomanNumerals.fromRoman("MMVII"), 2007)
    }
    
    func testInteger1669() {
        XCTAssertEqual(RomanNumerals.fromRoman("MDCLXIX"), 1669)
    }
}
