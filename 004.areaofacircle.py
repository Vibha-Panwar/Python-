# https://www.w3resource.com/python-exercises/python-basic-exercise-4.php

# Write a Python program which accepts the radius of a circle from the user and compute the area

from math import pi
r=float(input("Enter circle radius:"))
print(type(r))
area = float(pi*r**2)
print("area of circle:\n")
print(area)
