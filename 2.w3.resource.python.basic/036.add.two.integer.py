# https://www.w3resource.com/python-exercises/python-basic-exercise-36.php
# Write a Python program to add two objects if both objects are an integer type.

def add_numbers(x,y):
    if not (isinstance(x,int) and isinstance(y,int)):
        return "Input must be integers!"
    return x + y

print(add_numbers(2,5))
print(add_numbers(9,20.5))
print(add_numbers(1,60))
print(add_numbers('5',6))
print(add_numbers('1','5'))