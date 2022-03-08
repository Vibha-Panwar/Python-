# https://www.w3resource.com/python-exercises/python-basic-exercise-10.php

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("Enter a digit:"))
for i in range(0,5):
    print("itration no.",i,"and value is",n)
    n=n*n