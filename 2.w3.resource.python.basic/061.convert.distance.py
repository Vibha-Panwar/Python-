# https://www.w3resource.com/python-exercises/python-basic-exercise-61.php
# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

d_ft = int(input("Input a distance in feet:"))
d_inches = d_ft * 12
d_yards = d_ft / 3
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches ." %d_inches)
print("The distance in yards is %.2f yards." %d_yards)
print("The distance in miles is %.2f miles." %d_miles)
