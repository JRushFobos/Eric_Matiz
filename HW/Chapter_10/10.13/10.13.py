import json
import os
os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_10\\10.13')


def get_stored_username():
    '''Получает имя пользоватебя если оно существует'''
    filename = 'usenname.json'
    try:
        with open (filename,'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        None
    else:
        return username

def get_new_username():
    '''Запрашивает новое имя пользователя'''
    username = input('What is your name?')
    filename = 'usenname.json'
    with open (filename,'w') as f:
        json.dump(username,f)
    return username
    
def greet_user():
    '''Приветствует пользователя по имени'''
    new_username = get_new_username()
    stored_username = get_stored_username()
    if new_username == stored_username:
        print(f'Enter the username of the last user who used the program')
        get_new_username()
    else:
        print(f"We'll remember you when you come back,{stored_username}!")

greet_user()
    