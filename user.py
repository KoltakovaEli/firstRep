from matplotlib import use


class User:
    def __init__(self, username, password):
        self.name = username
        self.password = password
        self.__hash_password()
    def change_name(self, username):
        self.name = username
    def change_password(self, password):
        self.password = password
    def __hash_password(self):
        self.password += "123123"
class Admin(User):
    def hi(self):
        print("Hello,Fox!")
    def change_name(self,username):
        self.name = "admin: "+ username