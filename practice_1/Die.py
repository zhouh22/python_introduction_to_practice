from random import randint, choices


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


a = Die()
# print(a.roll_die())
b = Die(10)
c = Die(20)
for _ in range(9):
    print(f'a打印的值为{a.roll_die()}')
    print(f'b打印的值为{b.roll_die()}')
    print(f'c打印的值为{c.roll_die()}')
    print('*******************')
