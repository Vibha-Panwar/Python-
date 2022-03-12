# https://www.w3resource.com/python-exercises/python-basic-exercise-60.php
# Write a Python program to calculate the hypotenuse of a right angled triangle.

from math import sqrt
print("Input lengths of a right angle triangle:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)

print("The length of hypotenuse of the triangle is :",c)