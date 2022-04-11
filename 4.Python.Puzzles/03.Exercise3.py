# https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-3.php
# Write a Python program that accept an integer test whether an integer greater than 4^4
#  and which is 4 mod 34.
 
def test(n):
     return n % 34 == 4 and n > 4**4 

n = 922
print("Original number:")
print(n)
print("Now check whether the said integer is greater then 4^4 and get 4 as a reminder after dividing by 34.")
print(test(n))


n = 854
print("\noriginal number:")
print(n)
print("check the conditions again on the said integer.")
print(test(n))


n = 714
print("\n\tNew Integer:")
print(n)
print("Check if this integer fulfill the conditions.")
print(test(n))