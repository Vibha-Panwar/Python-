# for-in loop - to iterate over a well defined list of values.
# while loop - repeate an action till some condition is met.
# for-in loop on strings.
txt = "hello everyone"
for b in txt:
    print(b)

# for-in loop on list.
fruit = ["apple", "banana", "orange", "papaya","peach"]
for a in fruit:
    print(a)

# for-in loop on range.
for i in range(3,8):
    print(i)

# for-in loop with early end using break.
txt = "hello world"
for c in txt:
    if c == " ":
        break
    print(c)

# for-in loop skipping parts using continue.
txt = "hello everyone"
for c in txt:
    if c == " ":
        continue
    print(c)

# for-in loop with break and continue
txt = "hello world"
for abc in txt:
    if abc ==  " ":
        continue
    if abc == "o":
        break
    print(abc)
print("Done")

# While loop
import random
total = 0
while total <= 100:
    print(total)
    total += random.randrange(20)

# infinite while loop
#import random
#total = 0
#while total >= 0:
 #   print(total)
  #  total +=random.randrange(26)
#print("done")

# while with complex expression
import random
total = 0
while (total <1000) and (total % 17 != 2):
    print(total)
    total += random.randrange(25)
print("done")

# while with break
import random
total = 0
while total<10000000:
    print(total)
    total += random.randrange(20)

    if total % 17 == 1:
        break
    if total **2 % 23 == 7:
        break
print("Done")

# while True
import random
total = 0
while True:
    print(total)
    total += random.randrange(20)
    if total >= 10000000:
        break
    if total % 17 == 1:
        break
    if total **2 % 23 == 7:
        break
print("done")

# Duplicate input call
id = input("Type in your ID: ")
while len(id) != 9:
    id = input("Type in your ID: ")
print("your id is" + id)

# Eliminate dublicate input call
while True:
    id = input("Type in your ID: ")
    if len(id) == 9:
        break
print("Your id is " + id)

# Do while loop
while True:
    answer = input("What is the meaning of life?")
    if answer == "25":
        print("Yeeah,that's it!")
        break
print("Done")

# while with many continue calls
#while True:
 #   line = get_next_line()
  #  if last_line:
   #     break
   # if line_is_empty:
    #    continue
    #if line_has_a_hash_at_the_beginning:
     #   continue
    #if line_has_two_slash_at_the_beginning:
     #   continue

# Exit -> It will stop ur program no matter where you call it.
# return -> It will return from a function(it will stop the specific function).
# break -> it will stop the current "while" or "for" loop
# continue -> it will stop the current iteration of the current "while" or"for" loop

# Exercise : Print all the locations in a string.
# solution->
text = "The black cat climbed the green tree."
start = 0
while True:
    loc = text.find("c",start)
    if loc == -1:
        break
    print(loc)
    start = loc + 1