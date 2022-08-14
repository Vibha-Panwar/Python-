import sys
print(sys.executable)
print(sys.platform)
print(sys.argv[0])
print(sys.version_info.major)

print(sys.getsizeof(2))
print(sys.getsizeof(50))
print(sys.getsizeof(3.5))

print(sys.getsizeof(""))
print(sys.getsizeof("z"))
print(sys.getsizeof("hello"))
print(sys.getsizeof("hello world"))

# A Main Function
def main():
    print("Hello")
    print("World")
print("Before")
main()
print("After")

# Print Function in Python3
print("Hello",end=" ")
print("World")
print("Foo","Bar")
# end will set the next character added at the end of each print statement.

print("Hello",end=" ")
print("World")
print("Foo","Bar","Moon",sep=" ")
print("Sun")

# Prompting for user input in Python3
def main():
    print("We have a question?")
    name = input("your name : ")
    print("hello" + name + ",How are you ?")
main()
# Add number enter by the user
def main():
    a = input("First Number : ")
    b = input ("Second Number : ")
    print(a + b)
main()
# Input function take value as a string. No matter what, You give value as a number or words, 
# Addition (+) function will add those value as string addition. ex- a=1,b=2,a+b = 12

# Add number enter by user (fixed)
def main():
    a = input("First Number : ")
    b = input("Second Number : ")
    print(int(a)+int(b))
main()
# How can I check If a string can be converted to a number ?
val = input("Type in a number : ")
print(val)
print(val.isdecimal())
print(val.isnumeric())
if val.isdecimal():
    num = int(val)
    print(num)
# convert string to integer.
a = "23"
print(a)
print(type(a))

b = int(a)
print(b)
print(type(b))
# Converting float to integer.
a = 2.3
print(type(a))
print(a)
b = int(2.3)
print(type(b))
print(b)

a ="2.3"
print(type(a))
print(a)
#b = int(a)
#print(b)
#print(type(b))

a = "2.1"
b = float(a)
c = int(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
d = int(float(a))
print(d)
print(type(d))
print(int(float(2.1)))
print(int(float("2")))
print(int(float(2)))