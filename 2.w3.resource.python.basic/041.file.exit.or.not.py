# https://www.w3resource.com/python-exercises/python-basic-exercise-41.php
# Write a Python program to check whether a file exists.

import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))