import print_function

def make_car(marka, model, **car_info):
    car = {'marka':marka, 'model':model}
    for key, value in car_info.items():
        car[key] = value
    print_function.print_info_car(car)


car = make_car('Audi', 'T2', color='Red', tow_package='True')