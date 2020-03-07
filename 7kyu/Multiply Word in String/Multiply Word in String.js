/*
https://www.codewars.com/kata/5ace2d9f307eb29430000092/train/javascript

Multiply Word in String

You are to write an function that takes a string as it's first paramter. This string will be a string of words.
You are expected to then use the second parameter, which will be an integer, to find the corresponding word in the given string. The first word would be represented by 0.
Once you have the located string you are finally going to multiply by it the third provided paramater, which will also be an interger. You are additionally required to add a hyphen in between each word.

Example
modifyMultiply ("This is a string",3,5)

Should return

"string-string-string-string-string"

Since the 3rd word is 'string'(starting from 0 remember) and the third paramater indicates that it should be repeated 5 times.

Simple. Good luck.

*/

function modifyMultiply (str,loc,num) {
    return [...Array(num).keys()].map(function () { return str.split(" ")[loc] }).join("-");
} 

/*

Sample Tests

  Test.assertEquals(modifyMultiply("This is a string",3 ,5), "string-string-string-string-string", "The string is incorrect");
  Test.assertEquals(modifyMultiply("Creativity is the process of having original ideas that have value. It is a process; it's not random.",8 ,10), "that-that-that-that-that-that-that-that-that-that");
  Test.assertEquals(modifyMultiply("Self-control means wanting to be effective at some random point in the infinite radiations of my spiritual existence",1 ,1), "means");
  Test.assertEquals(modifyMultiply("Is sloppiness in code caused by ignorance or apathy? I don't know and I don't care.",6 ,8), "ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance");
  Test.assertEquals(modifyMultiply("Everything happening around me is very random. I am enjoying the phase, as the journey is far more enjoyable than the destination.",2 ,5), "around-around-around-around-around");

*/

