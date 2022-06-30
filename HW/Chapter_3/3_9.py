guests = ['Elon Musk', 'Albert Einstein', 'Nikola Tesla', 'Vasya Vakulenko']
my_invite = ' I\'d like to see you at dinner today!'
print('Number of guests:', len(guests))
print(guests[0], ',', my_invite.lower(), sep='')
guests = ['JRush', 'Dilen', 'Core', 'Baum']
prompt = "I'd like to see you at dinner today!"
print(guests[0], ',', prompt)
print(guests[1], ',', prompt)
print(guests[2], ',', prompt)
print(guests[3], ',', prompt)
no_come = guests.pop(0)
print(no_come, 'cant came today.')
guests.insert(0, 'Oveg')
print(guests[0], ',', prompt)
print(guests[1], ',', prompt)
print(guests[2], ',', prompt)
print(guests[3], ',', prompt)
print('\nMore guests are coming!')
new_guests = 'Jelu'
new_guests2 = 'Anatoly'
new_guests3 = 'Big boss'
guests.insert(0, new_guests)
guests.insert(2, new_guests)
guests.append(new_guests3)
print(len(guests), 'guests come today:')
print(guests[0], ',', prompt)
print(guests[1], ',', prompt)
print(guests[2], ',', prompt)
print(guests[3], ',', prompt)
print(guests[4], ',', prompt)
print(guests[5], ',', prompt)
print(guests[6], ',', prompt)
print('\nSorry only 2 guests today')
print(guests.pop(), 'sorry dont come')
print(guests.pop(), 'sorry dont come')
print(guests.pop(), 'sorry dont come')
print(guests.pop(), 'sorry dont come')
print(guests[0], 'i wait for you')
print(guests[1], 'i wait for you')
del guests[0]
del guests[0]
print(guests)
print(len(guests))
