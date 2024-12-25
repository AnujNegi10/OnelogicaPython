import random
import mymodule
a = random.randint(2,10)
print(a)
print(mymodule.mynumber)

# random => 0.0 <= X <1.0

rand_btw_0to1 = random.random()*10
#! Definition: Generates a random floating-point number in the range [0.0, 1.0) (inclusive of 0.0, but exclusive of 1.0).
print(round(rand_btw_0to1,1))

# may or maynot include upperbound 
rand_float = random.uniform(1,10)
#! Definition: Generates a random floating-point number in the range [a, b], including both a and b (the upper bound can be included).
print(rand_float)

# head and tails

random_handt = random.randint(0,1)

if random_handt == 0:
    print("head")
else:
    print("tails")

# randrange
# do not include upperbound [)
randr = random.randrange(1,3)
print(randr)


'''random.randint(a, b)	[a, b]	Yes
random.randrange(a, b)	[a, b)	No
random.uniform(a, b)	[a, b]	Yes (floating-point)
random.random()	[0.0, 1.0)	No'''