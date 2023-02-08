# 1
# Внутри my_module.py создайте вызваннную print которая выводит текст
# "Я функция из my_module.py". А затем импортируйте my_module.py в другой файл.
# И вызовите его.
# import my_modules1
#
# print(my_modules1)
# _________________________________________________________________________________
# 2
# Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat",
#                              "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# и вытащите 4 рандомных имени оттуда и сохраните в другой список.
import random
#
# spisok = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat",
#          "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random_list = random.sample(spisok,4)
# print(random_list)
# example 2
# import random
#
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat",
#          "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
#
# random_names = []
# for i in range(4):
#     random_index = random.randint(0, len(names) - 1)
#     random_names.append(names[random_index])
#
# print(random_names)
# _________________________________________________________________________________
# 3
# Узнайте какая у вас операционная система с помощью модуля sys и выведите на экран имя опрационной системы.
# import sys
#
# print(sys.platform)
# _________________________________________________________________________________
# 3
# Через терминал передайте Python несколько аргументов, а затем выведите их на экран

# _________________________________________________________________________________
# 4
# Через Python у себя на рабочем столе создайте директорию, а внутри дериктории создайте 5 РАНДОМНЫХ файлов.
# import os
# import random
# try:
#     os.mkdir('modules')
# except FileExistsError:
#     pass
# for i in range(5):
#     name = f'test{i}.txt'
#     file = os.path.join('modules', name)
#     with open(file, 'w') as file:
#         file.write(str(random.randint(1,5)))
# _________________________________________________________________________________
# 5
# Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.
# import random
# #1
# print('1 - задание')
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat",
#          "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random_names = []
# for i in range(4):
#     random.shuffle(names)
#     people = names[::2]
#     random_names.append(people)
# for i in enumerate(random_names):
#     print(i)
# #2
# print('2 - задание')
# random.shuffle(names)
# print(names )
# #3
# print('3 - задание')
# print(random.choice(names))
# #4
# print('4 - задание')
# names = random.randrange(1, 5, 1)
# print(names)
# _________________________________________________________________________________
# 6.
# Напишите программу которая будет принимать аргументы
# sys.argv и выводить на экран оттуда всё что передал пользователь.
# import sys

# s = ''
# s2 = ""
# for i in range(3,len(sys.argv)):
#     s = s + sys.argv[i]+' '
# s2 = s
# print(s2,end=' ')
# _________________________________________________________________________________
# 6.
# Спросите у пользователя 2 значения через input() а затем через модуль sys проверьте
# какое из 2-х значений занимает больше памяти.
# import sys
#
# a = input('Введите 1 - значение: ')
# b = input('Введите 2 - значение: ')
# size_a = sys.getsizeof(a)
# size_b = sys.getsizeof(b)
#
# if size_a > size_b:
#     print("1 - значение больше занимает памяти, чем 2: ", size_a)
# else:
#     print("2 - значение больше знаимает памяти чем 1: ", size_b)
# _________________________________________________________________________________
# 7.
# Создайте программу которая спрашивает у пользователя
# число N для генерации пароля а затем генерирует ему пароль длиною N символов.
# import random
#
# a = input('Введите число: ')
# simvoly = '0123456789'
# result = a + simvoly
# # result =  simvoly
# # print(random.choice(result))
# # print(random.choice(alfawid))
# # print(random.choice(simvoly))
# password = ''
#
# for i in range(4):
#     password += random.choice(result)
#
# print('Твой новый пароль: ', password)

# example 2 internet AI
# import random
# import string
#
# password_length = int(input("Enter the length of the password: "))
# symbols = string.ascii_letters + string.digits
#
# password = ''.join(random.choice(symbols) for i in range(password_length))
#
# print("Your password:", password)

