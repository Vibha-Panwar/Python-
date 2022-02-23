# https://www.w3resource.com/python-exercises/python-basic-exercise-18.php

# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.

n1 = int(input("Enter first digit :\t"))
n2 = int(input("Enter second digit :\t"))
n3 = int(input("Enter third digit :\t"))

if n1==n2==n3:
    r = n1*3*3
    print(f"sum of {n1} {n2} {n3} digit is :{r}")
else:
    r = n1+n2+n3
    print(f"sum of {n1} {n2} {n3} digit is : {r}")