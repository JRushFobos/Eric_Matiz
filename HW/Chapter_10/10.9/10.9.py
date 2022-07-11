import shutil
import os
os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_10\\10.8')

def open_files(filename):
    try:
        with open (filename) as f:
            names = f.readlines()
    except FileNotFoundError:
        pass
    else:
        for name in names:
            print(name.title(), end='')
            
filenames = ['dogs.txt','cats.txt']
for filename in filenames:
    open_files(filename)

#shutil.move('dogs.txt', 'move//dogs.txt')
