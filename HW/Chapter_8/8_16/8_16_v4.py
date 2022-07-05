import build_profile as b

user_profile = b.build('albert', 'einstein',
                             nationality='Russian',
                             gender='melee',
                             marital='single')
print(user_profile)