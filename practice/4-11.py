my_pizz = ['a', 'b', 'c']
friend_pizz = my_pizz[:]
my_pizz.append('d')
friend_pizz.append('e')
for item in friend_pizz:
    print(item, end='、')
