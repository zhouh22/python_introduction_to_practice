import json

filename = 'a.json'
try:
    username = input("请输入你的用户名：")
    if username.lower() == 'bo_voy':
        with open(filename, encoding='utf-8') as file:
            content = file.read()
            if len(content) != 0:
                with open(filename) as f1:
                    print(f"您已经存在的数字为{json.load(f1)}")
            else:
                number = input("请输入数字:")
                int(number)
                with open(filename, 'w') as f:
                    json.dump(number, f)
    else:
        print('不是本人')
except FileNotFoundError:
    pass
