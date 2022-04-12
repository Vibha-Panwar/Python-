# www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-6.php
# Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another.
#  Return true or false.

def test(li):
    return all(i in range(1000) and abs(i - j) >= 5 for i in li for j in li if i != j) and len(set(li)) == 100
nums = list(range(0, 1000, 10))
print("Original number:",nums)
print("Check whether the given list contain integer between 0 and 999 which all differ by 10 from one another.")
print(test(nums))

L1 = list(range(0, 999, 10))
print("\noriginal list:",L1)
print("check the list again.")
print(test(L1))