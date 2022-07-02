favorite_nums = {'jack':[8,16,32],
                 'lucy':[5,10,15],
                 'ben':[14],
                 'joe':[19,20,40],
                 'kate':[21],
                 }

for name, numb in favorite_nums.items():
	print (f'{name.title()} have favorite number:')
	for num in numb:
		print (f'{num}')