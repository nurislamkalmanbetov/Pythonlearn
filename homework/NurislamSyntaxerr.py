# 1 задания
# Представьте Вы хотите взять какой-то набор данных и переконвертировать его в SET для удаления дубликатов,
# в Classroom возьмите values и проверьте каждый ли элемент доступен для конвертации. Создайте список.
# Проитерируйте values. Если объект в списке можно переконвертировать добавьте True в новый список иначе добавьте False.
# После, с помощью функции all() скажите можно ли конвертировать values в SET?

# values = ("Razakov 32",{4,8}, 10, 1005, ["tables", "chairs"], 23.00)
# # print(set(values))
# result = list()
# for value in values:
#     if type(value) in (int, str, float, tuple, bool):
#         result.append(True)
#     else:
#         result.append(False)
# print(result)
# if all(result):
#     print('Yes')
# else:
#     print('Net')

# ______________________________________________________________________
# 2
# Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел.

# numbers = set()
# for i in range(5):
#     num = int(input('Введите 5 чисел: '))
#     numbers.add(num)
# print(numbers)
# print('Маленькое число: ', min(numbers))

# ______________________________________________________________________
# 3
# Представим Вы создали сайт онлайн курсов по Python. Ваша задача спросить у пользователя Python ФУНКЦИЮ и если
# такая есть исполнить и вернуть пользователю результат иначе сказать что в Python такой функции нет!

# try:
#     function_name = input("Введите функцию в Python. Для выхода - 'exit': ")
#     try:
#         function_name = eval(function_name)
#         print("Result:", function_name)
#     except:
#         print("В Python такой функции нет!")
#
# except:
#     print("Что-то пошло не так")
# ______________________________________________________________________
# 4

# Вы работаете в Банке и пишите программу которая считает % для кредита. Спросите у пользователя сумму
# займа(не меньше 50 000) и посчитайте сколько нужно будет вернуть если % = 3.47, результат округлите
# до 2 чисел после точки.
# Формула подсчёта переплаты: Сумма * (% / 100)

# amount = float(input('Ваша сумма займа: '))
# if amount < 50000:
#     print('Займ, должен быть свыше 50000: ')
# else:
#     procents = 3.47
#     interess = amount * (procents / 100)
#     total = amount + interess
#     print('Общяя сумма: ', total)
# ______________________________________________________________________
# 5
# Напишите код где есть TypeError,IndexError,NameError.

# TypeError example
# a = 10
# b = "20"
# c = a + b
# print(c)

# IndexError example
# list1 = [1, 2, 3, 4, 5]
# print(list1[10])

# NameError example
# print(x)
# ______________________________________________________________________
# 6
# Возьмите код #1 с Classroom и создайте для него try... except...
# Создайте несколько except выражений для разных типов ошибок.

# a = 10
# i = 15
# wo = 20
#
# try:
#     for e in range(-a, a):
#         print(wo, e)
#         if a > 5:
#             print("a > 5",a)
# except:
#     print('No')
# ______________________________________________________________________
# 7
# Перенесите к себе код #2 с Classroom и исправьте все ошибки, сделайте так чтобы работал.
# Если не знаете как исправить ошибку создайте для неё except выражение.
# example 1
# lst = []
# for i in range(10):
#     lst.append(i)
#
# a = list(reversed(lst))
# sls_obj = slice(0, 8)
# print(a[sls_obj]) #a - русская клавиатура была... 🤨
# example 2
# try:
#     lst = []
#     for i in range(10):
#         lst.append(i)
#
#     a = list(reversed(lst))
#     sls_obj = slice(0, 8)
#     print(a[sls_obj])
# except:
#     print('Не работает код')
# ______________________________________________________________________
# 8
# Перенесите к себе код #3 с Classroom и исправьте все ошибки, сделайте так чтобы код работал.
# Если не знаете как исправить ошибку создайте для неё except выражение.

# a = 0
# b = (1,) #Tuple
# numbers = []
# while b > a:
#     numbers += b
# b += 1

# Выполнение
# try:
#     a = 0
#     b = 1
#     c = 1000
#     numbers = []
#     while b > a and c > 0:
#         numbers.append(b)
#         b += 1
#         c -= 1
#         print(b)
# except:
#     print('Не работает код')
# finally:
#     print('Вообще нет')
# ______________________________________________________________________
# 9
# Дан словарь в котором ключи должны быть только строковыми объектами, но может встретиться Int,
# как в качестве ключа, но ваша проверка только проверяет на строку и поэтому у вас выходит баг,
# ваша задача обработать исключением ошибку TypeError
# Пример:
# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# for x in dict_.keys():
# x + 'abc'
# 1.Запустить код
# 2. Обработайте исключение
# example 1
# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# for key, value in dict_.items():
#     print(key,value)
# example 2
# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# for x in dict_.keys():
#     print(str(x) + 'abc')
#     print(str(x).split(' '))
# example 3
# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# try:
#     for x in dict_.keys():
#         x + 'abc'
# except TypeError:
#     print('asfasg')