person1 = {
	'first_name':'Katia',
	'last_name':'Bogacheva',
	'age':'28',
	'city':'Perm',
	}


person2 = {
	'first_name':'Oleg',
	'last_name':'Svetozar',
	'age':'40',
	'city':'Moscow',
	}


person3 = {
	'first_name':'Olya',
	'last_name':'Buziva',
	'age':'28',
	'city':'Chusovoy',
	}


people = [person1, person2, person3]
for person in people:
    print('\nName:', person['name'], person['surname'])
    print('Age:', person['age'])
    print('City:', person['city'])
