import random

randnum = random.randint(1,100)

number = int(input("I am guessing ȧnumber between 1 to 100 : "))

difficulty = input("choose difficulty level : easy hard")

attempts = 10
if difficulty=="hard":
    attempts=5
again = False

while(not again):
    user_guess = int(input("Make a guess"))
    if attempts==1:
        print("you loose")
        break
    if randnum>user_guess:
        print("too low")
        attempts -= 1
        print(f"remaining ateempts : {attempts}")
        again= False
    elif randnum<user_guess:
        print("too high")
        attempts -= 1
        print(f"remaining ateempts : {attempts}")
        again=False
   
        
    else:
        print(f"you got it . The answer was {randnum}")
        again = True