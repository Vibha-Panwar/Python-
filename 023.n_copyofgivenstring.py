# https://www.w3resource.com/python-exercises/python-basic-exercise-23.php

# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2

string = input("Enter your string:")
n = int(input("No. of copies :"))

def substring_copy(str,n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]
    result = ""
    for i in range(n):
        result = result + substr

    return result

print(substring_copy(string , n))   