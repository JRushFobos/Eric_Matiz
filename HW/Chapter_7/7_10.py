response = {}
active = True
while active:
    name = input ('What is your name?:')
    trip = input ('Were did you want to go?')
    response[name]=trip

    repeat = input ('Repeat input? Press "no" if your want to stop')
    if repeat == 'no':
        active = False

print ('Output all list with trip')
for name,trip in response.items():
    print (f'Person {name} want to trip in {trip}')    

