# WITH ... AS ...
# with open('file.txt', 'rb') as f:
#     f.read()
#
# Данная конструкция позволяет октрывать и закрывать файлы автоматически без вызова метода .close()
# __________________________
# with open('file.txt', 'rb') as f:
#     f.read()

# with open('test.txt', 'rb') as f:
#
#     print(f.read())
#
# f = open('test.txt', 'rb')
# print(f.read())
# f.close
# __________________________
# with open('testA.txt', 'rb') as f:
#     print(str(f.read()))
#
# f = open('testA.txt', 'rb')
# print(str(f.read()))
# f.close
# _____________________________
# with open('testA.txt', 'w') as file:
#     for i in range(5):
#         s = input('Введите слово: ')
#         file.write(s+'\n')
#
# with open('testA.txt', 'r') as f:
#     for i in f.readlines():
#         print(i)

# with open('testA.txt', 'w') as file:
#     for i in range(5):
#         s = input('Введите словао: ')
#         file.write(s+'\n')
#
# with open('testA.txt', 'r') as f:
#     data_file = f.readlines()
#     print(data_file)
#     if 'test\n' in data_file:
#         print('Yes')












