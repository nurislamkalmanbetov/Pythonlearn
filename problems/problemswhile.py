# 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована;
# for i in range (0,5):
#     print(i+1, '0')
# 2 Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран; (используем цикл while)
# a = 0
#sum = 0
# while a <= 100:
#     print(a)
#     sum+=1
#     a+=1
#print(sum)
# example 2
# print(sum(list(range(100))))
# 3 Дан список [2,5,2,-5,7,0,1,2,-3,-2,1,3,6,3]. Найти количество положительных чисел среди них;
# lst = [2,5,2,-5,7,0,1,2,-3,-2,1,3,6,3]
# count = 0
# for i in lst:
#     if i > 0:
#         count += 1
# print(count)
# 4 Перемножить все не чётные значения в диапазоне от 0 до 9435
# p = 1
# for i in range(1, 9435):
#     if i % 2 != 0:
#         p = p * i
#         print(p)
# 5 Записать в массив все числа в диапазоне от 54 до 9184 кратные 5;
# a = []
# for i in range(54,9185):
#    if i % 5 == 0:
#        a.append(i)
# print(a)
# ______________________________________________________________________
# Задача 1
# Есть список:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые больше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i > 5:
#         print(i)
#Задача 2
# Есть набор чисел
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# Поделить каждое число из digits на 9 и вывести на экран.
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# while digits / 9:
#     print(digits)
# Задача 3
# Здесь замешаны разные типы данных. Если вы уверены что логика написана правильно, но оно всё равно
# не работает скорее всего вы справились с заданием
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2,
# которых нет в spisok_1.
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# for a in spisok_2:
#     if a not in spisok_1:
#         print(a)
# Задание 4:
# Дан список  целых чисел:
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# new_numbers = []
# for num in numbers:
#     if num > 0:
#         new_numbers.append(1)
#     elif num < 0:
#         new_numbers.append(-1)
#     else:
#         new_numbers.append(0)
# print(new_numbers)
# Задача 5