# https://www.w3resource.com/python-exercises/python-basic-exercise-33.php

# Write a Python program to sum of three given integers.
#  However, if two values are equal sum will be zero

def sum(x, y, z):
    if x == y or y == z or z == x:
        sum = 0
    else :
        sum = x + y + z
    return sum

n1 = int(input("Enter your first number :\n"))
n2 = int(input("Enter your second number :\n"))
n3 = int(input("Enter your thired number :\n"))

print(f"sum of {n1} and {n2} and {n3} is :\n")
print(sum(n1,n2,n3))