# https://www.w3resource.com/python-exercises/python-basic-exercise-15.php

# Write a Python program to get the volume of a sphere with radius 6.

from math import pi
r = float(input("Enter the radius : \n "))
volume = float((pi*r*r*r*4)/3)
print("volume of the sphere :",volume)