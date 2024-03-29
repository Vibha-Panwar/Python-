user = {}
user['name'] = 'Foobar'
print(user)

user['email'] = 'foo@bar.com'
print(user)

the_name =user['name']
print(the_name)

field = 'name'
the_value = user[field]
print(the_value)

user['name'] = 'Edit piaf'
print(user)

# Keys :-->
user ={
    'fname': 'Foo',
    'lname': 'Bar',
}
print(user)
print(user.keys())
# Keys are returned in seemingly random order.

# Loop over keys :-->
user = {
    'fname': 'Foo',
    'mname': 'min',
    'lname': 'Bar',
}
for k in user.keys():
    print(k)

for k in user.keys():
    print("{} -> {}".format(k,user[k]))

# Loop using items :-->
people = {
    'foo': '123',
    'bar': '456',
    'qux': '789'
}
for name,uid in people.items():
    print("{} => {}".format(name,uid))

user = {
    'fname': 'Foo',
    'mname': 'Fifi',
    'lname': 'Bar',
}
for t in user.items():
    print("{} => {}".format(t[0],t[1]))
    print("{} => {}".format(*t))

# Values :--> vaalues are returned in the random order as the keys.
user = {
    'fname': 'Harry',
    'mname': 'James',
    'lname': 'Potter'
}
print(user)
print(user.keys())
print(user.values())

# Not Existing Keys :-->
def main():
    user = {
        'fname': 'Lily',
        'lname': 'Potter',
    }
    print(user['fname'])
#    print(user['email'])
main()

# Get Key :--> If we use 'get' method to call the value, it works. 
# but if there is no key similar to the what we called, then we will get answer as 'None'.
# 'None' meaning according to boolean is 'False'.
user ={
    'fname':'Harry',
    'lname': 'Potter',
    'address': 'Cupboard under the stairs',
}
print(user.get("fname"))
print(user.get("lname"))
print(user.get("address"))
print(user.get("email"))
print(user.get("answer",42))

# Does the keys exist? :-->
user = {
    'fname': 'Foo',
    'lname': 'Bar',
}
print('fname' in user)
print('email' in user)
print('Foo' in user)
for k in ['fname','email','lname']:
    if k in user:
        print("{} => {}".format(k,user[k]))

# Does the value exist ? :-->
user = {
    'fname': 'FOFO',
    'lname': 'BABA',
} 
print('fname' in user.values())
print('FOFO' in user.values())

# Delete Key :-->
user = {
    'fname':'Harry',
    'lname':'Potter',
    'email': 'harry@potter.com'
}
print(user)
fname = user['fname']
del user['fname']
# print(user['fname'])
print(user)

lname_was = user.pop('lname')
print(lname_was)
print(user)

# List of Dictionaries :-->
people = [
    {
        'name': 'Foo Bar',
        'email': 'foo@example.com',
    },
    {
      'name': 'Qux Bar',
      'email': 'qux@example.com',
      'address': 'Any, Country',
      'Children': [
        'Alpha',
        'Beta',
      ]  
    }
]
print(people)
print(people[0]['name'])
print(people[1]['Children'][0])

# Shared Dictionary :-->
people = [
    {
        "name": "Fofo",
        "id": "1",
    },
    {
        "name": "Bar",
        "id": "2",
    },
    {
        "name": "Moo",
        "id": "3",
    }
]
by_name = {}
by_id = {}
for p in people:
    by_name[p['name']] = p
    by_id[p['id']] = p
print(by_name)
print(by_id)

print(by_name["Fofo"])
by_name["Fofo"]['email'] = 'fofo@example.com'
print(by_name['Fofo'])
print(by_id["1"])

#immutable numbers: numbers as dictionary key :-->
number = {
    23 : "Twenty Three",
    17 : "Seventeen",
    3.14 : "Three dot Fourteen",
    42 : "Fourty Two"
}

print(number)
print(number[17])
print(number.values( ))

# immutable collection : Tuple as dictionary Key
points = {}
p1 = (2,3)
points[p1] = 'Joe'
points[(17, 5)] = 'Jane'
print(points)
for k in points.keys():
    print(k)
    print(k.__class__.__name__)
    print(points[k])