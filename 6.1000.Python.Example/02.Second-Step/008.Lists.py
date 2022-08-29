# Layout of the Lists:
# -> Layout is flexible.
more_stuff = [
    23,
    2.34,
    True,
    None,
    "Foo Foo",
    ['another','string'],
    {
        'a':'Dictionary',
        'Language': 'Python',
    },
]
print(more_stuff)

# Lists --> *Access single element : [INDEX]
# * Access a sublist : [Start:End]
# * Create a copy of that sublist.

planets = ['Mercury','venus','Earth','Mars','jupiter','Saturn']
print(planets)
print(len(planets))

print(planets[0])
print(type(planets[2]))
print(planets[0:3])
print(type(planets[0:2]))
print(planets[1:4])
print(planets[2:])
print(planets[:3])
print(planets[:])

#list slice with steps --> [start:end:step]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
print(letters[::])
print(letters[::1])
print(letters[::2])
print(letters[1::2])
print(letters[2:9:2])
print(letters[1:20:3])
 
# Change a list ->
x = ['abc','def','ghi','jkl']
x[0] = 'pqr'
print(x)
x[1:3] = ['xyz','123']
print(x)
x[1:3] = ['dog']
print(x)
x[1:2] = ['cat','ant']
print(x)
x[1] = ['pig','rat','bee','house-fly']
print(x)
# unlike strings, Lists are mutable. You can change the content of a list.
# We can use slice notation to change several elements at once.
# we can even have different number of elements in the slice and in the replacement.
# This will change the lenght of an array.

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(numbers)
numbers[1::2] = [0,0,0,0,0,0,0]
print(numbers)

# List assignment and list copy
x = ['apple','bob','cat','donkey']
y = x
x[0] = 'pqr'
print(x)
print(y)

# If you relley want a copy the pythonic way is to use the slice syntax.
# It creates a shallow copy.

x = ["apple",'battle','cattle','drown','endless']
y = x[:]
x[0] = 'attack'
x[2] = 'castle'
print(x)
print(y)

# Deep Copy
from copy import deepcopy
x = ['apple','boy','cat','dog']
y = deepcopy(x)
x[0] = 'qwe'
print(x)
print(y)

# Join Function --> join method takes all the items of a list, tuple and joins them into a string.

fields = ['one','two and three','four','five']
together = ' : '.join(fields)
print(together)
mixed = '-=<> '.join(fields)
print(mixed)
another = ' '.join(fields)
print(another)

# join list of numbers
a = ['x','y','2']
