class User:
    def __init__(self, name, password):
        self.name = name
        self.passwprd = password

    def login(self, name, password):
        if name == self.name and password == self.password:
            return True
        return False


class Admin(User):
    def __init__(self, name, password, privilages):
        super().__init__(name, password)
        self.privilages = privilages
    
    def get_privilages(self):
        return self.privilages

# там где можно использовать Admin, можно использовать User