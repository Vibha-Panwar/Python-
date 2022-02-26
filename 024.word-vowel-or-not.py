# https://www.w3resource.com/python-exercises/python-basic-exercise-24.php

# Write a Python program to test whether a passed letter is a vowel or not

print("!!!!Vowels Verifier!!!!\t\n")
letter = input("Enter one character:")

def vowel_verify(letter):
    all_vowels ='aeiouAEIOU'
    return letter in all_vowels

print("Is your character vowel?",vowel_verify(letter))
