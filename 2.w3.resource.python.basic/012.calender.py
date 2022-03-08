# https://www.w3resource.com/python-exercises/python-basic-exercise-12.php

# Write a Python program to print the calendar of a given month and year.

import calendar

input_string = input("Enter the month and year in mm/yyyy format :")
date = input_string.split("/")
m = int(date[0])
y = int(date[-1])

print("printing calendar for the month",m,"and year",y)
print(calendar.month(y,m))