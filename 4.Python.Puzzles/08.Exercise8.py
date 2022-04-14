# https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-8.php
# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.

def test(string):
    import re
    merged = re.split(r"([ ,]+)",string)
    return [merged[::2],merged[1::2]]

s = "W3resource Python,Exercise"
print("original string:",s)
print("split the said string into 2 list:Words and separators")
print(test(s))

D = 'The dance, held in school gym, ended in the midnight.'
print("\t New string is:",D)
print("split the given string into 2 list : Words and Separators")
print(test(D))

V = "The colour of the study room is blue, yellow, and green."
print("\t new string is:",V)
print("Again split the given string into 2 list: Words and Separators")
print(test(V))