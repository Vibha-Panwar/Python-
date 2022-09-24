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
"""
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
     