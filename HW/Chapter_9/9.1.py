class Restaurant ():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print (f"Restorant name is {self.restaurant_name.title()} with cuisine {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print (f"Restorant {self.restaurant_name.title()} is open")

my_restoran = Restaurant('Rich Star', 'Japanese')

my_restoran.describe_restaurant()
my_restoran.open_restaurant()