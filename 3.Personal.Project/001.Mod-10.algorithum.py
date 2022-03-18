# CC = input("Enter a credit_card no:")
# CC = ['1','2','3','4','5','6','7','8','9']
# print("original list is :" + str(CC))

# for i in range(0, len(CC)):
  #  CC[i] = int(CC[i])

# print("Modified list is:" + str(CC))
# for f in cC:
#    print ("\n",cC[f])




C = ['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6']
def list_slice(s , step):
    return[s[i:: step] for i in range(step)]
print(list_slice(C,2))