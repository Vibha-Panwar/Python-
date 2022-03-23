print("Let's practice everthing.")
print("You\'d need to know \' bout escape with \\ that do:")
print("\n next line and \t tabs.")

poem = """
\t The lovely World
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intuition
and requires explanation
\n\t where there is none."""

print("------------------")
print("poem")
print("--------------------")

five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans / 1000
    crates = jars/100
    return jelly_beans , jars , crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

# remember that this is just another way to format a string.
print("with a starting point of: {}".format(start_point))

# it is just like with an f"" string.
print(f"we 'd have {beans} beans , {jars} jars and {crates} crates.")

start_point = start_point / 10

print("We can do that in this way:")
formula = secret_formula(start_point)

# this is an easy way to apply a list to a format string.
print("We'd have {} beans , {} jars , {} crates.".format(*formula))
  