# String - Anything you put in the double quotes or single quotes is called string. Otherwise python will try to find the meaning of the given text.
soup = "Spiced carrot & vegetable soup"
salad = "Fruit salad"
print(soup)
print(salad)

# Long Lines
text = "abc"  "def"
print(text)
other = "abcdef"
print(other)
long_string = "one" "two" "three"
print(long_string)
short_row = "one"\
    "two"\
        "three"
print(short_row)
longer_string = "first row second row third row"
print(longer_string)
shorter = "first line \
second line \
third line"
print(shorter)

# Triple Quotes Strings (multi-line)
# -> If you want to give multi line string then you have to put 3 quotes(single/double) on the both side of the text.
# Then answer will come in the same patterns as it was given in the string.
# As you already see if we put single quotes and give multi line text still the output will come in a single line.
text = """First Place
Second Place
Third Place"""
print(text)

# String length(len)
line1 = "Hello World"
hw = len(line1)
print(hw)
line2 = "hello everyone"
print(len(line2))

# String Repetition and Concatenation
# -> means we can multiply string too.and for the concatenation we can add two or more string together.
name = 2 * "Black"
print(name)
full_name = name + "Pink"
print(full_name)
title = "New song track-pink venom"
print(title)
print('=' * len(title))

# A character in a string
text = "winter bear"
a = text[0]
print(a)
b = text[8]
print(b)

# String slice
text = "hello world"
b = text[1:4] # [start,stop,gap] python never give last point in output instead it gives (last point -1) point
print(b)
print(text[2:])
print(text[:2])

# change a string
# In Python, strings are immutable. They never change.
# But we find a way-- How to change a string.
text = "abcd"
print(text)
text = text[:2] +'Y'+ text[3:]
print(text)

 # String Copy -> means the given value goes in different variable.that means it copy in different place.
text = "abcd"
print(text)
text = text + 'ef'
print(text)
other = text
print(other)
text = "xyz"
print(text)
print(other)

# String Functions and Methods (len,upper,lower)
a = "xYz"
print(len(a))
b = a.upper()
print(b)
print(a.lower())

# Index in String -> means it will count the place of the given input(it could be any world,letter)
text = "The golden cat climbed the green tree."
print(text.index("go"))
print(text.index("the"))
print(text.index("ee"))
# This index function count the white space too. So don't forget to count them too.
   
# index in string with range
text = "The golden cat climbed the green tree."
print(text.index("c"))
print(text.index("c",13))
print(text.index("be",15))
print(text.index("re",29))

# rindex in string with range
text = "The black cat climbed the green tree."
print(text.rindex("c"))
print(text.rindex("c",10))
print(text.rindex("c",3,15))
# rindex find the last occurrence of the specified value.
# string.rindex(value,start,stop)

# Find in string.
text = "The black dog is running behind a red car."
print(text.find("bl"))
print(text.find("car"))
print(text.find("cat"))
print(text.find("d"))
print(text.find("b",8))
print(text.find("re",10))
print(text.find("is",15,25))
# find function is similar to the rindex.It is also give you the last occurrence of specified value.
# The only difference is that if find function couldn't find the value then it will give the output as(-1) and rindex show an error in output.

# In string. -> checking a substring is in the string or not?
txt = "hello world"
if "wo" in txt:
    print('found wo')
if "x" in txt:
    print('found x')
else:
    print('Not found x')

# index if in string
sub = "cat"
txt = "The black cat climbed the gree tree."
if sub in txt:
    loc = txt.index(sub)
    print(sub + 'is at' + str(loc))
sub = "dog"
if sub in txt:
    loc = txt.index(sub)
    print(sub + "is at" + str(loc))
    