# https://www.w3resource.com/python-exercises/python-basic-exercise-20.php

# Write a Python program to get a string which is n (non-negative integer) copies of a given string

string = input("Enter your string :\t")
times = int(input("How many times you want to repeat : \t"))
result = ""
for i in range(times):
    result = result + string

print("New string : \n",result)