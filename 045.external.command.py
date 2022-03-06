# https://www.w3resource.com/python-exercises/python-basic-exercise-45.php
# Write a python program to call an external command in Python.

from subprocess import call
call(["ls","-l"])