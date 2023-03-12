## There are 3 types of number in python dictionary:
# Integer (1,45,34647)
# Float (1.34, 35.124456)
# Complex (1j)
## And you have already know which command to use to find the type an object.
# -> print(type(object))

# Integer:

x = 12
y = 231232454523445
z = -245353
print(type(x))
print(type(y))
print(type(z))

# Float :
x = 12.345
y = 1.0
z = -8.677564
print(type(x))
print(type(y))
print(type(z))

# Float can be specified with an "e", indicated power of 10.
x = 34e5
y = 12e3456
z = 456e2
print(type(x))
print(type(y))
print(type(z))

# Complex : complex are written with a "j" as an imaginary part.
x = 3+5j
y = 2+1j
z = 23+1j
print(type(x))
print(type(y))
print(type(z))

## Convert type of object.
x = 1
y = 1.1
z = 1j

a = float(x)
b = int(y)
c = complex(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1,50))
