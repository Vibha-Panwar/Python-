people = 30
samosa = 20
jalebi = 40

if samosa > people:
    print("There are so many samosas.")
elif samosa < people:
    print("All people can't have samosa.")
else:
    print("Can't decide what to give to the people.")

if jalebi > people:
    print("We will give jalebi to the people in dessert.")
elif people > jalebi:
    print("Can't give jalebi also to every people.")
else:
    print("Still can't decide.")

if samosa > jalebi:
    print("then we will give samosas to everyone.")
else:
    print("then we will give jalebi to everyone.")