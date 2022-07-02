age = 'How old are you?'

while True:
   tiket_price = input (age)
   if age != 'quit':	
       if int(tiket_price) < 3:
           print ('Free')
       elif int(tiket_price) >=3 and int(tiket_price) >=12:
           print ('10$')
       else:
          int(tiket_price) > 12
          print('15$')
   else:
       break: