from sys import argv
from os.path import exists

script , from_file , to_file = argv
print(f"Copying from {from_file} to {to_file} .")

vibha1 = open(from_file)
vibha2 = vibha1.read()

print(f"Does the output file exist? {exists(to_file)}")

vibha3 = open(to_file , 'w')
vibha3.write(vibha2)

vibha3.close()
vibha1.close()