from sys import argv
from os.path import exists

script , from_file , to_file = argv
print(f"Copying from {from_file} to {to_file} .")

vibha1 = open(from_file)
vibha2 = vibha1.read()

print(f"The input file is {len(vibha2)} bytes long.")
print(f"Does the output file exist? {exists(to_file)}")
print("Read, hit the RETURN to continue,CTRL-C to abort.")
input()

vibha3 = open(to_file , 'w')
vibha3.write(vibha2)

print("Alright, All Done!!")

vibha3.close()
vibha1.close()