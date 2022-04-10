def ghost_room():
    print("There is a ghost here.")
    print("that ghost standing infront of another gate.")
    print("How are you going to move that ghost?")

    while True:
        choice = input("> ")

        if choice == "talk with it":
            print("It will tell you about your future girlfriend.")
        elif choice == "tease it":
            dead("it will slap your face off.")
        elif choice == "worship the God.":
            print("ghost vanish in thin air. Now you can leave this room easily.Good Job!!!")
            exit(0)
        else:
            print("I don't know what that mean.")

def lion_room():
    print("Here is a big strong lion.")
    print("How are you going to move that lion from another door so that you can left that room alive???")
    

    while True:
        choice = input("> ")

        if choice == "stand like a statue.":
            dead("lion come to you then kick you and pill your skin apart by his pawn.")
        elif choice == "play dead person role.":
            print("lion come and sniff you and leave you thinking you are a dead person.")
            print("Now you can leave that room secreatly.")
            exit(0)
        elif choice == "play with her cubs":
            dead("she will made you stay there forever .")
        else:
            print("I don't know what you trying to say.")


def dead(Why):
    print(Why,"You are dead!!!")
    exit(0)

def start():
    print("You are standing in a dark room.")
    print("There are 2 doors to exit.")
    print("Which one do you take?")

    choice = input("> ")
    if choice == "1":
        ghost_room()
    elif choice == "2":
        lion_room()
    else:
        dead("You stamble around the room until you starve.")

start()