names = ['joey', '瑞秋', '钱', '莫妮卡']
name = names.pop(2)
names.append('小贱贱')
print(len(names))
for i in names:
    print(f'我想邀请“{i}”来共进晚餐')
print(f'{name}')
print('我找到了更大的一个餐桌')
names.insert(0, '嘿嘿')
names.append('哈哈')
for i in names:
    print(f'我想邀请“{i}”来共进晚餐')
print('我只能邀请两位嘉宾共进晚餐')
print(names)
for i in range(len(names)):
    if len(names) != 2:
        name1 = names.pop()
        print(f'我无法邀请“{name1}”来共进晚餐,抱歉')
print(names)
del names[-1]
del names[-1]
print(names)
