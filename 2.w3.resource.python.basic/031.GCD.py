# https://www.w3resource.com/python-exercises/python-basic-exercise-31.php
# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(x , y):
    gcd = 1
    if x % y == 0 :
        return y
    for k in range(int (y),0,-1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

print("GCD of 12& 17 =", gcd(12,17))
print("GCD of 4&6 = ",gcd(4,6))
