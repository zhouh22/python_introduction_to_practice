from random import choice


class Ticket:
    def __init__(self):
        pass


my_ticket = ['1', '6', 'a', 'e']
i = 1
while True:
    number = [str(i) for i in range(10)]
    number.extend(['a', 'b', 'c', 'd', 'e'])
    tar_num = []
    for _ in range(4):
        a = choice(number)
        number.remove(a)
        tar_num.append(a)
    if my_ticket[0] in tar_num and my_ticket[1] in tar_num and \
            my_ticket[2] in tar_num and my_ticket[3] in tar_num:
        print(f"第{i}次中奖了")
        print(tar_num)
        break
    else:
        print(f"第{i}次没有中奖")
        i += 1
