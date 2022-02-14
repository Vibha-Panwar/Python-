# https://www.w3resource.com/python-exercises/python-basic-exercise-8.php

# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

input_list = input("enter a list element seprated by comma\t")
color_list = input_list.split(",")
print("your color_list is :\t", color_list)
print("first color :",color_list[0])
print("last color :",color_list[-1])
