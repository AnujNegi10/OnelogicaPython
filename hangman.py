# take a word and ask the user to guess a letter if it is present give right else give false

import random
vocab = ["computer", "software", "AI", "cloud", "network", "database", "algorithm","forest", "ocean", "mountain", "river", "tree","school", "college", "university", "teacher", "learning", "library"]

choosed_word = random.choice(vocab).lower()

print(choosed_word)

print(len(choosed_word))
wordlen = len(choosed_word)

# placeholder
placeholder = ""
for pos in range(0,wordlen):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []
lives=6
while not game_over:
    guess_letter = input("enter a letter to guess ").lower()
    
    display=""
    
    for letter in choosed_word:
        
       
        if letter==guess_letter:
            display += guess_letter

            correct_letter.append(guess_letter)
            # print(f"remaining life : {lives}")
        elif letter in correct_letter:
            display+=letter
        else:
            display += "_"
    
            
    print(display)
    if guess_letter not in choosed_word:
        lives -= 1
        print(f"remaining life : {lives}")
        if lives == 0:
            game_over=True
            print("you loose")
    if "_" not in display:
        game_over = True
        print("you win")
    




