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
