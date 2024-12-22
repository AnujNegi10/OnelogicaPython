import random
print("welcome to rps")
print("1 is for rock \n 2 is for paper \n 3 is for scissors")

humanchoice = int(input("enter your choice "))

ai_choice_lsit = [1,2,3]
aichoice = random.choice(ai_choice_lsit)

if humanchoice>3:
    print("invalid choice")

else:
    print(f"ai choosed {aichoice}")

if (aichoice==1 and humanchoice==1) or (aichoice==2 and humanchoice==2) or (aichoice==3 and humanchoice==3):
    print("Draw")

else:
    if aichoice==1 and humanchoice==3:
        print("ai won")
    
    elif aichoice==1 and humanchoice == 2:
        print("you won")

    elif aichoice==2 and humanchoice == 1:
        print("ai won")
    elif aichoice==2 and humanchoice == 3:
        print("you won")
    elif aichoice==3 and humanchoice == 1:
        print("you won")
    elif aichoice==3 and humanchoice == 2:
        print("ai won")
   



    
    


 

