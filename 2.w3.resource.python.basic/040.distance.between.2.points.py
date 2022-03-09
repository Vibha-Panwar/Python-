# https://www.w3resource.com/python-exercises/python-basic-exercise-40.php
# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math
p1 = [4,0]
p2 = [6,6]
distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

print(distance)