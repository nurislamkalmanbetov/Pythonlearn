# 06.02.23
# Всроенные функции - len(), print(), input()
# all()
# Функция которая принимает Iterable Object и проверяет все ли объекты являются True.
# any()
# Функция которая принимает Iterable Object и проверяет если хотябы один объект в списке явлеются True.
# abs()
# Возвращает число в АБСОЛЮТНОМ значении.
# min()
# Возвращает самый маленький по значению объект из набора данных.
# eval()
# Позволяет исполнить Python code из Строки.
# reversed()
# Возвращает ЗАКРЫТЫЙ Список данных - которые записаны в обратном порядке.
# max()
# Возвращает самый большой по значению объект из набора данных.
# slice()
# Позволяет создать ОБЪЕКТ СРЕЗА и применять его настройки для выреза данных.
# round()
# Округляет значение числа до задонного места.
# ___________________________________________________________________________
# results = [False,False,False,True,False,False]
# salaries = [17740,11000,8000,12500]
# print(any(results)) # проверяет, хотябы одно True
#
# salaries = [17740,11000,8000,12500]
# slice_range = slice(1,4)
# print(salaries[slice_range])
#
# results = [False,False,False,True,False,False]
# salaries = [17740,11000,8000,12500]
# print(all(results)) # проверяет, все ли значения являются True
#
# salaries = [17740,11000,8000,12500]
# print(max(salaries))
#
# print(eval('salaries[:2]'))

# print(round(17.819324712, 3))

# print(abs(-31)) #на минус дает плюс, на плюс дает плюс. То есть, переварачивает, в положительном ввиде

# salaries = [17740,11000,8000,12500]
# print(list(reversed(salaries)))

# t = input('enter code: ')
# print('type(t): ', type(t))
# print('t: ', t)
# print('t: ', t)
# r = eval(t)
# print('type(r): ', type(r))
# print(('r: ', r))
# ______________________________________________________________
# nums = [1,'2',3,'4','ба',7,'8',1,2]
#
# #  for i in range(1,9):
# #     if int(i) % 2 == 0:
# #        print(nums[8]/i)
#
# try:
#     for i in range(-5,5):
#         if int (i) % 2 == 0:
#             print(nums[7]/i)
#
# except NameError  or IndexError as exep:
#     print('Found error in code!')
#     print('exep: ', exep())
# except (IndexError, IndexError) as i_e:
#     print('Найдена ошибка!')
#     print(i_e)
# except ZeroDivisionError as z_d_e:
#     print('Найдена ошибка!')
#     print(z_d_e)
# else:
#     print('я работаю в любом случае else')
# finally:
#     print('я работаю в любом случае finaly')
#
# print('error')

# ___________________________________________________________________________
# # 1 Скопируйте текст к себе на компьютер:
# Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.

# # 2 Monthes:
# January       18000
# February      32641
# March         28300
# April         11200
# May           21100
# June          19000
# July          8000
# August        72000
# September     12300
# October       17000
# November      25000
# December      30000
# ___________________________________________________________________________________________
