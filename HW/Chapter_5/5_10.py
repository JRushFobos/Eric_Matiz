current_users = ['admin', 'john', 'oleg', 'mike', 'kate']
new_users = ['olia', 'tolia', 'serg', 'masha', 'misha']

for user in new_users:
    if user.lower() in current_users:
        print('f'User {user.title()} is already registered, please select a different username')
    else:
        print(f'You can register as {user.title()}')

