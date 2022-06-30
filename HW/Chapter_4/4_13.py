menu = ('sausage', 'broccoli', 'potato', 'vegetables', 'chicken')
print('In menu next food:')
for name in menu:
    print(name)
new_menu = list(menu[:])
new_menu.append('tomato')
new_menu.append('sandwich')
new_menu = tuple(new_menu)
print(new_menu)
for name in new_menu:
    print(name)
