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

# sort mixed :
mixed = [100,'fofo','fifi',42]
print(mixed)
mixed.sort
print(mixed)

# Key Sort :--> sort the list by the length of its value.
animals = ['chicken','cow','snail','elephant','ox','bee']
print(animals)
animals.sort()
print(animals)
animals.sort(key=len)
print(animals)
animals.sort(key=len, reverse=True)
print(animals)

# Sort Tuples :-->
students = [
    ('John','A',2),
    ('Zoro','B',3),
    ('Dave','C',1),
]
print(students)
print(sorted(students))
print(sorted(students, key=lambda s : s[1]))
print(sorted(students, key=lambda s : s[2]))

from operator import itemgetter
print(sorted(students, key= itemgetter(2)))

# sort with sorted :-->
animals = ['chicken','cow','snail','elephant']
print(animals)
s = sorted(animals)
print(s)
print(animals)
r = sorted(animals, reverse=True, key=len )
print(r)
print(animals)

# Difference between sort() and sorted()
# --> I didn't get this difference.

# Key sort with sorted
animals = ['bee','dog','fox','cat','fly','alk','yak','bat','eel',]
animals_in_abc = sorted(animals)
print(animals)
print(animals_in_abc)
animals_by_length = sorted(animals, key=len)
print(animals_by_length)

# Sorting characters of a string.
letters = 'axzb'
print(letters)
s = sorted(letters)
print(s)
print(letters)
r = ''.join(sorted(letters))
print(r)

# Range :
for i in range(11,18,2):
    print(i)

for i in range(5,7):
    print(i)

for i in range(3):
    print(i)

# Looping over index:
things = ['abc','def','ghi','jkl',34]
for var in things:
    print(var)

things = ['abc','def','ghi','jkl',34]
for i in range(len(things)):
    print(i,things[i])

# Enumerate list :-->
planets = ['mercury','venus','earth','mars','jupiter','saturn']
for idx, planet in enumerate(planets):
    print(idx,planet)


