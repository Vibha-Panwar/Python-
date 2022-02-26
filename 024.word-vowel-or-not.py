# https://www.w3resource.com/python-exercises/python-basic-exercise-24.php

# Write a Python program to test whether a passed letter is a vowel or not

def w_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(w_vowel('c'))
print(w_vowel('e'))