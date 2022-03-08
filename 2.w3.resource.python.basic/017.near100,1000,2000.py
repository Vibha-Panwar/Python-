# https://www.w3resource.com/python-exercises/python-basic-exercise-17.php

# Write a Python program to test whether a number is within 100 of 1000 or 2000.

# abs() function returns the absolute value.

def near_thousand(n):
    return((abs(1000-n)<=100) or(abs(2000-n)<=100))

n = int(input("Enter your digit :\n"))
print("Is your digit near to 1000 or 2000 :",near_thousand(n))