# Exercise : Count Digits
# Given a list of numbers numbers = [1203, 1256, 312456, 98],
# count how many times each digit appears?






# [].extend :--> By this function we can add more than one word in the list. 
names = ['FoFo Bar','Orgo Morgo']
names.extend(['Joe Doe','Jane Dol'])
print(names)

# append vs extend :-->
names = ['fofo Bar','Orgo Morgo']
more = ['Joe Doe','Jane Doe']
names.extend(more)
print(names)

names.append(more)
print(names)

names = ['foo','Bar']
names.append('qwe')
print(names)

names = ['Foo','Bar']
names.extend('qwe')
print(names)

# split and extend :-->
lines = [
    'abc def ghi',
    'hello world',
]
collector = []
for l in lines:
    collector.extend(l.split())
    print(collector)