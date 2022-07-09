import os
os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_10\\10.4')

with open ('guest_book.txt','a') as users_list:
    while True:
        user = input("Input user name, or press 'q' to exit.")
        if user != 'q':
            print (f'Hello {user.title()}')
            users_list.write(user + '\n')
        else:
            break

with open ('guest_book.txt','r') as users_list:
    guests = users_list.readlines()
    for user in guests:
        print(user, end='')