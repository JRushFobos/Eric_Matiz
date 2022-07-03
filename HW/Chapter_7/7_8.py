sandwich_orders = ['peperony','cheese','mushrooms','tomato','meat']
finished_sandwiches =[]
print (sandwich_orders)
print (finished_sandwiches)
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print (f'I made your {sandwich} sandwich')
    finished_sandwiches.append(sandwich)

print('Sandwich order:',sandwich_orders)
print('Finish sandwiches:',finished_sandwiches)
