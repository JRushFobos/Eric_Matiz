menu = ('pizza','falafel','carrot cake')
for name in menu:
    print(name)
add_menu = menu[:]
new_menu.append('pizza1')
new_menu.append('falafel1')
print(new_menu)
for name in new_menu:
    print(name)
