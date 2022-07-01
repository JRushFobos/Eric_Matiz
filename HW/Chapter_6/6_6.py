favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'rudy',
	'phil':'python',
	}

friends = {'phil','sarah'}

for name in favorite_languages:#keys():
	print (f'Hi {name.title()}')

	if name in friends:
		language = favorite_languages[name]
		print (f'{name.title()}, I see y favorite language is {language.title()}')