users = ['admin', 'zhouhang', 'rou', 'qi', 'yan', '']
for user in users:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report')
    elif user == '':
        print('We need to find some users')
    else:
        print(f'Hello {user}, thank you for logging in again')
