# Defining Simple Function :-->
#  We define a function with the word "def". After this give the name of the function.
# After name add parentheses and in the parentheses, give the list of the parameters.
# closed parentheses is followed by a colon ":".Then the body of the function is indented to the right.
# The depth of indentation does not matter but it must be the same for all the lines of the function.
# When we stop the indentation and start a new expression on the first column, that’s what tells Python that the function defintion has ended.

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
