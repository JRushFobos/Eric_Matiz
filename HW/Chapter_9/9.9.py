class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        long_name= f'{self.make} {self.model} {self.year}'
        return long_name.title()

    #Прямое изменение атрибута
    def read_odometr(self):
        print (f'This car has {self.odometr_reading} mile on it.')
    
    '''Изменениет атрибута с использованием метода''' 
    def update_odometr(self,mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print ("You can't roll back an odometer!")

    '''Изменение атрибута с приращиванием'''
    def increment_odometer(self,miles):
        self.odometr_reading += miles

class ElectricCar(Car):
    '''Автомобиль со спецификой электромобиля.'''
    def __init__(self,make,model,year):
        '''Инициализация атрибутов класса'''
        super().__init__(make,model,year)
        
        '''Класс как атрибут в классе'''
        self.battary = Battary()

'''Класс как атрибут в классе'''
class Battary():
    def __init__(self,battary_size=75):
        self.battary_size = battary_size

    def describe_battary(self):
        print (f'This car has a {self.battary_size} kWh battary')

    def get_range(self):
        if self.battary_size == 75:
            range = 260
        elif self.battary_size == 100:
            range = 315
        print(f'This carcan go about {range} miles on a full charge.')

    def upgrade_battery(self):
        if self.battary_size != 100:
            self.battary_size = 100
            print ('Battary charge on 100')
        else:
            print ('Battary charge on < 100')
        
my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battary.describe_battary()
my_tesla.battary.get_range()
my_tesla.battary.upgrade_battery()
my_tesla.battary.describe_battary()
my_tesla.battary.get_range()