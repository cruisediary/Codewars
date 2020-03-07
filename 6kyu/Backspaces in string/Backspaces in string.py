"""
https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python

Backspaces in string

Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples

"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""

"""

def clean_string(s):
    ss = ""
    for c in s:
        ss = ss[:-1] if c == "#" else ss + c
    return ss

"""

Sample Tests

Test.assert_equals(clean_string('abc#d##c'), "ac")
Test.assert_equals(clean_string('abc####d##c#'), "" )
Test.assert_equals(clean_string("#######"), "" )
Test.assert_equals(clean_string(""), "" )
Test.assert_equals(clean_string("a####"), "" )

"""
