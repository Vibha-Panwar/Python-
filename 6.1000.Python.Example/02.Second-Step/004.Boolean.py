# Boolean If Statement again
x = 2
if x == 2:
    print("It is 2.")
else:
    print("It is not 2.")

# True And False are real boolean values.
x = 3
v = x == 3
print(v)
if v:
    print(v,"is true-who would thought?")
v = x == 4
print(v)
if v:
    print(v,"is true - who would thought?")
else:
    print(v,"is false - who would thought?")

# boolean
x = 23
if x:
    print("23 is true.")
y = 0
if y:
    print("0 is true.")
else:
    print("0 is false.")

# True and False values in Python
# None, 0 , ""(empty String)
# False, [], {}, ()
# everything else is true.

values = [None, 0, "",False, [], {}, (), "0", True]
for v in values:
    if v:
        print("True value: ",v)
    else:
        print("False value: ",v)

# Comparision Operators
# == equal, != not equal, < less than, <= less than equal, > greater than, >= greater than and equal

a = "43"
b = 43
print(a == b)
print(a!= b)
print(b == 43.0)
print(None == None)
print(None == False)

# boolean operators
# and, or,not
#Boolean truth tables
# And Operator- true + true = true
#               true + false = false
#               false + true = false
#               false + false = false
# Or Operator - True + true = true
#               true + false = true
#               False + true = True
#               false + false = false 
# Not Operator - true = false
#                False = true

# Short Circuit
#def check_money():
 #   return money > 1000000
#def check_salary():
 #   salary +=1
  #  return salary >= 1000
#while True:
 #   if check_money() or check_salary():
  #      print("I can live well.")

# Short Circuit Fixed
#def check_money():
 #   return check_money > 1000000
#def check_salary():
 #   salary += 1
  #  return salary >= 1000
#while True:
 #   has_good_money = check_money()
  #  has_good_salary = check_salary()

#if has_good_money or has_good_salary:
 #   print("I can live well.")

# Exercise : Compare numbers
Q = input("Please enter in a string: ")
A = input("Please enter in another string: ")
print("How to compare?")
print("1) ASCII")
print("2) Length")
how = input()
if how == '1':
    first = Q > A
    second = Q < A
elif how == '2':
    first = len(Q) > len(A)
    second = len(Q) < len(A)

if first:
    print("First number is bigger.")
elif second:
    print("First number is smaller.")
else:
    print("They are equal.")