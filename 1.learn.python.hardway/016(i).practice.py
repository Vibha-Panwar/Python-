from sys import argv
script , file_name = argv

print("opening the file....")
ABC1 = open(file_name , 'w')

print("Now I'm going to ask you some questions.")
question1 = input("what is your name : ")
question2 = input("how old are you : ")
question3 = input("where do you live : ")

print("I am going to print this into a file.")
ABC1.write(question1)
ABC1.write(question1)
ABC1.write("\n")
ABC1.write(question2)
ABC1.write("\n")
ABC1.write(question3)
ABC1.write("\n")

print("and, we are finally closing it.")
ABC1.close()
