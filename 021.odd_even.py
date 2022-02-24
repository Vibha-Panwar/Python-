# https://www.w3resource.com/python-exercises/python-basic-exercise-21.php

# Write a Python program to find whether a given number (accept from the user) is even or odd,
# print out an appropriate message to the user.

No = int(input("Enter a no.: \t"))
mod = No % 2
if mod == 0:
    print("",No,"is an even number.")
else:
    print("",No,"is an odd number.")