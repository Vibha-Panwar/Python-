# https://www.w3resource.com/python-exercises/python-basic-exercise-53.php
# Write a python program to access environment variables.

import os
print('*-------------------------------------------*')
print(os.environ)
print('*--------------------------------------------*')
print(os.environ['HOME'])
print('*--------------------------------------------*')
print(os.environ['PATH'])
print('*--------------------------------------------*')