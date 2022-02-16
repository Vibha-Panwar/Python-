# https://www.w3resource.com/python-exercises/python-basic-exercise-9.php

# Write a Python program to display the examination schedule. (extract the date from exam_st_date).

input_list = input("enter date in DD/MM/YYYY format :")
date = input_list.split("/")
print("day:",date[0])
print("month:",date[1])
print("year:",date[2])