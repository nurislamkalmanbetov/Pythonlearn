# Nurislam 02.02.2023
# Задание 1:
# 1.  Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

# a = 0
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         a += i
# print(a)
# ____________________________________________________________
# Задание 2
# 1. Написать скрипт который проходится по ключам и проверяет значения
# a) Если значение делиться на 3, то записываем строку “Hi”
# b) Если значение делиться на 5, то записываем строку “Bye”
# ПРИМЕР:
# Дано -> dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# Результат -> a = Bye
# b = Hi

# d = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# for key, value in d.items():
#     if value % 3 == 0:
#         print(key, "= Hi")
#     elif value % 5 == 0:
#         print( key, "= Bye")
#     else:
#         print(key, "= None")
# ___________________________________________________________________
# 2
# 1 Напишите программу, которая берёт текст и выводит два слова:
# 2.Наиболее часто встречающееся
# 3.Cамое длинное

# text = '''
# В 1960-е годы в СССР начались попытки запускать аппараты к Венере в рамках космической программы «Венера».
# Первый пуск был неудачными, но уже второй аппарат Венера-1 достиг зоны действия тяготения планеты,где с ним было потеряна связь — он пролетел на расстоянии 100 000 км от поверхности.
# В 1965 году результат был уже лучше — 24 000 км.Венера-4 доставила спускаемый аппарат и смогла получить данные о давлении,
# что использовали при построении следующих аппаратов.Венера-7 впервые совершила мягкую посадку на другую планету — в 1970-м году.
# А Венера-9 в 1975 году впервые передала телевизионную панораму с Венеры на Землю.'''
# s1  = set(text)
# res = 0
# for i in s1:
#     if text.count(i) > res:
#         res = text.count(i)
# print(res)



# words = text.split()
# word_counts = {}
# for word in words:
#     word_counts[word] = word_counts.get(word, 0) + 1
#     most_common_word = max(word_counts, key=word_counts.get)
# longest_word = max(words, key=len)
#
# print("Most common word:", most_common_word)
# print("Longest word:", longest_word)
# ______________________________________________________________________
# 3 Слияние словарей
# Напишите программу для слияния нескольких словарей в один.

# my_friends = {"Joomart": "+996555246810","Adinai": "+996555013579","Ermek": "+996777013579","Atai": "+996777246810",
#  "Aslan": "+996999246810"}
# his_her_friends = {"Lyazat": "+996551123456","Salavat": "+996552234567","Daniyar": "+996553345678",
# "Bolot": "+996554456789","Alymbek": "+996555501234","Dastan": "+996556678912","Maksat": "+996557789012",
#  "Aibek": "+996558890123"}
# our_friends = {}
# print(our_friends.update(my_friends))
# print(our_friends.update(his_her_friends))
# print(our_friends)
# 2 example
# our_friends = {**my_friends, **his_her_friends}
# print(our_friends)
# ________________________________________________________________________
# Задание 3
# 1. Даны списки:
# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # Нужно вернуть список, который состоит из элементов, которые есть либо только в первом, либо только во втором
# print(list(set(list_1 and list_2)))
# __________________________________________________________________________
# 2.
# list_1 = [2, 8, 1, 2, 5, 3, 4, 6, 7, 9, 10, 8, 11, 17, 13]
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в
# последовательности или NO, если не встречалось.
# list_1 = [2, 8, 1, 2, 5, 3, 4, 6, 7, 9, 10, 8, 11, 17, 13]
# s = set()
# for num in list_1:
#     if num in s:
#         print(num, "YES")
#     else:
#         s.add(num)
#         print(num, "NO")
# ___________________________________________________________________________