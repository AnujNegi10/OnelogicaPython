# scope
# local and global scope

# global scope
a=10

def newfunc():
    b=20 # local scope
    print(a)
    print(b)

newfunc()
# print(b) can not be accessed

print("\n")

player_health = 10

def game():
    def drink_prime():
        health=2
        print(player_health)
        print(health)
    print(player_health)
    drink_prime()
game()

# there is no block scope in python

game_level = 3
animal = ["dog","cat","cow"]


if game_level < 5:
    new_enemy = animal[0]
    

# as there is no block scope so new_enemy is still accessible untill it is in a function

print(new_enemy)

print("\n")

# modifying global scope

a = 1
def inc_value():
    global a # without this it treats the "a" as a local variable and thus give error
    
    a +=10
    print(f"new value {a}")
inc_value()
print(f"value : {a}")

# Global constants always write in capital letter
PI_VALUE = 3.14
