import os
os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_10\\10.10')


def find_the (filename):
    with open (filename) as f:
        content = f.read()
        all_the = content.lower().count('the')
        print(f'In the file {filename} word "the" appears {all_the} time')
        only_the = content.count('the ')
        print(f'In the file {filename} word only "the" appears {only_the} time')

filenames=['The Happy Family.txt','The Gringos.txt','Cow-Country.txt']
for filename in filenames:
    find_the(filename)