# import string - # Есть оказывается свои встроенные методы внутри
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_letters = ascii_lowercase + ascii_uppercase
# digits = '0123456789'
# _________________________________________________________________________________
# 8.
# Создайте игру Камень-Ножницы-Бумага с Компьютером. Где компьютер даёт вам выбрать опцию,
# а сам затем генерирует своё значение. По итогу говорит выиграли вы, проиграли или ничья.
# import random
# l1 = ['stone', 'paper', 'scissors']
# print('1 - Камень')
# print('2 - Бумага')
# print('3 - Ножница')
# user = int(input('Введите число, для выбора: '))
# comp = random.randrange(1,4,1)
# print(user,comp)
# if user == comp:
#     print('Ничья')
# elif user == 1 and comp == 2:
#     print('Выграл компютер', comp)
# elif user == 1 and comp == 3:
#     print("Вы выиграли", comp)
# elif user == 2 and comp == 1:
#     print("Вы выиграли", comp)
# elif user == 2 and comp == 3:
#     print("Выграл компютер", comp)
# elif user == 3 and comp == 1:
#     print("Выграл компютер", comp)
# elif user == 3 and comp == 2:
#     print("Вы выиграли", comp)
# _________________________________________________________________________________
# 9.
# Используя функцию randrange() получите псевдослучайное четное число в пределах от 6 до 12.
# Также получите число кратное пяти в пределах от 5 до 100.
# from random import randrange
#
# print(randrange(6, 12, 2))
# print(randrange(5, 100, 5))
# ____________________________________________________________________________________
# 10.
# Найдите модуль os и sys в google и поработайте с каждым отдельно
# os
# os.name - имя операционной системы. Доступные варианты: 'posix', 'nt', 'mac', 'os2', 'ce', 'java'.
# os.environ - словарь переменных окружения. Изменяемый (можно добавлять и удалять переменные окружения).
# os.getlogin() - имя пользователя, вошедшего в терминал (Unix).
# os.getpid() - текущий id процесса.
# os.uname() - информация об ОС. возвращает объект с атрибутами: sysname - имя операционной системы, nodename - имя машины в сети (определяется реализацией), release - релиз, version - версия, machine - идентификатор машины.
# os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True) - проверка доступа к объекту у текущего пользователя. Флаги: os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение.
# os.chdir(path) - смена текущей директории.
# os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True) - смена прав доступа к объекту (mode - восьмеричное число).
# os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True) - меняет id владельца и группы (Unix).
# os.getcwd() - текущая рабочая директория.
# os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True) - создаёт жёсткую ссылку.
# os.listdir(path=".") - список файлов и директорий в папке.
# os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.
# os.makedirs(path, mode=0o777, exist_ok=False) - создаёт директорию, создавая при этом промежуточные директории.
# os.remove(path, *, dir_fd=None) - удаляет путь к файлу.
# os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает файл или директорию из src в dst.
# os.renames(old, new) - переименовывает old в new, создавая промежуточные директории.
# os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает из src в dst с принудительной заменой.
# os.rmdir(path, *, dir_fd=None) - удаляет пустую директорию.
# os.removedirs(path) - удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.
# os.symlink(source, link_name, target_is_directory=False, *, dir_fd=None) - создаёт символическую ссылку на объект.
# os.sync() - записывает все данные на диск (Unix).
# os.truncate(path, length) - обрезает файл до длины length.
# os.utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True) - модификация времени последнего доступа и изменения файла. Либо times - кортеж (время доступа в секундах, время изменения в секундах), либо ns - кортеж (время доступа в наносекундах, время изменения в наносекундах).
# os.walk(top, topdown=True, onerror=None, followlinks=False) - генерация имён файлов в дереве каталогов, сверху вниз (если topdown равен True), либо снизу вверх (если False). Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов).
# os.system(command) - исполняет системную команду, возвращает код её завершения (в случае успеха 0).
# os.urandom(n) - n случайных байт. Возможно использование этой функции в криптографических целях.
# os.path - модуль, реализующий некоторые полезные функции на работы с путями.

