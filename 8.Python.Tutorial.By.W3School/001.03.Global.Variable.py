# Variables that are created outside of a functionare known as global variables.
# Global Variable can used in both inside and outside of a function.
x = "awesome"
def myfun():
    print("Python is " + x)
myfun()
# Here we defind x variable outside of the function but used it in the function.

# Remember something -- if you defined the same variable inside the function with
# different value then it can be used only inside the function. It doesn't affect
# the value of global variable.
x = "awesome"
def myfun():
    x = "fantastic"
    print("Python is " + x)
myfun()
print("Python is " + x)

## The Global Keyword :
# If you want to define global variable but remember it in the middle of the function
# then you do not need to go all the way up/starting of the program. You can define 
# Global variable in the middle of the function by using "Global Keyword".
def myfun():
    global x
    x = "fantastic"
myfun()
print("Python is " + x)

# You can use this global keyword to change the value of the global variable.
x = "Awesome"
def myfun():
    global x
    x = "fantastic"

myfun()
print("Python is " + x)
