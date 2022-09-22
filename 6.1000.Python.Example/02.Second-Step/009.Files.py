# Open and read file :-->
"""
### Printing  File Lines ###

filename = 'D:\\Example\\numbers.txt'
with open(filename, 'r') as fh:
    for line in fh:
        print(line)


# Filename on the command Line :-->
import sys
def main():
    if len(sys.argv) != 2:
        exit("usage : " + sys.argv[0] + " Filename ")
    filename = sys.argv[1]
    with open(filename) as fh:
        print("Working on the file", filename)
        for line in fh:
            print(line)
main()


# Filehandle with or without :-->
filename = 'D:\\Example\\numbers.txt'
fh = open(filename, 'r')
print(fh)
data = fh.read()
fh.close()
print(fh)

with open(filename, 'r') as fh:
    print(fh)
    data = fh.read()
print(fh)


## Filehandle with return :-->
import sys
def process_file(filename):
    with open(filename, 'r')as fh:

        for line in fh:
            line = line.rstrip("\n")
            if len(line) > 0:
                if line[0] == "#":
                    return

            if len(line) > 1:
                if line[0:2] == "//":
                    return
            print(line)
process_file(sys.argv[1])



# Read all the lines into a list :-->
filename = 'D:\\Example\\numbers.txt'
with open(filename, 'r') as fh:
    lines_list = fh.readlines()
print(lines_list) 
print(len(lines_list))
for line in lines_list:
    print(line)

## Read all the characters into a string(slurp):-->
filename = "D:\\Example\\numbers.txt"
with open(filename, 'r') as fh:
    lines_str = fh.read()
print(lines_str)
print(len(lines_str))
"""
"""
## Open file exception handling :-->
filename = 'D:\\Example\\numbers.1.txt'
try:
    with open (filename,'r') as fh:
        lines = fh.read()
except Exception as err:
    print('There was some error in the file operations.')
    print(err)
    print(type(err).__name__)

print("Still running.")
"""

## Open many files -exception handling :-->
import sys
def main():
    for filename in sys.argv[1:]:
        try:
            with open (filename) as fh:
                total = 0
                count = 0
                for line in fh:
                    number = float(line)
                    total += number
                    count += 1
                print("Average:", total/count)
        except Exception:
            print("trouble with {} ".format (filename))

main ()
