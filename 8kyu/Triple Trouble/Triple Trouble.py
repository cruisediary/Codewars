"""
https://www.codewars.com/kata/5704aea738428f4d30000914/train/python

Triple Trouble

Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.

*/

def triple_trouble(one, two, three):
    return "".join(list(map(lambda x: "".join(x), zip(one, two, three))))

/*

Sample Tests

Test.describe("Basic tests")
Test.assert_equals(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
Test.assert_equals(triple_trouble("aaaaaa","bbbbbb","cccccc"), "abcabcabcabcabcabc")
Test.assert_equals(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
Test.assert_equals(triple_trouble("Bm", "aa", "tn"), "Batman")
Test.assert_equals(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")

*/
