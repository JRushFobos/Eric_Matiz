pizzas = ['Pizza Marinara', 'Cheesy Crust Pizza', 'Neapolitan Pizza Margherita]
friend_pizzas = pizzas[:]
pizzas.append('Hunt')
friend_pizzas.append('seafood')
print(pizzas)
print(friend_pizzas)
for pizza in pizzas:
    print(pizza)
for pizza in friend_pizzas:
    print(pizza)
