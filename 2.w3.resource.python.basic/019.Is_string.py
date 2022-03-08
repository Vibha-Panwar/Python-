# https://www.w3resource.com/python-exercises/python-basic-exercise-19.php
# Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

def new_string(str):
    if len(str) >= 2 and str[:2] == "Is" :
        return str
    return "Is" + str

string = input("Enter string :\t")
print(new_string (string))