def add(a , b):
    print(f"Adding {a} + {b}")
    return a+b

def subtract(a , b):
    print(f"Subtracting {a} - {b}")
    return a-b


def multiply(a , b):
    print(f"Multiplying {a} * {b}")
    return a*b

def divide(a , b):
    print(f"Dividing {a} / {b}")
    return a/b
    
print("Let's do some math with just functions.")

age = add(15,30)
height = subtract(180,5)
weight = multiply(10,4)
iq = divide(200,2)

print(f"Age:{age} , Height:{height} , Weight:{weight} , IQ:{iq}")
print("Here is a puzzle.")

What = add(age,subtract(height , multiply(weight , divide(iq , 2))))
print("That becomes:",What,"Can you do it by hand?")