def get_city_function (city, country, population=''):
    if population:
        full_name = f'{city.title()} {country.title()} - population: {population}'
        return full_name
    else:
        full_name = f'{city.title()} {country.title()}'
        return full_name
    
get_city_function('santiago','chile')