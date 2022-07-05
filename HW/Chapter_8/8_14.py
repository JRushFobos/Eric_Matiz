def make_car(marka, model, **car_info):
    car = {'marka':marka, 'model':model}
    for key, value in car_info.items():
        car[key] = value
    print_info_car(car)

def print_info_car(car):
    for keys,values in car.items():
        print (keys,':',values)

car = make_car('Audi', 'T2', color='Red', tow_package='True')