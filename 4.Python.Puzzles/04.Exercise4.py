# https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-4.php
# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. 
# If n is odd, all piles have an odd number of stones.Each pile must more stones than the previous pile but as few as possible. 
# Write a Python program to find the number of stones in each pile.

def test(n):
    return [n+2 * i for i in range (n)]

n = 2
print("No. of pile:",n)
print("No. of stones in each pile are:")
print(test(n))

n = 10
print("No. of pile:",n)
print("No. of stones in every pile are:")
print(test(n))

n = 9
print("No. of piles:",n)
print("No of stones in every piles are:")
print(test(n))