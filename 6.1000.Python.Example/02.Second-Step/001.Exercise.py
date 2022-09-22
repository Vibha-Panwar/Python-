# Tarnary Operator
from tkinter import Y


def main():
    x = input('Give a number: ')
    if int(x) > 0:
        print("Number is positive.")
    else:
        print("Number is negative.")
main()

# There is no case and switch statement in Python.

# Exercise : Rectangular
def main():
    x = int(input('Length: '))
    y = int(input('width: '))

    Area = x * y
    print(Area)
main()

# Exercise: Calculator
def main():
    a = int(input("Give a number: "))
    b = int(input('Give another number: '))
    oper = input('Operator(+-*/): ')
    if oper == '+':
        response = a+b
    elif oper == '-':
        response = a-b
    elif oper == '*':
        response = a*b
    elif oper == '/':
        response = a/b
    else:
        print("Invalid operator:",format(oper))
        return
    print(response)
main()