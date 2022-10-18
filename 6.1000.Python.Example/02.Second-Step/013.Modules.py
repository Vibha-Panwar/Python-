### Modules :--> Module is just a Python file with a set of functions. It is same as code liberary.
# modules contain function but it can also contain variable of all type like- array, Dictionary etc.
"""
def add(a, b):
    return a+b
z = add(2,3)
print(z) 

import my_calculator
z = my_calculator.add(6,3)
print(z)

# A module is simply a Python file with a .py extension that can be imported inside another Python program.
# The name of the Python file becomes the module name.
# The module contains definitions and implementation of classes, variables, and functions that can be used inside another program.

import my_calculator
Q = my_calculator.sub(4,6)
print(Q)

from my_calculator import multi

print(multi(4, 5))

import sys
print(sys.path)

### Flat Project directory Structure:-->

### Runtime Loading of modules :-->
print("Start running")

import mygreet
mygreet.hello()
print("Done")

### Conditional loading of modules :-->
import random
print("Start running")
name = input("Your Name: ")

if name == "Foo":
    import mygreet
    mygreet.hello()
else:
    print("No loading")

print("Done")

### Duplicate importing of functions:-->
from my_calculator import add
print(add(2, 5))

#from my_math import add
#print(add(3, 6))

from my_calculator import multi
print(multi(5, 8))


### Script or Library :-->
def run():
    print("run in ",__name__)

print("Name space in Module.py",__name__)
if __name__ == '__main__':
    run()

## Script or Library - Import :-->
# If it is importes by another module then it won't run automatically.
# We have to call it manually.

### Assert to verify values :-->
def add(x, y):
    return x*y

for x, y, z in [(2,2,4), (9,2,18), (2,3,5)]:
    print(f"add({x}, {y}) == {z}")
    if add(x, y) != z:
        raise Exception(f"add{x, y} != {z}")
"""
def add(x, y):
    return x*y
for x, y, z in [(2, 2, 4), (9, 2, 11), (2, 3, 5)]:
    print(f"add({x}, {y}) != {z}")
    assert add(x, y) == z