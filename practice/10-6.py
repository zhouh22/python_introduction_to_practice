while True:
    try:
        a = input("请输入一个数字:")
        b = input("请输入一个数字:")
        print(int(a) + int(b))
    except ValueError:
        print("您输入的内容不是数字,请重新输入")
