# Copy-Paste Code :-->
"""
a = [2, 3, 93, 18]
b = [27, 81, 11, 35]
c = [32, 103, 11]

total_a = 0
for v in a:
    total_a += v
print("sum of a : {} average of a : {}".format(total_a, total_a / len(a)))

total_b = 0
for v in b:
    total_b += v
print("sum of b : {} average of b : {}".format(total_b, total_b / len(b)))

total_c = 0
for v in c:
    total_c += v
print("sum of c : {} average of c : {}".format(total_c, total_c / len(c)))

### Again Copy - Paste Code fixed :-->
a = [2, 3, 93, 18]
b = [27, 81, 11, 33]
c = [32, 104, 1]
def calc(numbers):
    total = 0
    for v in numbers:
        total += v
    return total, total/len(numbers)
total_a, avg_a = calc(a)
print("Sum of a: {} average of a: {}".format(total_a, avg_a))

total_b, avg_b = calc(b)
print("Sum of b: {} average of b: {}".format(total_b, avg_b))

total_c, avg_c = calc(c)
print("Sum of c: {} average of c: {}".format(total_c, avg_c))

### Copy paste code further improvement :-->
data = {
    'a' : [2, 3, 54, 178],
    'b' : [27, 81, 11, 36],
    'c' : [32, 103, 1] 
} 
def calc(numbers):
    total = 0
    for v in numbers:
        total += v
    return total, total/len(numbers)
total = {}
avg = {}
for name, numbers in data.items():
    total[name], avg[name] = calc(numbers)
    print("Sum of {} : {} average of {} : {}".format(name,total[name],name,avg[name]))

### Palindrome :-->
def is_palindrome(s):
    if s == '':
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False
def iter_palindrome(s):
    for i in range(0, int(len(s)/2)):
       if s[i] != s[-(i+1)]:
        return False
    return True

print(is_palindrome(''))
print(is_palindrome('a'))
print(is_palindrome('ab'))
print(is_palindrome('aba'))
print(is_palindrome('abba'))
print(is_palindrome('abcba'))

print(iter_palindrome(''))
print(iter_palindrome('a'))
print(iter_palindrome('ab'))
print(iter_palindrome('aa'))
print(iter_palindrome('abc'))
print(iter_palindrome('aba'))
print(iter_palindrome('abba'))
""" 
### Exercise :--> Write a function that will accept any number of numbers and return a list of values:

# The sum  ## Statics, Recursive, Tower of hanoi, Merge and bubble sort.
# Average
# Minimum
# Maximum 
