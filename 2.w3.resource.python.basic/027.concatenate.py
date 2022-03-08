# https://www.w3resource.com/python-exercises/python-basic-exercise-27.php

# Write a Python program to concatenate all elements in a list into a string and return it.

def concatenate_list_data(list):
    result = ''
    for element in list :
        result += str(element)
    return result

print("Enter your list :\n")
list1 = input("->\t")

print("Input veriable is:",type(list1))
print("User can not give input in list type.")
print("Giving list as input in program hardcoded.")

print(concatenate_list_data(["V","I","B","H","A"]))