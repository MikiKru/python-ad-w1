class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.permissionSelect = True
    def readPost(self):
        if(self.permissionSelect):
            print("READING...")
    def __str__(self):
        return "login: %s password: %s PERMISSIONS: %s" \
               %(self.login,self.password, ("SELECT" if (self.permissionSelect == True) else ""))

# moderator dziedziczy po obiekcie user
class Moderator(User):
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.permissionInsert = True

user = User("user", "user")
print(user)




# admin dziedziczy po obiekcie moderator
class Admin(Moderator):
    pass

