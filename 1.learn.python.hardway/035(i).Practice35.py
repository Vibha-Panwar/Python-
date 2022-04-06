def ghost_room():
    print("There is a ghost here.")
    print("that ghost standing infront of another gate.")
    print("How are you going to move that ghost?")

    choice = input("> ")

    if choice == "talk with it":
        print("It will tell you about your future girlfriend.")
    elif choice == "tease it":
        print("it will slap your face off.")
    elif choice == "worship the God.":
        print("ghost vanish in thin air .So, now you can leave this room easily.Good Job!!!")
    else:
        print("I don't know what that mean.")

def bear_room():
    print("Here is a big fat bear.")
    print("How are you going to move that bear from another door so that you can left that room alive???")

    choice = input("> ")

    if choice == "stand like a statue.":
        print("Bear come to you then kick you and pill your skin apart by his pawn.")
    elif choice == "play dead person role.":
        print("Bear come and sniff you and leave you thinking you are a dead person.")
        print("Now you can leave that room secreatly.")
    elif choice == "play with her cubs ":
        print("she will made you stay there forever .")

    else:
        print("I don't know what you trying to say.")

def start():
    print("You are standing in a dark room.")
    print("There are 2 doors to exit.")
    print("Which one do you take?")

    choice = input("> ")
    if choice == 1:
        ghost_room()
    elif choice == 2:
        bear_room()
    else:
        print("You stamble around the room until you starve.")

start()