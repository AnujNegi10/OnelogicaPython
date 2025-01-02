class User:
    def __init__(self, username, email, preferences=None):
        """
        Initializes a user instance.
        
        :param username: Username of the user
        :param email: Email address of the user
        :param preferences: Optional preferences for personalized recommendations
        """
        self.username = username
        self.email = email
        self.preferences = preferences if preferences else []

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"

    def add_preference(self, preference):
        """
        Adds a preference to the user's list.
        
        :param preference: Product category or keyword
        """
        self.preferences.append(preference)