# sys
# _________________________________________________________________________________________________________________
# # 11.
# # Определить дату, которая наступит через 1000 дней от текущей даты
# import datetime
#
# dt = datetime.datetime.now()
# thdt = datetime.timedelta(days=1000)
# result = dt+thdt
# print('Через 1000 дней, будет дата и время: ', result)

# _________________________________________________________________________________________________________________
# NAMES = ["AIBEK", "JOOMART", "ADINAI", "ERMEK", "ATAI", "ASLAN", "LYAZAT",
#          "SALAVAT", "DANIYAR", "BOLOTBEK", "ALYMBEK", "DASTAN", "MAKSAT"]

# ПОВТОРЕНИЕ:
# ЗАДАНИЕ 1:
# С ПОМОЩЬЮ ЦИКЛА ПРОЙДИТЕ ПО ЛИСТУ NUMBERS И ВЫВОДИТЕ НА ЭКРАН СУММУ ДВУХ СОСЕДНИХ ЧИСЕЛ.
# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# n = len(numbers)
# for i in range(n):
#     print(numbers[i-1]+numbers[(i+1) % n], end=' ')
# _________________________________________________________________________________________________________________
# ЗАДАНИЕ 2:
# В PYTHON ЕСТЬ МОДУЛЬ DATETIME А В МОДУЛЕ ЕСТЬ ОСОБЕННЫЕ ФУНКЦИИ КОТОРЫЕ ПОКАЗЫВАЮТ НАСТОЯЩЕЕ ВРЕМЯ.
# С ПОМОЩЬЮ МОДУЛЯ DATETIME ВЫВЕДИТЕ НА ЭКРАН СКОЛЬКО ВРЕМЕНИ В ДАННЫЙ МОМЕНТ.
# import datetime
#
# dt = datetime.datetime.now()
# print(dt)
# _________________________________________________________________________________________________________________
# ЗАДАНИЕ 3:
# В PYTHON ЕСТЬ МОДУЛЬ TIME, С ПОМОЩЬЮ НЕГО МОЖНО ОТПРАВЛЯТЬ ПРОГРАММУ В СОН.
# ЗАПУСТИТЕ ЦИКЛ FOR I IN RANGE(10) И КАЖДЫЙ ШАГ ЦИКЛА ВЫЗЫВАЙТЕ
# ФУНКЦИЮ МОДУЛЯ TIME КОТОРАЯ ЗАСТАВЛЯЕТ ПРОГРАММУ ЗАСНУТЬ.
# import time
#
# for i in range(10):
#     print("Программа проснется через: ", i)
#     time.sleep(1)
# _________________________________________________________________________________________________________________
# ЗАДАНИЕ 4:
# В PYTHON ЕСТЬ ВСТРОЕННАЯ ФУНКЦИЯ КОТОРАЯ ПОЗВОЛЯЕТ ОБЪЕДИНЯТЬ ДВА СПИСКА ДЛЯ ЦИКЛА FOR.
# list_a = [1,3,5,7,9,11,13]
# list_b = [2,4,6,8,10,12,14]
#
# for i in list_b:
#     list_a.append(i)
#
# print(list_a)
# _________________________________________________________________________________________________________________
# ЗАПУСТИТЕ ЦИКЛ FOR С ДВУМЯ ПЕРЕМЕННЫМИ КОТОРЫЕ БУДУТ ПРОХОДИТЬ
# ПО LIST1 И LIST2 ОДНОВРЕМЕННО И ВЫВОДИТЕ ЭТИ ПЕРЕМЕННЫЕ НА ЭКРАН

# # Функция zip() в Python создает итератор, который объединяет элементы из нескольких источников данных.
# # Эта функция работает со списками, кортежами, множествами и словарями для создания списков или кортежей,
# # включающих все эти данные.
# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
#
# for i, j in zip(list1, list2):
#     print(i, j)