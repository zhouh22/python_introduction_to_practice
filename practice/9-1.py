class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe(self):
        print(f'{self.type, self.name}')

    def open(self):
        print('餐馆正在营业')

    def set_number_served(self, person_number):
        self.number_served = person_number

    def increment_number_served(self, increase_person):
        self.number_served += increase_person


r = Restaurant('a', '1')
# r.describe()
# r.open()
# print(r.number_served)
# r.number_served = 10
# print(r.number_served)
r.set_number_served(100)
print(r.number_served)
r.increment_number_served(19)
print(r.number_served)
