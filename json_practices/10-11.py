import json

try:
    filename = 'a.json'
    a = input('Please enter you like number:')
    with open(filename, 'w') as file:
        json.dump(a, file)
    with open(filename) as file:
        print(json.load(file))
except ValueError:
    print("*********8")
