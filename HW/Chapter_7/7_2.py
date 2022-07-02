promt = 'How many people to book a table'

book = input(promt)
if int(book) > 8:
	print ('Please, wait...')
else:
	print ('We are waiting for you in our restaurant')