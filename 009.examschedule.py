# https://www.w3resource.com/python-exercises/python-basic-exercise-9.php

# Write a Python program to display the examination schedule. (extract the date from exam_st_date).

input_list = input("enter date in DD/MM/YYYY format :")
print(type(input_list))
date = input_list.split("/")
print(type(date))
print("day:",date[0])
print(type(date[0]))
print("month:",date[1])
print("year:",date[2])