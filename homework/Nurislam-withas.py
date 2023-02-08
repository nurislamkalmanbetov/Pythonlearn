# 1
# С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога. Если у вас Windows,
# сделайте тоже самое))) Только с помощью команды dir. В итоге у вас на рабочем столе должен появиться файл
# directories.txt. Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.
import os

# with open('directories.txt', 'w') as file:
#     for i in range(5):
#         s = input('Введите слово: ')
#         file.write(s+'\n')
#
# with open("/home/hpadmin/Desktop/ITCbootcamp/homework/directories.txt", "r") as f:
#     for line in f:
#         print(line.strip())
# _______________________________________________________________
# 2
# Создайте файл users.txt. Напишите программу которая спрашивает
# у пользователя его Логин и Пароль и записывает в файл users.txt.

# with open('users.txt', 'w') as file:
#     for i in range(1):
#         s = input('Введите Ваш логин: ')
#         b = input('Введите Ваш пароль: ')
#         file.write(s+'\n')
#         file.write(b+'\n')
# _______________________________________________________________
# 3
# Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то выведет
# на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.

# my_fileW = open('text.txt', 'w')
# my_fileW.write('We are Wakanda!')
# my_fileW.close()
#
# with open('text.txt', 'r') as file:
#     text = file.read()
# if 'w' in text.lower():
#     print('Да, в тексте есть w')
# else:
#     print('Нет, в тексте нет w')
# _______________________________________________________________
# 4
# Создайте текстовый файл python.txt и запишите в него текст #1 из Classroom:
# Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит
# букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,
# выведите на экран все полученные слова. Подсказка: используйте for.

# with open('python.txt', 'r') as file:
#     text = file.read()
# t_words = []
# words = text.split()
# for word in words:
#     if 't' in word.lower():
#         t_words.append(word)
#
# if t_words:
#     print('Слова в котором есть буква "t": ', t_words)
# else:
#     print('No')
# _______________________________________________________________
# 5
# Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя
# войти или зарегистрироваться. Спросите его логин и пароль. Если такой логин уже есть скажите ему
# что логин уже существует и предложите авторизоваться спросив пароль. Если такого логина неоказалось
# среди уже существющих продолжайте регистрацию. Спросите у него Пароль 2 раза и сохраните в
# в файл datebase.txt только если пароли совпадают.

# login = input('Введите логин:')
# password = input('Введите пароль:')
#
# f = open('database.txt', 'w')
# f.write(f'Логин - {login}'
#         f'\nПароль - {password}')
# f.close()
#
# with open("database.txt", "w") as f:
#     f.write("user1,password1\n")
#     f.write("user2,password2\n")
#     f.write("user3,password3\n")
#
# print("Please enter 'login' or 'sign up'")
# user_choice = input().lower()
#
# if user_choice == "login":
#     print("Enter your login and password separated by a comma")
#     login, password = input().split(",")
#
#     with open("database.txt", "r") as f:
#         lines = f.readlines()
#         found = False
#         for line in lines:
#             line_login, line_password = line.strip().split(",")
#             if line_login == login:
#                 found = True
#                 if line_password == password:
#                     print("Login Successful")
#                 else:
#                     print("Incorrect Password")
#         if not found:
#             print("This login does not exist")
# elif user_choice == "sign up":
#     print("Enter a new login and password separated by a comma")
#     login, password = input().split(",")
#     with open("database.txt", "r") as f:
#         lines = f.readlines()
#         found = False
#         for line in lines:
#             line_login, line_password = line.strip().split(",")
#             if line_login == login:
#                 found = True
#                 print("This login already exists, please try another one")
#                 break
#     if not found:
#         print("Enter your password again")
#         password2 = input().strip()
#         if password == password2:
#             with open("database.txt", "a") as f:
#                 f.write(f"{login},{password}\n")
#                 print("Sign up successful")
#         else:
#             print("Passwords do not match, please try again")
#
# else:
#     print("Invalid choice, please try again")
# example 2
# print("Войдите или зарегистрируйтесь!")
# log = input("Ваш логин: ")
# password = input("Ваш пароль: ")
# users = ''
# with open("database.txt", 'r') as f1:
#     users = f1.read()
#     print('file: ', users)
# database = dict()
#
# for user in users.split('\n'):
#     print(user)
#     database.update(eval(user))
# print('after: ', database)
#
# if log in database:
#     if database[log] == password:
#         print("Вы вошли!")
#     else:
#         print("Пароль не верен!")
# else:
#     password_2 = input("Введите пароль еще раз: ")
#     if password_2 == password:
#
#         print("Поздравляю вы зарегестрировались")
#         with open("database.txt", "a") as f:
#             f.write('\n')
#             f.write(str({log: password_2}))
#     else:
#         print("Пароли должны совпадать!!!")
# _______________________________________________________________
# 6
# Создайте форму регистрации которая спрашивает у пользователя: Логин, Пароль и Фото. Заранее подготовьте
# фото на компьютере и когда программа спросит ваше фото просто укажите полный путь до места где лежит ваше фото.
# Программа должна проверить если фото правда существует по такому пути
# И также это фото с одним из 3 расширений("jpeg", "jpg", "png") то вы сохраняете в файл логин, пароль,
# путь до фото которое указал пользователь. А самому пользователю вы говорите о том что Регистрация Успешна!
# login = input("Enter your login: ")
# password = input("Enter your password: ")
# photo_path = input("Enter the path to your photo: ")
#
# with open("/home/hpadmin/Desktop/Nurislam/Nuris.png", "r") as f:
#     for i in f.readlines():
#         print(i)

# with open('Nuris.txt', 'w') as file:
#     for i in range(1):
#         login = input("Enter your login: ")
#         password = input("Enter your password: ")
#         photo_path = input("Enter the path to your photo: ")
#         file.write(login+'\n')
#         file.write(password+'\n')
#         file.write(photo_path+'\n')
# _______________________________________________________________
# 7
# Напишите программу которая спрашивает от пользователя 2 вещи:
# 1.Путь до картинки которую нужно изменить.
# 2.Путь до картинки НА которую нужно изменить.
# Если оба пути существуют перепишите первую картинку на вторую,
# если нет скажите пользователю какая картинка не существует.

# directory = "/home/hpadmin/Desktop/Nurislam"
# files = os.listdir(directory)
# print(files)

