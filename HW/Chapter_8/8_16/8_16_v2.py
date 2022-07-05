from build_profile import build

user_profile = build('albert', 'einstein',
                             nationality='Russian',
                             gender='melee',
                             marital='single')
print(user_profile)