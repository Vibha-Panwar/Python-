# https://www.w3resource.com/python-exercises/python-basic-exercise-6.php

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

values = input("input some comma seprated numbers :")
list = values.split(",")
tuple = tuple(list)
print('list : ', list)
print('tuple : ', tuple)
