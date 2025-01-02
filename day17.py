class User:
    def __init__(self,user_id,username):
        # print("new object is created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        user.followers +=1
        self.followers +=1

user_1 = User("001","anuj")
user_2 = User("002","aman")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# we can also set default value such as followers in this case   

# user_1 = User("001","anuj")
# # user_1.id = "001"
# # user_1.username = "anuj"
# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)

# print("\n")
# user_2 = User("002","aman")
# # user_2.id = "002"
# print(user_2.id)
# print(user_2.username)

