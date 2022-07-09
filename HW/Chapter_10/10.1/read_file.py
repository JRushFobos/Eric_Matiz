with open ('learning_python.txt') as learning_python:
    learning_python_lines = learning_python.readlines()

'''read all file'''
for line in learning_python_lines:   
    print(line.strip())

'''Enumeration strings'''
line_enumeration = ''
for string in learning_python_lines:
    line_enumeration += string

print(line_enumeration.strip())

'''Save string ib list'''
save_to_list = learning_python_lines
for string in save_to_list:
    print (string.strip())




