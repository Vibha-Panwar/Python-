# Defining Simple Function :-->
#  We define a function with the word "def". After this give the name of the function.
# After name add parentheses and in the parentheses, give the list of the parameters.
# closed parentheses is followed by a colon ":".Then the body of the function is indented to the right.
# The depth of indentation does not matter but it must be the same for all the lines of the function.
# When we stop the indentation and start a new expression on the first column, that’s what tells Python that the function defintion has ended.
"""
def add(x, y):
    z= x + y
    return z
a = add(10, 2)
print(a)
q = add(23, 4)
print(q)

# Defining a function :-->
def sendmail(From, To, Subject, Content):
    print('From :', From)
    print('To :', To)
    print('Subject :', Subject)
    print('')
    print('Content :', Content)
    print(Content)
    
sendmail('abc','def', 'xyz', 'lmnop')

## Parameter can be named :-->
def sendmail(From, To, Subject, Content):
    print('From :', From)
    print('To :', To)
    print('Subject :', Subject)
    print('')
    print(Content)

sendmail(
    Subject = 'self message',
    Content = 'Has some content too',
    From = 'gaasdf',
    To = 'fdfgafg',
)
"""
"""
## Mixed positional and named parameter :--> We can not mix them, choose either one.
def sendmail(From, To, Subject, Content):
    print('From', From)
    print('To', To)
    print('Subject', Subject)
    print('')
    print(Content)

sendmail(
    Subject = 'dfgadaf',
    Content = 'bdrytjry',
    To = 'sdgh.com',
    'sdfsgdgg.com',
)

## Default Values :-->
def prompt(question, retry=3):
    while retry > 0:
        inp = input('{} ({}) :'.format(question, retry))
        if inp == 'my secret':
            return True
        retry -= 1
    return False
print(prompt("Type in your password"))
print(prompt("Type in your password", 1))

### Several defauls, using names :-->
# The parameter  with default value must come at the end of the parameter declartion.
def f(a, b=2, c=3):
    print(a, b, c)
f(1)
f(1, b=0)
f(1, c=5)
f(1, c=5, b=0)
# f(b=0, 1)

## Arbitrary number of arguments :-->
def mysum(*numbers):
    print(numbers)
    total = 0
    for s in numbers:
        total += s
    return total
print(mysum(1))
print(mysum(1,2))
print(mysum(1,2,4,5))
x = [2, 3, 4, 5]
print(mysum(*x))

### Fixed parameters befor the others :-->
def mysum(op, *numbers):
    print(numbers)
    if op == '+':
        total = 0
    elif op == '*':
        total = 1
    else:
        raise Exception('invalid operator {}'.format(op))

    for s in numbers:
        if op == '+':
            total += s
        elif op == '*':
            total *= s
    return total
print(mysum('+',1))
print(mysum('+',1,2))
print(mysum('*',3,4,5))
print(mysum('+',3,4,7,8))
print(mysum('%',2,4))

### Arbitrary key-value paris in parameters :-->
def f(**kw):
    print(kw)
f(a=23, b=12)

### Extra key-value pairs in parameters :-->
def f(name, **kw):
    print(name)
    print(kw)
f(name="Fofo",a=2, b=4)


## Every parameter option :-->
def f(op, count = 0, *things, **kw):
    print(op)
    print(count)
    print(things)
    print(kw)
f('+',3,4,6,5,a=23,b=34)
"""
