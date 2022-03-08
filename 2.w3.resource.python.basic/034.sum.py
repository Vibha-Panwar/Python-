# https://www.w3resource.com/python-exercises/python-basic-exercise-34.php
# Write a Python program to sum of two given integers.
#  However, if the sum is between 15 to 20 it will return 20

def sum(x,y):
    sum = x+y
    if sum in range(15,20):
        return 20
    else:
        return sum

n1 = int(input("Enter your first number :\n"))
n2 = int(input("Enter your second number :\n"))

print(f"sum of {n1} and {n2} is :\n")
print(sum(n1,n2))