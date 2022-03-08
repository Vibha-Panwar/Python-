# https://www.w3resource.com/python-exercises/python-basic-exercise-29.php

# Write a Python program to print out a set containing all the colors from color_list_1 
# which are not present in color_list_2.
# Test Data:
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

color_list_1 = set(["white","black","red"])
color_list_2 = set(["red","green"])
print("Original set element:")
print(color_list_1)
print(color_list_2)
print("\n Differenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\n Differenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))