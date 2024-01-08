# with open('learning_python.txt') as file:
#     content = file.read()
#     print(content, end='')
with open('learning_python.txt') as file:
    content = file.readlines()
    for item in content:
        #     print(item, end='')
        # print(file)
        # con = file.readline()
        # print(con)
        # print(content)
        if 'python' in item:
            print(item.replace('python', 'c'), end='')
