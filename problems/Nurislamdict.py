# Nurislam 01.02.2023
# ____________________________________________________________________________________________________________________
# PROBLEM 000:
# Из Dictionary №1: Словарь №1: menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# Добавьте в меню
#  'besh_barmak' который стоит  130 сом.
# Оказалось лагман слишком дешевый. Обновите цену на 135
# Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо. Удалить borsh

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# print(menu.update({'besh_barmak': '130 som'}))
# print(menu.update({'besh_barmak': 135}))
# menu.pop('borsh')
# print(menu)
# # _________________________________________________________________________________________________________________
# PROBLEM 10:
# Из Dictionary №1: menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# Добавьте в меню напитки как ключ "drinks",
# А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu.update({'drinks': None})
# menu['drinks'] = 'Coca-Cola', 'Sprite', 'Fanta'
# print(menu)
# # _________________________________________________________________________________________________________________
# PROBLEM 020:
# Создайте SET который хранит в себе все методы  для работы  с  SET.
# Создайте второй SET который хранит в себе  методы  для работы  с  Dictionary которые вы сегодня узнали.
# Проверьте какие методы похожи у этих типов данные.
# set_metods = {"add", "clear", "copy", "difference", "difference_update", "discard", "intersection",
#                "intersection_update", "isdisjoint", "issubset", "issuperset", "pop", "remove", "symmetric_difference",
#                "symmetric_difference_update", "union", "update"}
# dict_metods = {"clear", "copy", "fromkeys", "get", "items", "keys",
#                 "pop", "popitem", "setdefault", "update", "values"}
# same_methods = set_metods.intersection(dict_metods)
# print(same_methods)
# # _________________________________________________________________________________________________________________
# PROBLEM 31:
# Создайте пустой словарь.
# Запустите цикл который 3 раза спросит его имя и его пароль.
# Записывайте имя пользователя как ключ, а пароль как его значение.

# dict1 = {'Bekjan': 'programmist',
#          'Janybek': 'desing',
#          'Asel': 'teacher',
#          'Neymar': 'soccer player',
#          'Avtandil': 'student'}
# for a, profession in dict1.items():
#     print("Здравствуйте {0} Прекрасная профессия {1}".format(a,profession))
# # _________________________________________________________________________________________________________________
# PROBLEM 27:
# Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
# С помощь цикла for пройти вывести на экран строку:
# "Здравствуйте <Имя>  Прекрасная профессия <Профессия>"

# info_1 = {'Nurislam': 'Software Engineer','Aidos': 'Devops', 'Aleksandr': 'Product manager',
#             'Bekjan': 'Project manager', 'Alisher': 'Golang Developer'}
# for name, profession in info_1.items():
#     print(f"Здравствуйте, {name}! Прекрасная профессия - {profession}.")  #{profession} - он сам появился??? Спросить
# # _________________________________________________________________________________________________________________
# PROBLEM 22:
# Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.
# Сделайте так чтобы эти данные уже никто не смог поменять позже.

# numbers = set()
# for i in range(10):
#     number = int(input("Введите ваше число: "))
#     numbers.add(number)
#     print(numbers)
    # в Тапл нужно было перевести
# Сделайте так чтобы эти данные уже никто не смог поменять позже - Как сделать?
# _________________________________________________________________________________________________________________
# PROBLEM 11:
# Есть список Южноамериканских стран
# Google Colab -  south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia','Ecuador', 'Guyana',
#                                             'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# в котором Суринам встречается два раза. Необходимо написать программу,
# которая удалит дублирующуюся запись, и возвратит в результате список

# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia','Ecuador', 'Guyana',
#                             'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# new_info = list(set(south_american_countries))
# print(new_info)
# _________________________________________________________________________________________________________________
# PROBLEM 101:
# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст:
# suitcase = []
# Однако он может вместить всего 5 вещей.
# Положите 5 вещей в чемодан.Вы передумали, и решили убрать последнюю вещь.

# suitcase = []
# suitcase.extend(["Зарядку", "Power-bank", "Духи", "Защиту 😁", "Гель для волос", "Туфли"])
# suitcase.pop() # pop() - удаляет только последнюю?! Спросить
# print(suitcase)
# example 2
# suitcase = []
# counter =0
# while counter <5:
#   veshi = input(f"Введите вещь: (counter+1): ")
#   suitcase.append(veshi)
#   counter +=1
# print(suitcase[:4])
# _________________________________________________________________________________________________________________
# PROBLEM 001:
# farm_1 = {"dog", "cat", "pig", "sheep"}
# farm_2 = {"chicken", "cat", "parrot", "pig"} # Вторую ферму, я сам прописал
# Напишите код, который: Выведет новое множество, которое есть как в
# первой ферме, так и во второй.

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"chicken", "cat", "parrot", "pig"}
# print("Есть в двух фермах: ", farm_1.intersection(farm_2))
# print("У второй есть: ", farm_2.difference(farm_1))
# _________________________________________________________________________________________________________________
# PROBLEM 100:
# farm_1 = {"dog", "cat", "pig", "sheep"}
# farm_2 = {"chicken", "cat", "parrot", "pig"} # Вторую ферму, я сам прописал
# Напишите код, который выведет новое множество, состоящее из животных,
# которые есть во второй ферме, но нет в первой.
# farm_1 = {"dog", "cat", "pig", "sheep"}
# farm_2 = {"chicken", "cat", "parrot", "pig"}
# print("Все животные, во второй ферме: ", farm_2)
# print("У второй фермы, есть, в отличии от первой фермы: ", farm_2.difference(farm_1))
# print("Нету у первой фермы: ", farm_1.intersection(farm_2))