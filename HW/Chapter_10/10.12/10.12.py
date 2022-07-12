import json
import os
os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_10\\10.12')


try:
    favorite_num = 'favorite_num.json'
    with open (favorite_num,'r') as f:
        num = json.load(f)
        print(f'Я знаю ваше любимое число! Это {num}')  
except FileNotFoundError:
    favorite_num = 'favorite_num.json'
    with open (favorite_num, 'w') as f:
        num = input ('Inter your favorite number: ')
        json.dump(num, f)  


