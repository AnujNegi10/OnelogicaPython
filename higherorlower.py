import random
data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 346,
        "description": "Musician and Actress",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 330,
        "description": "Actor and Former Wrestler",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 380,
        "description": "Reality TV Star and Entrepreneur",
        "country": "United States"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 370,
        "description": "Musician and Actress",
        "country": "United States"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 250,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 290,
        "description": "Reality TV Star and Entrepreneur",
        "country": "United States"
    },
    {
        "name": "Beyoncé",
        "follower_count": 250,
        "description": "Musician and Actress",
        "country": "United States"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 290,
        "description": "Musician",
        "country": "Canada"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 270,
        "description": "Musician",
        "country": "United States"
    }
]
points = 0
again = False
while(not again):
    
    compareA = random.choice(data)
    print(f"Compare A: {compareA["name"]}")
    
    compareB = random.choice(data)
    print(f"Compare B: {compareB["name"]}")
    
    while compareA == compareB:
        compareB = random.choice(data)


    res = input("Who has more followers? Type 'A' or 'B' : ").upper()
    def tofind(A,B,res):
        if res!="A" and res !="B":
            
            return f"invalid choice"
        if A>B and res=="A":
            return True
        elif A>B and res=="B":
            return False
        elif A<B and res=="B":
            return True
        else:
            return False
        # else:
        #     print("invalid")
    
    resof_func = tofind(int(compareA["follower_count"]),int(compareB["follower_count"]),res)

    if resof_func == True:
        print("you guessed it right")
        points +=1
        # again = False
    elif resof_func=="invalid choice":
        print("invalid choice")
        break
    else:
        print(f"you loose . Toatal Points : {points}")
        again = True

