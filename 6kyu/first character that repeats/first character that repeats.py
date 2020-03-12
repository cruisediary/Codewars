/*
https://www.codewars.com/kata/54f9f4d7c41722304e000bbb/train/python

first character that repeats

Find the first character that repeats in a String and return that character.

first_dup('tweet') => 't'
first_dup('like') => None
This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'.

*/

def first_dup(s):
    for x in s:
        if s.count(x) > 1:
            return x
    return None

/*

Sample Tests

test.assert_equals(first_dup('tweet'), 't')
test.assert_equals(first_dup('Ode to Joy'), ' ')
test.assert_equals(first_dup('ode to joy'), 'o')
test.assert_equals(first_dup('bar'), None)
test.assert_equals(first_dup('123123'), '1');
test.assert_equals(first_dup('!@#$!@#$'), '!');
test.assert_equals(first_dup('1a2b3a3c'), 'a');

*/
