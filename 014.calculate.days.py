# https://www.w3resource.com/python-exercises/python-basic-exercise-14.php

# Write a Python program to calculate number of days between two dates.

from datetime import date 
one = input("Enter first date in DD/MM/YYYY format :\n")
two = input("Enter second date in DD/MM/YYYY format :\n")

date1 = one.split("/")
date2 = two.split("/")

f_date = date(int(date1[-1]),int(date1[1]),int(date1[0]))
l_date = date(int(date2[-1]),int(date2[1]),int(date2[0]))

delta = l_date - f_date
print("delta days :",delta.days)