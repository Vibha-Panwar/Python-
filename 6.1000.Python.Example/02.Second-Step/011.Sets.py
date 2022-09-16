# Sets:--> Sets is one of the built-in function in python.
# 1-List, 2-Tuple, 3-Dictionary, 4-Sets
# It is collection of unordered,unchangeble and unindexed.
# It doesn't allow duplicate value.
# Sets items can be anythings.--integer, String, Boolean.
# We can even mix them up in a single set.
# List                  |  Tuple                 |  Sets               |  Dictionary          |
# Ordered               |  Ordered               |  Unordered          |  Ordered             |
# Changeble             |  Unchangeble           |  Unchangeble        |  Changeble           |
# Allow Duplicate value |  Allow Duplicate value |  No Duplicate value |  No Duplicate value  |

# Set Intersection :--> This function is used for selection of common items from 2 sets.
english = set(['door','car','lunar','era'])
spanish = set(['era','lunar','hola'])
print('english :', english)
print('spanish :', spanish)
both = english.intersection(spanish)
print(both)

# We can use "&" function also instead of intersection function. Both of the functions gives the same result.
again_both = english & spanish
print(again_both)


# Set Subset :--> "issubset" is a function which is used to find out a set is either a subset of another set or not.
english = set(('car','Bus','Door','era'))
spanish = set(('era','Door','hola'))
word = set(('Door','hola'))
print('issubset :', word.issubset(english))
print('issubset :', word.issubset(spanish))

# Set Symmetric Difference :--> symmetric_difference() is used to get the elements from the both of the sets but not the common ones.
english = set(('Door','Moon','Sun','House'))
spanish = set(('Sun','Moon','Hola'))

diff = english.symmetric_difference(spanish)
print('symatric_difference :', diff)

# Set Union :--> union() is used to merge two sets into one. It also removes the duplicate values. 
english = set(('Door','Moon','Sun','Mars','era'))
spanish = set(('era','Moon','Sun','Bus'))
all_the_words = english.union(spanish)
print(english)
print(spanish)
print(all_the_words)

# There is a symbol which we can use instead of union(). This symbol gives the same result as union() gives.
all_the_words = english | spanish
print(all_the_words)

# Set relative complement :-->
english = set(['Door','car','lunar','era'])
spanish = set(['era','lunar','hola'])
eng = english - spanish
spa = spanish - english

print(eng)
print(spa)
print(english)
print(spanish)

# We can use difference() too. It is similar to '-' operater.Both give the same results
spa1 = spanish.difference(english)
print(spa1)

# Set examples :-->
things = set(['table','chair','door','window','fan','tubelight'])
print(things)
print(things.__class__) #class is an object in python. python itself uses it for interprate the program. i.e. it is use class object to find out what kind of program we are typing.
print(things.__class__.__name__) # class__name__ will give the specific name after interprate it.
if 'table' in things:
    print("It has table.")
else:
    print("It has not.")

# Defining an empty set :-->
objects = set()
print(objects)

# Adding an element to a set(add) :-->
objects = set()
print(objects)

objects.add("Mars")
print(objects)
objects.add("venus")
print(objects)
objects.add("Saturn")
print(objects)

# Merging one set into another set(update) :-->
objects = set(['Mars','Jupiter','Saturn'])
internal = set(['Mercury','Venus','Earth','Mars'])
objects.update(internal)
internal.update(objects)
print(objects)
print(internal)

All = objects.union(internal)
print(All)
# There is a slite difference between union() and update(). Try to concentrate on this and don't get confuse on these little difference.
