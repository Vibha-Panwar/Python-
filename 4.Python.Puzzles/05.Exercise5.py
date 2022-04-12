# https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-5.php
# Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings.

def test(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

str11 = ['a','abb','sfs','oo','de','sfde']
print("Original list:",str11)
print("check the nth-1 string is a proper substring of nth string in a given list.")
print(test(str11))

str12 = ['v','i','b','h','a','tae']
print("\ncurrent List:",str12)
print("check the function again on this list.")
print(test(str12))

str13 = ['cola','alpaca','kitten','horse','chimmy','tiger','bunny','double_bunny']
print("\nweird list:",str13)
print("try to find out whose name are those")
print(test(str13))



list1 = ['a','b','c','d','e','eedr']
def test(str1):
    return str1[4] in str1[5] and str1[4] != str1[5]

print("\noriginal list",list1)
print(test(list1)) 
