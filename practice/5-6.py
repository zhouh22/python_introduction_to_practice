age = int(input('请输入年龄：'))
if age < 2:
    print('这个人是婴儿')
elif 2 <= age < 4:
    print('这个人是幼儿')
elif 4 <= age < 13:
    print('这个人是儿童')
elif 13 <= age < 20:
    print('这个人是青少年')
elif 20 <= age < 65:
    print('这个人是成年人')
elif age >= 65:
    print('这个人是老年人')
