import json
import os
os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_10\\10.11')


favorite_num = 'favorite_num.json'
with open (favorite_num, 'w') as f:
    num = input ('Inter your favorite number: ')
    json.dump(num, f)

    
