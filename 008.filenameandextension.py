# https://www.w3resource.com/python-exercises/python-basic-exercise-7.php

#Write a Python program to accept a filename from the user and print the extension of that.

filename = input("enter your filename with extension :")
extension = filename.split(".")
print("file extension is:",repr(extension[-1]))