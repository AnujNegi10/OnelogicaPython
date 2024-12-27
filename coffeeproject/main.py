from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

again = True
while again:
    user = input(f"What would you like? {menu.get_items()}: ")
    if user=="off":
        again=False
    elif user=="report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(user)
        print(drink)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
        # print(coffeemaker.is_resource_sufficient(drink))
        
        

