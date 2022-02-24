# https://www.w3resource.com/python-exercises/python-basic-exercise-21.php

# Write a Python program to find whether a given number (accept from the user) is even or odd,
# print out an appropriate message to the user.

num = int(input("Enter a number :"))
mod = num % 2
if mod > 0 :
    print("This num is an odd number.")
else :
    print("This num is an even number.")