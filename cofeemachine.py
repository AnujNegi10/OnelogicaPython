MENU = {
    "espresso":{
        "ingridients":{
            "water":50,
            "coffee":18,
        },
        "cost":55
    },
    "latte":{
        "ingridients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":100,
    },
    "cappuccino":{
        "ingridients":{
            "water":258,
            "milk":100,
            "coffee":24,
        },
        "cost":30,
    }
}

resources = {
    "water":400,
    "milk":400,
    "coffee":100
}

def is_resources_there(ingridients):
    # is_enough=True
    lack_res=[]
    for item in ingridients:
        if ingridients[item]>= resources[item]:
            print(f"sorry there is not enough {item}")
            lack_res.append(item)
    return lack_res

def refill(lack):
    for item in lack:
        resources[item] += int(input(f"enter the refill amount {item}: "))
    print("Refilled successful")

def process_coins():
    print("insert rupees or coins")
    total = int(input("how many rupe 10:"))*10
    total += int(input("how many rupe 50:"))*50
    total += int(input("how many rupe 100:"))*100
    total += int(input("how many coin 5:"))*5
    
    return total

def is_transaction(money_got,cost):
    if money_got >= cost:
        change = money_got-cost
        print(f"Here is the change returned {change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry thats not enough money")
        return False
    
def make_coffee(drink_name,ingridients):
    for item in ingridients:
        resources[item]-=ingridients[item]
    print(f"Here is your {drink_name}")

profit=0
again=True

def coffee():
    global again
    while again :
        user = input("what do you want (espresso/latte/cappuccino)")
        
        if user=="off":
            again=False
            
        elif user=="report":
            print(f"Water:{resources['water']}")
            print(f"Milk:{resources['milk']}")
            print(f"Coffee:{resources['coffee']}")
            print(f"Money: ${profit}")
        else:
            drink = MENU[user]
            lacking = is_resources_there(drink["ingridients"])
            if not lacking:
                payment = process_coins()
                if is_transaction(payment,drink["cost"])==True:
                    make_coffee(user,drink["ingridients"])
                    
            else:
                refill(lacking)
                       
           
            
coffee()