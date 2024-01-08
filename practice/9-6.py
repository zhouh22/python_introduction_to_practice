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


class Ice_CreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['草莓', '芒果', '西瓜']

    def show_flavors(self):
        for item in self.flavors:
            print(item)


ice = Ice_CreamStand('a', 'b')
print(ice.flavors)
print(ice.show_flavors())
