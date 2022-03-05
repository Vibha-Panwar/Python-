# https://www.w3resource.com/python-exercises/python-basic-exercise-39.php
# Write a Python program to compute the future value of a specified principal amount,
#  rate of interest, and a number of years.

amt = 10000
int = 3
years = 7
Future_value = amt*((1+(0.01*int))**years)
print(round(Future_value,2))