# Format sprintf
age = 42.12
name = 'stars'
str_concatenate = "The user " + name + " was born " + str(age) + " years ago."
print(str_concatenate)

str_percentage = "The user %s was born %s years ago." % (name,age)
print(str_percentage)

str_format = "The user {} was born {} years ago.".format(name,age)
print(str_format)

str_f_string = f"The user {name} was born {age} years ago."
print(str_f_string)

# Example using format - indexing
txt = "Kim younjong"
num = 25
print("The user {} was born {} years ago." . format(txt,num))
print("The user {0} was born {1} years ago." . format(txt,num))
print("The user {1} was born {0} years ago." . format(num,txt))
print("{0} is {1} years old." . format(txt,num))

# Example using format with names
txt = "Foo Bar"
num = 2019
print("The user {name} was born in {age} year." . format(name=txt, age=num))

# Format columns
data = [["abc",12],["def",23],["ghi",34],["jkl",45],["mno",56]]
for entry in data:
    print("{} {}".format(entry[0],entry[1]))
print('-' * 19)

for entry in data:
    print("{:<4}|{:>3}".format(entry[0], entry[1]))

# Example using format - alignment
txt = "Some random text"
print("'{}'".format(txt))
print("'{:20}'".format(txt))
print("'{:<20}'".format(txt))
print("'{:>20}'".format(txt))
print("'{:^20}'".format(txt))

# format string
name  = "Txt group"
print("{:s}".format(name))
print("{}".format(name))

# Format characters and types
Q = 23
print("{:b}".format(Q))
print("{:c}".format(Q))
print("{:d}".format(Q))
print("{:o}".format(Q))
print("{:x}".format(Q))
print("{:n}".format(Q))
print("{}".format(Q))

# Format floating point number
x = 412.345678901
print("{:e}".format(x)) # exponent
print("{:E}".format(x)) # Exponent
print("{:f}".format(x)) # fixed point
print("{:.2f}".format(x)) # fixed point(only 2 point after decimal)
print("{:F}".format(x)) # same as f
print("{:g}".format(x)) # generic: only 3 points after decimal
print("{:G}".format(x)) # same as g
print("{:n}".format(x)) # number: same as generic
print("{}".format(x))

# f-strings(format string literals)
name = "KTHV"
age = 27
pi = 3.141592653589793
r = 2
print(f"The user {name} was born {age} years ago.")
print(f"The user {name:10} was born {age} years ago.")
print(f"The user {name:>10} was born {age} years ago.")
print(f"The user {name:>10} was born {age:>10} years ago.")
print(f"PI is {pi:.3}.")
print(f"PI is '{pi:.3f}'.")
print(f"Area is {pi*r**2}")
print(f"Area is {pi*r**2:.3f}")

# print using old %- syntex (????????????)
# Format braces, brackets and parentheses

print("{{{}}}".format(42))
print("{{ {} }}".format(42))
print("[{}] ({})".format(42,42))
print("%{}".format(42))

# Example - using format with attributes of objects

import sys
print("{0.executable}".format(sys))
print("{system.argv[0]}".format(system = sys))

# raw f-string
name = "foofoo"
print(r"a\nb {name}")
print(rf"a\nb {name}")
print(fr"a\nb {name}")