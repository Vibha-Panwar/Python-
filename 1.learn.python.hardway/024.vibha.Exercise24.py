print("It says we will do everything.")
print("Whatever we have done in previous exercises.")
print("In this single exercise")
print("First start with symboles that repersent\ nothing.\\ with this also.")
print("but if we give \n this then next line will be start and if we give \t then we find out there will be a little more Gap then usual.")

poem = ("""
\t I wanna be with you
   And I wanna stay with you
  Just like the stars shining bright
\t You're glowing once more
""")
print("""---------""")
print(poem)
print("***-----***")

multple_of_five = 50*2/5+10
print(f"This sould be thirty {multple_of_five}.")

def secret_formula(starting_point):
  Jelly_beans = start_point * 500
  Jars = Jelly_beans /100
  cracker = Jars + 100
  return Jelly_beans,Jars,cracker

start_point = 10000
beans,Jars,cracker = secret_formula(start_point)

print("with a starting point of: {}".format(start_point))
print(f"We have {Jelly_beans} beans , {Jars} Jars and {cracker}")

start_point = start_point /10
print("Can we do it in another way?")
formula = secret_formula(start_point)
print("we'd have beans {} and {} Jars and {} crackers.".formula(*formula))
