toppings = []
active = True
while active:
    topping = input('Enter topping for pizza or "quit" for leave')
    if topping != 'quit':
        toppings.append(topping)
    else:
        break

print ('Your topping ',topping ,' add in your order')

