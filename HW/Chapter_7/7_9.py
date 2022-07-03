sandwich_orders = ['pastrami','peperony','cheese','mushrooms','tomato','meat']
finished_sandwiches =[]
print (sandwich_orders)
print (finished_sandwiches)
print ('Pastrami is endless')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print ('Sandwich orders without pastrami:',sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print (f'I made your {sandwich} sandwich')
    finished_sandwiches.append(sandwich)

print('Sandwich order:',sandwich_orders)
print('Finish sandwiches:',finished_sandwiches)
