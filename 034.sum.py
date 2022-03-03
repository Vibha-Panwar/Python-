# https://www.w3resource.com/python-exercises/python-basic-exercise-34.php
# Write a Python program to sum of two given integers.
#  However, if the sum is between 15 to 20 it will return 20

def sum(x,y):
    sum = x+y
    if sum in range(15,20):
        return 20
    else:
        return sum

print(sum(10,6))
print(sum(5,6))
print(sum(8,7))