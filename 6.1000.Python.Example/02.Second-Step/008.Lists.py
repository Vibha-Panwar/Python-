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
a = ['x','2','y']
b = ['x',2,'y']
print(":".join(a))
# print(":".join(b))
print(":".join(map(str,b)))
# map() :--> map function give us output after appling the  given function on given variable.
# map(functionwhich you want to apply,variable on which function will apply) 
print(":".join(str(xyz) for xyz in b))


# Split Function:
# *Special Case :--> To split a string to its characters: Use the list() function.

words = "ab:cd:ef:gh"
wor_split = words.split(':')
print(wor_split)

# Split by space.
names = "bheem   chutki   Dholu  Bholu  indumati"
naam = names.split( )
print(naam)

# split to characters
chars = list("indu dholu")
print(chars)

# re.split() --> ??

# for loop on lists:
things = ['apple','banana','peach',23]
for var in things:
    print(var)
# here var means variable means anything which is present in things will be printed.

# in list
words = ['apple','banana','peach','42']
if 'apple' in words:
    print('found apple')
if 'a' in words:
    print("found a")
else:
    print("NOT found a")
if 42 in words:
    print("found 42")
else:
    print("NOT found 42")

# Where is the element in the list
words = ['cat','dog','bee','bug','rat','owl']
print(words.index("rat"))
print(words.index("dog"))

# index improved
words = ['cat','dog','owl','bee']
name = 'owl'
if name in words:
    print(words.index(name))
name = 'python'
if name in words:
    print(words.index(name))

# [].insert function: --> This function is used to insert specific value at the specific place.
# list.insert(positiion,element) ; element could be any string, number, object.
words = ['apple','banana','carrot','dragon']
print(words)
words.insert(2,'zebra')
print(words)
words.insert(0,20)
print(words)

# [].append function --> This method is also used to add add new item in the list but that element will always add at the end of the list.
# list.append(element)
names = ['fofo','fifi','bumbalbi','magnito','kim']
print(names)
names.append("KTH")
print(names)

# [].remove function -->It used to remove element from the list but it will remove first entry of the given element.
# If there is another same element then it will remain same. If you want to remove all the given element to remove then you have use loop function.
names = ['fofo','fifi','bumbalbi','magnito','kim']
print(names)
print(names.remove('kim'))
print(names)
names = ['fofo','fifi','bumbalbi','kim','magnito','kim']
print(names)
while 'kim' in names:
    names.remove('kim')
print(names)

# remove element by index[].pop function --> It is a simple method don't feel it is hard to understand.
# just give specific value to pop function and it will delete it.

planets = ['mercury','venus','earth','mars','jupiter']
print(planets)
third = planets.pop(2)
print(third)
print(planets)
second = planets.pop(0)
print(planets)
last = planets.pop()
print(last)
print(planets)

# Remove several elements of list by index :-->
names = ['fofo','fifi','baz','moo','mua','qux']
names[2:4] = []
print(names)

# Use list as a Queue :-->
a_queue = []
print(a_queue)
a_queue.append('Moo')
print(a_queue)
a_queue.insert(0,'zebra')
print(a_queue)
first = a_queue.pop(0)
print(first)
print(a_queue)

#Queue using deque from collections
from collections import deque
items = deque(['fofo','fifi'])
print(type(items))
print(items)
items.append('zozo')
print(items)
print(len(items))
items.append('coco')
print(items)

txt = items.popleft()
print(txt)
print(items)
print(len(items))

# Fixed size queue:- means giving the max length of the deque.
from collections import deque
queue = deque([],maxlen = 3)
print(len(queue))
print(queue.maxlen)
queue.append("Foo")
queue.append("Bar")
queue.append("Baz")
print(queue)
queue.append("Zoo")
print(queue)
# Here note one thing -- when we give maxlength to deque and append a lot of number
# or string in the list then deque will contain only the latest one. It will leave the elements from the left side of the list.

# List as a stack
stack = []
stack.append("Joe")
print(stack)
stack.append("Jane")
print(stack)
stack.append("Bob")
print(stack)
while stack:
    name = stack.pop()
    print(name)
    print(stack)

# Stack with deque
from collections import deque
stack = deque()
stack.append("Joe")
stack.append("Jane")
stack.append("Bob")
while stack:
    name = stack.pop()
    print(name)
    print(stack)

# Exercise : Queue
# It will prompt the user for a new name by printing :, the user can type in a name and press ENTER. The app will add the name to the queue.
#If the user types in “n” then the application will remove the first name from the queue and print it.
#If the user types in “x” then the application will print the list of users who were left in the queue and it will exit.
#If the user types in “s” then the application will show the current number of elements in the queue.

# Solution : Queue with List
queue = []
while True:
    inp = input(":")
    inp = inp.rstrip("\n")

    if inp == 'x':
        for name in queue:
            print(name)
        exit()
    if inp == 's':
        print(len(queue))
        continue
    if inp == 'n':
        if len(queue) > 0:
            print("next is {}".format(queue.pop(0)))
        else:
            print("The queue is empty")
        continue
    queue.append(inp)

# Solution : Queue with deque
from collections import deque
queue = deque()
while True:
    inp = input(":")
    inp = input.rstrip("\n")
    if inp == "x":
        for name in queue:
            print(name)
        exit()

    if inp == "s":
        print(len(queue))
        continue
    if inp == "n":
        if len(queue) > 0:
            print("next is {}".format(queue.popleft()))
        else:
            print("The queue is empty.")
        continue
    queue.append(inp)        