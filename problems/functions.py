# 1
# Создайте функцию которая которая берёт лист делит его пополам и обе стороны разворачивает в противоположную сторону.
# Пример:Оригинальный Лист:
# list_1 = ['name', 'age', '1', '19']
# Изменённый Лист:
# list_1 = ['age', 'name', '19', '1']

# list_1 = ['name', 'age', '1', '19']
#
# def reverse_and_split_list(list_1):
#     half = len(list_1) // 2
#     first_half = list_1[:half][::-1]
#     second_half = list_1[half:][::-1]
#     return first_half + second_half
#
# print(reverse_and_split_list(list_1))
# ________________________________________________________________________________________________________
# 2
# Создайте функцию которая генерирует 10 чисел Фибоначчи:
# 1,1,2,3,5,8,13,21,34,...
# n = []
# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# data = list(fibonacci(10))
# print(data)
# ________________________________________________________________________________________________________
# 3
# Создайте функцию сложения, затем функцию вычитания двух чисел...
# Создайте 3-ю функцию которая вызывает первые 2 внутри себя.

# def add(a,b):
#     return a + b
#
# def minus(a,b):
#     return a - b
#
# def add_minus(a,b):
#     result1 = add(a, b)
#     result2 = minus(a, b)
#     print(result1,result2)
#
#
# add_minus(10,5)
# ________________________________________________________________________________________________________
# 4
# 1.
# Спросите у пользователя имя файла. Создайте функцию которая создаёт файл с именем которое передал пользователь.
# Присвойте ИМЯ функции к переменной и вызывайте функцию через переменную.


