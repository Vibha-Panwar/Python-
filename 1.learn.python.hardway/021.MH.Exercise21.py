def add(a,b):
    print(f"Adding {a} + {b}")
    return a+b

def subtract(a,b):
    print(f"Subtract {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"Multiplying {a}*{b}")
    return a*b

def module(a,b):
    print(f"Module {a}%{b}")
    return a%b

print("Let's do some math with the functions we defined above.")
Age = add(10,10)
weight = subtract(70,10)
height = multiply(83,5)
IQ = module(200,3)
print(f"Age: {Age},weight: {weight}, height: {height} and IQ: {IQ}")

puzzle = add(Age,subtract(weight,multiply(height,module(IQ,2))))
print("Can you solve it by hand.")
print(puzzle)