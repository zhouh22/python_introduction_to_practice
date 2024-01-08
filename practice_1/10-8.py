try:
    with open('cats.txt') as file:
        cats = file.read()
    with open('dogs.txt') as f:
        dogs = f.read()
    print(cats, dogs)
    print(dogs.count('the'))
except FileNotFoundError:
    print('文件夹不存在')
