def add(n1,n2):
    return n1+n2 

def subtract(n1,n2):
    return n1-n2 
def divide(n1,n2):
    return n1/n2 
def multiply(n1,n2):
    return n1*n2 

oprn_dict = {"+":add ,"-":subtract,"/":divide,"*":multiply}

# variable func
# print(oprn_dict["*"](2,3))



def calculator():
    fn = int(input("enter the first number: "))
    again = True
    
    while again:
        oprn = input("enter the operation to perform *,/,+,- ")

        sn = int(input("enter the sec numbere: "))
        answer=oprn_dict[oprn](fn,sn)
        print(f"{fn} {oprn} {sn} = {answer}")

        choice=input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation")

        if choice =="y":
            fn = answer
        else:
            again = False
            calculator()
            # ! recurssion
    
calculator()
    




