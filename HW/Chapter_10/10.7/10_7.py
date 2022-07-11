import os
os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_10\\10.5')

with open ('programing_like.txt','w') as programing_like:
    while True:
        answer = input ('Write whay do y like programing, press "q" to Exit')
        if answer != 'q':
            programing_like.write(answer+'\n')
        else:
            break

with open ('programing_like.txt','r') as programing_like:
    answer_list = programing_like.readlines()
    for answer in answer_list:
        print (answer, end='')