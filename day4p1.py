# Lists
import random
fruits =["mango","apple","bannana",34]
# index in frwd = 0,1,2,3...
# index in bckwrd = -1,-2,-3....

# alter any item in list
fruits[1] = "mac"
print(fruits[1])
print(fruits[-1])

# append any element to the end
fruits.append("newfruit")
fruits.append("mango")
print(fruits)

# extend : to add a new list to the end of a current list

fruits.extend([1,2,3])
print(fruits)
print(len(fruits))
print(fruits[8])

# cannot extend a non iterable element

# doing the same task with append 

fruits.append([1,2,3])
print(fruits)

# game - who will pay the bill

friends = ["anuj","vaibhav","naseem","vivek","ankur","slok"]
length = len(friends)
pickhim = random.randint(0,length-1)

print(f"he will pay the bill : {friends[pickhim]}")

# inbuilt function is also there 

print(f"he will pay {random.choice(friends)}")

#  nested list

dog_breeds = [
    "Labrador Retriever",
    "German Shepherd",
    "Golden Retriever",
    "Bulldog",
    "Poodle",
    "Beagle",
    "Rottweiler",
    "Siberian Husky",]

cat_breeds = [
    "Persian",
    "Siamese",
    "Maine Coon",
    "Bengal",
    "Ragdoll",
    "Sphynx",
    "British Shorthair",
    "Abyssinian",]

pet_animals = [dog_breeds,cat_breeds]
print(pet_animals)
print(pet_animals[0])
print(pet_animals[0][2])

len2 = len(pet_animals[0])
print(len2)

lenbase = len(pet_animals)
print(lenbase)