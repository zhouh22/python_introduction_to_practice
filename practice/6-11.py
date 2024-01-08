cities = {
    'China': {
        'country': 'a',
        'population': 'a',
        'fact': 'a'
    },
    'Brunei': {
        'country': 'a',
        'population': 'a',
        'fact': 'a'
    },
    'Qatar': {
        'country': 'c',
        'population': 'c',
        'fact': 'c'
    }
}

for keys, values in cities.items():
    for i, j in values.items():
        print(keys, i, j)
