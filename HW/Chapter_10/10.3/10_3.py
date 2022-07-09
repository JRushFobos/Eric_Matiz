import os
os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_10\\10.3')

user = input ('Please, inter your name')

with open ('guest.txt','w') as user_name:
    user_name.write(user)
