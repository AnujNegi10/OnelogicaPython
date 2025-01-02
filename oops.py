# oops<object oriented programming>

from turtle import Turtle,Screen
# timmy = Turtle()
# my_screen = Screen()
# # print(timmy)

# timmy.shape("turtle")
#object attribute 
# print(my_screen.canvheight) 

# object method
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])
# table.add_row(["Anuj", 16352, 1554769, 232.4])

# print(table)

table.add_column("Pokemon name",["pikachu","charmender","lizzardz"])
table.add_column("Type",["mammal","mammal","reptile"])
table.align = 'r'
print(table)