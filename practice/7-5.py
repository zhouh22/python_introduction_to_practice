while True:
    age = int(input('请输入用户的年龄：'))
    if age < 3:
        print('票价免费')
    elif 3 <= age <= 12:
        print('收费10美元')
    elif age > 12:
        print('收费15美元')
