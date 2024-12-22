print("welcome to treasure island")

choice1 = input('you\'r at a crossroad , where do you want to go ? Type "left" or "right" ').lower()

if choice1 == "left":
    print("\n")
    choice2 = input('you came to a lake .Type "wait" to wait for a boat . Type "swim" to swim across').lower()

    if choice2 == "wait":
        choice3 = input("you arrive at an island . choose a color out of red , blue and yellow \n which color do you choose  ").lower()

        if choice3 == "red":
            print("you won")
        elif choice3 == "blue":
            print("you were close")
        else:
            print("nice try")

    else:
        print("you got attacked . Game over")
else:

    print("game over")
