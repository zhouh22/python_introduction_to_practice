while True:
    name = input('请输入你的名字:')
    print(f'欢迎{name}来到我的空间')
    with open('guest_book.txt', 'a') as file:
        file.write(name + '\n')
