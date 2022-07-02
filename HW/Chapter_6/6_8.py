dina = {'name':'dina',
	'type':'cat',
	'owner':'john'}

uma = {'name':'uma',
	'type':'dog',
	'owner':'pasha'}

mickey = {'name':'mickey',
	'type':'mouse',
	'owner':'lena'}

pets = [dina, uma , mickey]
for pet in pets:
	print (f'\nName pet is {pet["name"].title()}')
	print (f'Type pet is {pet["type"].title()}')
	print (f'Owner pet"s is {pet["owner"].title()}')
