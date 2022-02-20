# https://www.w3resource.com/python-exercises/python-basic-exercise-14.php

# Write a Python program to calculate number of days between two dates.

from datetime import date 
first_date = date(2022,3,10)
last_date = date(2022,3,28)
alpha = last_date - first_date 
print(alpha.days)