class Restaurant ():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print (f"Restorant name is {self.restaurant_name.title()} with cuisine {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print (f"Restorant {self.restaurant_name.title()} is open")

    def restaurant(self):
        print (f'Number of visitors served: {self.number_served}')

    '''Изменение с помощью метода и печать'''
    def set_number_served(self,numbers_visitors):
        self.number_served = numbers_visitors
        print (f'Number of visitors served (using the method): {self.number_served}')
    
    '''Изменение с помощью метода и приращивания - incriment'''
    def increment_number_served(self,numbers_visitors):
        self.number_served += numbers_visitors
        print (f'the number of visitors served increased and amounted to:{self.number_served}')
    
class Icecreamstand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def show_flavors_list(self,*flavors):
        print('Flavors list:')
        for flavor in flavors:
            print (flavor.title())
    

my_restoran = Restaurant('Night Moon','Russain')
my_restoran.describe_restaurant()
my_restoran.open_restaurant()
my_restoran.restaurant()

'''class IceCreanStand'''
IceCream = Icecreamstand('Morozko','Russain')
IceCream.show_flavors_list('apricot', 'banana', 'vanilla', 'cherry')

'''Прямое изменение атрибута'''
my_restoran.number_served = 20
my_restoran.restaurant()

'''Изменение с помощью метода и печать'''
my_restoran.set_number_served(40)

'''Изменение с помощью метода и приращивания - incriment'''
my_restoran.increment_number_served(50)

