# my_file = open('/home/hpadmin/Downloads/Colorful_Shanghai_(163856257).jpeg', 'r')
# print(my_file)
# print(type(my_file)) #<class '_io.TextIOWrapper'>
#
#
# my_file = open('/home/hpadmin/Downloads/Colorful_Shanghai_(163856257).jpeg', 'rb')
# print(my_file)
# print(type(my_file)) #<class '_io.BufferedReader'>

# 'r' - Для чтения
# 'w' - Только для записи
# "rb", "wb" - Буква b ставится после основного мода для возможности открыть файл в байт режиме.
# "a" - мод позволяет открыть файл без потери данных для записи в него!
# _______________________________________________________________________
# .read()
# Данный метод выгружает всё содержимое файла в переменную.
# .write(*)
# Данный метод записывает содержимое в файл.
# .readlines()
# Данный метод берёт каждую линию текста и добавляет её в лист.
# .close()
# Данный метоб ОБЯЗАТЕЛЕН!
# Он закрывает соединение с файлом
# _______________________________________________________________________
# my_file = open('/home/hpadmin/Downloads/Colorful_Shanghai_(163856257).jpeg', 'rb')
# my_file.close()
# _______________________________________________________________________
# "w" - открыть файл, для записи. Если файл, уже сушествует, то он перезапишет (старые данные удаляются).
# Если нет, то файл создается
# my_fileW = open('testW.txt', 'w')
# my_fileW.write('We are, Python!')
# my_fileW.close()
# #
# # 'a' - открыть файл, для записи. Если файл уже сушествует, то он добавляет. Или же, дополняе, если нет - создает новую.
# my_fileA = open('testA.txt', 'a')
# my_fileA.write(' Hi, dear! ')
# my_fileA.close()
#
# my_fileR = open('testA.txt', 'a')
# data_file = my_fileR.readlines()
# print(data_file)
# my_fileR.close()

# my_fileRB = open('testA.txt', 'rb')
# data_file = my_fileRB.read()
# print(data_file)
# my_fileRB.close()


# my_file = open('testA.txt', 'a') # a - add добавить
# my_file.write(' Hello! My name is Nurislam \n '
#                ' How are you doing today? \n'
#                'What is your name? ')
# my_file.close()
#
# my_file = open('testA.txt', 'r') # r - читать
# data_file = my_file.read()
# print(data_file)
# my_file.close()















