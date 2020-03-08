"""
https://www.codewars.com/kata/57a06005cf1fa5fbd5000216/train/python

Write function wordsToSentence which will create a string from a list of strings, separated by space.

Example:

["hello", "world"] -> "hello world"

"""

def words_to_sentence(words):
    return " ".join(words)


"""

Sample Tests

test.assert_equals(words_to_sentence(['bacon', 'is', 'delicious']), 'bacon is delicious')

"""
