# 1 Задача
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# Выведите среднию температуру за неделю
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# average_temp = sum(week_temp)//len(week_temp)
# print("Средняя температура за неделю: ", average_temp,'C')

# 2 Задача
# Есть кортеж: a  = (4,2,5,8,6,9)
# измените 8 на 11
# a  = (4,2,5,8,6,9)
# a = list(a)
# a[3] = 11
# a = tuple(a)
# print(a)

# 3 Задача
# a  = (4,2,5,8,6,9) - Переставьте обратно
# a = (4, 2, 5, 8, 6, 9)
# a = a[::-1]  # reverse the tuple
# print(a)
# print(list(reversed(a))) # 2nd example

# 4 Задача
# LIST №1 удалите дубликаты из списка
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# a = list(set(week_temp))
# print(a)

# 5 Задача
# LIST №3 переставьте максимальное  и минимальное значение местами
# a = [4,2,5,8,6,9]
# a[a.index(min(a))], a[a.index(max(a))] = a[a.index(max(a))], a[a.index(min(a))]
# print(a)

# a = [8,16,2,3,4,1,5,15,16]
# print(a.index(min(a)))
# print(a.index(max(a)))
# x = max(a)
# y = min(a)
# print(x, y)
# a[a.index(y)] = x
# a[a.index(x)] = y
# print(a)

