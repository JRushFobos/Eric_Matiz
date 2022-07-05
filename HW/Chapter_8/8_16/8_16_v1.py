import build_profile

user_profile = build_profile.build('albert', 'einstein',
                             nationality='Russian',
                             gender='melee',
                             marital='single')
print(user_profile)