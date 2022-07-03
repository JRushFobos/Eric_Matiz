def sandwiches (*toppings):
    print('Order sandwich with topping:')
    for topping in toppings:
        print ('Do your order by:',topping.title())


sandwiches('peperony','cheese','mushrooms','tomato','meat')
sandwiches('peperony','cheese','mushrooms')
sandwiches('peperony')