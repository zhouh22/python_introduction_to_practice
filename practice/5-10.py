current_users = ['Tom', 'ada', 'sasa', 'jiu', 'heihei']
new_users = ['tom', 'xiahou', 'haha', 'JIU', 'a']
for user in new_users:
    if user in current_users or user.lower() in current_users:
        print(f'该用户名{user}已被使用')
    else:
        pass
