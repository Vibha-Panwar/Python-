# Format sprintf
age = 42.12
name = 'stars'
str_concatenate = "The user " + name + " was born " + str(age) + " years ago."
print(str_concatenate)

str_percentage = "The user %s was born %s years ago." % (name,age)
print(str_percentage)

str_format = "The user {} was born {} years ago.".format(name,age)
print(str_format)

str_f_string = f"The user {name} was born {age} years ago."
print(str_f_string)

# Example using format - indexing
txt = "Kim younjong"
num = 25
print("The user {} was born {} years ago." . format(txt,num))
print("The user {0} was born {1} years ago." . format(txt,num))
print("The user {1} was born {0} years ago." . format(num,txt))
print("{0} is {1} years old." . format(txt,num))

# Example using format with names
txt = "Foo Bar"
num = 2019
print("The user {name} was born in {age} year." . format(name=txt, age=num))

# Format columns
data = [["abc",12],["def",23],["ghi",34],["jkl",45],["mno",56]]
for entry in data:
    print("{} {}".format(entry[0],entry[1]))
print('-' * 19)

for entry in data:
    print("{:<4}|{:>3}".format(entry[0], entry[1]))

# Example using format - alignment

