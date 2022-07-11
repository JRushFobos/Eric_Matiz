print('Addition calculator')
print('Enter 2 numbers, the calculator will add them')

while True:
    num1 = input('Input first number:')
    if  num1 == 'q':
        break

    num2 = input('Input second number:')
    if num2 == 'q':
        break

    try:
        sum = int(num1)+int(num2)
    except ValueError:
        print ('Only numbers are allowed to enter')
    else:
        print (f'Addition result: {sum}')