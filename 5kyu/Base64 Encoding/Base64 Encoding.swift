/*
https://www.codewars.com/kata/5270f22f862516c686000161/train/swift

Base64 Encoding

Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.

Do not use built in functions.

Usage:

// should return "dGhpcyBpcyBhIHN0cmluZyEh"
"this is a string!!".toBase64 

// should return 'this is a string!!'
"dGhpcyBpcyBhIHN0cmluZyEh".fromBase64
You can learn more about Base64 encoding and decoding here.

Note: This kata uses the non-padding version ("=" is not added to the end).

*/

extension String {
    public var toBase64: String {
        return Data(self.utf8).base64EncodedString()
    }
  
    public var fromBase64: String {
        guard let data = Data(base64Encoded: self) else { return "" }
        guard let str = String(data: data, encoding: .utf8) else { return "" }
        return str
    }
}

/*

Sample Tests

import XCTest
class SolutionTest: XCTestCase {
	
	static let base64Chars: [UInt8] = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".utf8)
	
	static let testStrings = [
		("this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"),
		("this is a test!","dGhpcyBpcyBhIHRlc3Qh"),
		("now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"),
		("1234567890  ", "MTIzNDU2Nzg5MCAg"),
		("ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"),
		("the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"),
		("dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"),
		("VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"),
		("TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"),
		("e", "ZQ=="),
		("ee", "ZWU=")
	]
	
	static var allTests = [
		("Encode Test", encodeTest),
		("Decode Test", decodeTest)
	]
	
	func encodeTest() {
		for stringPair in SolutionTest.testStrings {
			XCTAssertEqual(stringPair.0.toBase64, stringPair.1)
		}
	}
	
	func decodeTest() {
		for stringPair in SolutionTest.testStrings {
			XCTAssertEqual(stringPair.1.fromBase64, stringPair.0)
		}
	}
}


XCTMain([
	testCase(SolutionTest.allTests)
])

*/
