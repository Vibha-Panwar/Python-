# https://www.w3resource.com/python-exercises/python-basic-exercise-49.php
# Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import isfile,join
files_list = [f for f in listdir('/home/students') if isfile(join('/home/students',f)) ]
print(files_list);