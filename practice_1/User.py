import operator


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_ticket = ['1', '6', 'a', 'e']
my_ticket1 = ['6', '1', 'a', 'e']
print(my_ticket == my_ticket1)
print(operator.eq(my_ticket, my_ticket1))
print(sorted(my_ticket) == sorted(my_ticket1))
