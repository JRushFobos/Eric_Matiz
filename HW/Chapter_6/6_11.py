cities = {
    'guangzhou':{
        'country':'Сhina',
        'population':700000,
        'fact':'canton',
        },
    'london':{
        'country':'United Kingdom',
        'population':800000,
        'fact':'modern',
        },
    'newyork':{
        'country':'Russia',
        'population':850000,
        'fact':'modern',
        }
        }
for city, city_info in cities.items():
	print (f'City: {city.title()}')
	print (f'\t{city_info["country"]}')
	print (f'\t{city_info["population"]}')
	print (f'\t{city_info["fact"]}')  
