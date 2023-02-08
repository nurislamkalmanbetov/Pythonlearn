# Типы данных
# int, float - Это(данные)

# STR - Это(данные)
#
# TUPLE - Это массив - где можно много цифр засунуть

# a = 'i am bob'
# print(a.split())

# Index
# a = 'i am bob'
# print(a.split()[2])

# a = 'we are bob and tom'
# b = a.split()
# print(len(b))
# print(b[3])
# print(b[:3])
# print(b[3:])
# print(b[2:4])
# print(b[-1])
# print(b[-2])
# __________________
# a = ['a', 'b', 'c'] # Кортеж - изменяется!
# b = ('a', 'b', 'c', 4, 5, 6) # Кортеж - НЕ изменяется!
# a.append(6)
# a[1] = 'k'
# print(a)
# _____________________
# a = ['Nuris', 'Edo', 'Aiba', 'Take']
# b = ('Johns', 'Borris', 'Backham', 'Brooklyn', 34, 44, 1)
# a.append('Nahui') # Добавляет
# print(a)
# _______________________
# a = ['Nuris', 'Edo', 'Aiba', 'Take']
# b = ('Johns', 'Borris', 'Backham', 'Brooklyn', 34, 44, 1)
# a.extend('Nahui') # Добавляет по одному элементу типа "N","a","h","u","i"
# print(a)
# _________________________
# a = ['Nuris', 'Edo', 'Aiba', 'Take']
# b = ('Johns', 'Borris', 'Backham', 'Brooklyn', 34, 44, 1)
# a.remove('Nuris') # Удаляет
# print(a)
# ___________________________
# a = ['Nuris', 'Edo', 'Aiba', 'Take']
# b = ('Johns', 'Borris', 'Backham', 'Brooklyn', 34, 44, 1)
# a.pop(1) # Удаляет временно
# print(a)
# ____________________________
# a = ['Nuris', 'Edo', 'Aiba', 'Take']
# b = ('Johns', 'Borris', 'Backham', 'Brooklyn', 34, 44, 1)
# a.index('Edo') # Возвращает удаленный элемент
# print(a)
# ____________________________
# list_numbers = [1,2,4,6,7,8,3,5,6]
# list_numbers.append(10)
# summ = sum(list_numbers)
# print(list_numbers)
#
# stroka = 'test user name'
# stroka.split(' ')
# print(stroka)