# https://www.w3resource.com/python-exercises/python-basic-exercise-16.php

# Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference

digit = int(input("Enter your digit : \n"))
d = digit - 17

if d > 17 :
    print(f"your difference{d} is greater than 17 .")
    d = d*2
    print(f"Double of your difference is : {d}")
else :
    print(f"your difference {d} is less than 17 .")
