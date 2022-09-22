from sys import argv
from os.path import exists

script , from_file , to_file = argv
print(f"Copying from {from_file} to {to_file} .")

para1 = open(from_file)
para2 = para1.read()

print(f"Does the output file exist? {exists(to_file)}")

para3 = open(to_file , 'w')
para3.write(para2)

para3.close()
para1.close()