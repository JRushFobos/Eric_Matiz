favorite_places = {
    'sam':['nowyork','london','paris'],
    'jack':['beijing','tokyo'],
    'rose':['ottawa'],
    }
for name,cites in favorite_places.items():
	print (f'Name {name.title()} lives in:')
	for city in cites:
		print (f'\t{city.title()}')

