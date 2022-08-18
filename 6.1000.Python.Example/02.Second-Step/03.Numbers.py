a = 42 # decimal
h = 0xA # 10 - Hexadecimal - starting with 0x (?)
o = 0o11 # 9- octal -- Starting with 0o (?)
b = 0b11 # 3 - binary numbers - starting with 0b (?)

r = 2.3
print(a)
print(h)
print(o)
print(b)
print(r)

# Operators for numbers
a = 3
b = 4
c = 5.5
d = a + b
print(d) # 7
print(a+b) # 7
print(a+c) # 8.5
print(b/a) # 1.333
print(b//a) # 1 Floor division(->after division, give the result to the nearest whole number.)
print(a*c) # 16.5
print(a**b) # 81 (power sign)
print(17%3) # 2 (modulus)->shows the remainder after the division.

a += 7 # 10, is also same as 'a = a+7'
print(a)
a -= 2
print(a)

# pseudo Random number
import random # random function generates a random float number between 0.0 and 1.0 .
a = random.random()
print(a)
print(random.random())
print(random.random())

# Generating a random number list by using choice function.
import random
list = [1,2,3,4,5,6,7,8]
print(random.choice(list))

string = "Harry Potter"
print(random.choice(string))

# generating a random number using seeds.(?)
import random
random.seed(30)
print(random.random())
print(random.random())
print(random.random())

# Rolling Dice - randrange (?)
import random
print(1 + int(6 * random.random()))
print(random.randrange(1,7,(4)))

# Built-in-method
import random
rnd = random.random
print(rnd)
y = rnd()
print(y)
