class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.permissionSelect = True

# moderator dziedziczy po obiekcie user
class Moderator(User):
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.permissionInsert = True







# admin dziedziczy po obiekcie moderator
class Admin(Moderator):
    pass

