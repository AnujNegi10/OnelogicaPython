# key : value
# {key : value}
# {"schools" : "a place to learn"}

prog_dict = {"error":"An error in a program that prevents the prog " , "function":"a code that can be reused "}

print(prog_dict["error"])
# print(prog_dict["error3"]) key error

# to enter a new key
prog_dict["newkey"] = "new key value"
print(prog_dict)

# empty dictinory
empty_dictionary = {}


# wipe an existing dictionaries
# prog_dict = {}
# print(prog_dict)

# edit an item in a dictionary
prog_dict["error"] = "moth in the computer"
print(prog_dict)

print("\n")
# iterate in dict
for i in prog_dict:
    # gets the key
    print(i)

    # gets the value of the key
    print(prog_dict[i])

# Nested list

travelto ={
    "india":["new delhi","pune","orrisa"]
}
# how to access pune
print(travelto["india"][1])

nested_list = ["A","B",["C","D"]]
# how to print letter D

print(nested_list[2][1])

# travel log

travel = {
    "India":{
        "city":["pune","mumbai"],
        "visits":{1,2,3}
    }
}
print(travel["India"]["city"][1])
print(travel["India"]["visits"])

print(travel.values())
print(travel.keys())