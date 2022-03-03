# https://www.w3resource.com/python-exercises/python-basic-exercise-33.php

# Write a Python program to sum of three given integers.
#  However, if two values are equal sum will be zero

def sum(x, y, z):
    if x == y or y == z or z == x:
        sum = 0
    else :
        sum = x + y + z
    return sum

print(sum(2,3,4))
print(sum(1,1,1))
print(sum(12,12,13))