# In this Exercise, We learn the counting in List and do some practice in zig zag mode.
# So that we can understand it in better way and get some confidence.

List1 = [10,20,30,40,50,60]
List2 = [70,80,90,100,110]
# So, here we have 2 list which have some numbers in them.

print("what number is on the position of second place in List1?")
print(List1[1])
print("What number is on the position of fifth place in List2?")
print(List2[4])

# Now we are going to try some math on ours Lists.

print(List1[2]+List2[0])
print(List2[4]-List1[5])
print(List1[0]*List2[3])
print(List2[3]/List1[1])
print(List2[4]%List1[1])
# Till here Everything is going smoothly.

print("Let's try it in backward direction. Then we will see howmuch you get it.")

print(List2[-1]-List1[-1])
print(List1[-4]+List2[-3])

print("Did you see what we do above?\nlet me explain it now.\nIf we count the List numbers from left to right then counting start from zero.")
print("But if we start counting reversly means from right to left\nThen counting start with (-1) not from zero.")