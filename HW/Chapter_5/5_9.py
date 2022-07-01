names = ['admin', 'john', 'oleg', 'mike', 'kate']
if names:
    for name in names:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ', name.title(), ' thank you for logging in again')
else:
    print('List is empty')
