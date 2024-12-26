import random
black_deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]

player_cards = []
computer_cards = []

for i in range(0,2):
    player_cards.append(random.choice(black_deck))
    computer_cards.append(random.choice(black_deck))
    
# print(player_cards)
player_sum = sum(player_cards)
computer_sum = sum(computer_cards)
# print(player_sum)

def doesisblackjack_player(player_sum):
    if player_sum==21:
        return True
    else:
        return False
    
def doesisblackjack_computer(computer_sum):
    if computer_sum==21:
        return True
    else:
        return False

def user_lesseleven(player_sum):
    if player_sum<21 :
        if (11 in player_cards):
            newone = player_sum+11
            result = doesisblackjack_player(newone)
            if result == False:
                return False
            
    
if doesisblackjack_computer==True and doesisblackjack_player==False:
    print("computer won")
elif doesisblackjack_computer==False and doesisblackjack_player==True:
    print("player won")
else:
    