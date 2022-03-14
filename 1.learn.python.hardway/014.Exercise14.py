from sys import argv

script , user_name = argv
prompt = '<3'

print(f"Hi {user_name} , I am the {script} script.")
print("I would like to ask some questions.")
print(f"Do you like me {user_name} ?")
like = input(prompt)

print(f"Where do you live {user_name} ?")
live = input(prompt)

print("What kind of computer you have ?")
computer = input(prompt)

print(f"""
Alright,so you said {like} about liking me.
you live in {live}. Not sure where that is.
And you have a {computer} computer. Nice.
""")