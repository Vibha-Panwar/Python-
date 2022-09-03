# Implement a Reverse Polish Calculator

#1 2,
#2 3,
#3 4
#4 +
#5 *
#6 =
#7 14

# Soltion- Reverse Polish calculator(stack) with List.
stack = []
print("x = eXit,s = Show,[+,-,*,/,=]")
while True:
    val = input("Enter any number :")
    if val == 's':
        print(stack)
        continue
    if val == 'x':
        break
    if val == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
        continue
    if val == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a-b)
        continue
    if val == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
        continue
    if val =='/':
        a = stack.pop()
        b = stack.pop()
        stack.append(a/b)
        continue
    if val == '=':
        print(stack.pop())
        continue
    stack.append(float(val))

# Solution -- Reverse polish calculator (stack) with deque
from collections import deque
stack = deque()
while True:
    val = input("give a number : ")
    if val == "x":
        break
    if val == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
        print(stack)
        continue
    if val == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
        print(stack)
        continue
    if val == '=':
        print(stack.pop())
        continue
    stack.append(float(val))

# Debugging Queue :

# SORT FUNCTION
# sort() :--> This function sort the list in ascending order by default.
# list.sort(reverse = True|False, key = myfunc)
# By default reverse = False :-> means list will change in ascending order.
# If we change it into True then list will change in decending order.
# key :-> a function to specify the sort criteria.

planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn']
print(planets)
planets.sort()
print(planets)
planets.sort(reverse=True)
print(planets)

# Sort Numbers :
numbers = [7,2,-4,19,8]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort(key=abs, reverse=True)
print(numbers)

