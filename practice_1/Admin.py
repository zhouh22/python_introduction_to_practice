from User import User


class Admin(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.privileges = ["can add post", "can delete user", "can ban user"]

    def show_privileges(self):
        print(self.privileges)


tom = Admin('Tom',18)
tom.show_privileges()
