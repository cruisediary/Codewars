"""
https://www.codewars.com/kata/571b2ee08d8c9c0d160014ec/train/python

How sexy is your name? Write a program that calculates how sexy one's name is according to the criteria below.

There is a preloaded dictionary of letter scores called SCORES. Add up the letters (case-insensitive) in your name to get your sexy score. Ignore other characters.

SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
          'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
          'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
          'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}
The program must return how sexy one's name is according to the "Sexy score ranking" chart.

       score <= 60:   'NOT TOO SEXY'
 61 <= score <= 300:  'PRETTY SEXY'
301 <= score <= 599:  'VERY SEXY'
       score >= 600:  'THE ULTIMATE SEXIEST'

"""

def sexy_name(name):
    SCORES[" "] = 0
    score = sum(list(map(lambda x: SCORES[x.upper()], name.strip())))
    if score <= 60:
        return "NOT TOO SEXY"
    elif score <= 300:
        return "PRETTY SEXY"
    elif score <= 599:
        return "VERY SEXY"
    else:
        return "THE ULTIMATE SEXIEST"

"""

Sample Tests

test.describe('Basic Tests')

test.it('Not too sexy!')
test.assert_equals(sexy_name('GUV'), 'NOT TOO SEXY')
test.assert_equals(sexy_name('PHUG'),"NOT TOO SEXY")
test.assert_equals(sexy_name('FFFFF'), 'NOT TOO SEXY')
test.assert_equals(sexy_name(''),"NOT TOO SEXY")
test.assert_equals(sexy_name('PHUG'),"NOT TOO SEXY")

test.it('Pretty sexy!')
test.assert_equals(sexy_name('BOB'),"PRETTY SEXY")
test.assert_equals(sexy_name('JLJ'), 'PRETTY SEXY')
test.assert_equals(sexy_name('HHHHHU'), 'PRETTY SEXY')
test.assert_equals(sexy_name('BOB'),"PRETTY SEXY")
test.assert_equals(sexy_name('WWWWWU'),"PRETTY SEXY")

test.it('Very sexy!')
test.assert_equals(sexy_name('YOU'), 'VERY SEXY')
test.assert_equals(sexy_name('FABIO'),"VERY SEXY")
test.assert_equals(sexy_name('ARUUUUUUUUU'), 'VERY SEXY')

test.it('The ultimate sexiest!')
test.assert_equals(sexy_name('ROBBY'), 'THE ULTIMATE SEXIEST')
test.assert_equals(sexy_name('SAMANTHA'), 'THE ULTIMATE SEXIEST')
test.assert_equals(sexy_name('DONALD TRUMP'), "THE ULTIMATE SEXIEST")
test.assert_equals(sexy_name('BILL GATES'), "THE ULTIMATE SEXIEST")
test.assert_equals(sexy_name('SCARLETT JOHANSSON'), "THE ULTIMATE SEXIEST")
test.assert_equals(sexy_name('CODEWARS'),"THE ULTIMATE SEXIEST")
test.assert_equals(sexy_name('PAMELA ANDERSON'),"THE ULTIMATE SEXIEST")

test.it('Should also handle lowercase letters')
test.assert_equals(sexy_name('you'), 'VERY SEXY')
test.assert_equals(sexy_name('Codewars'),"THE ULTIMATE SEXIEST")

"""
