class Restaurant ():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print (f"Restorant name is {self.restaurant_name.title()} with cuisine {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print (f"Restorant {self.restaurant_name.title()} is open")

rich_star_restoran = Restaurant('Rich Star', 'Japanese')
poor_moon_restoran = Restaurant('Poor Moon', 'Italian')
agraba_restoran = Restaurant('Agraba', 'Eastern')

rich_star_restoran.describe_restaurant()
poor_moon_restoran.describe_restaurant()
agraba_restoran.describe_restaurant()
