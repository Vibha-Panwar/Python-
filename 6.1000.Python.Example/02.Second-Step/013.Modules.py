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
"""
### Flat Project directory Structure:-->
