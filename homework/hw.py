# problem1
# print(17925 > (34**2))
# print(17925 > (26*3))
# print(17925 > (17*3))
# print(17925 > (4394*4))


# problem2
# print('A>B', 'A<C')
# print(7%3*4.8)
# print(True == True)
# print((5+2) != (2+6))

# problem3
# print(5+5)
# print(5*5)
# print(5**2)
# print((5+5)+(5*5)+(5**2)-193432)

# problem4
# print('(17*3)>(12*5)', (17*3)>(12*5))
# print((12**3) > (13*7))
# print((4**5) == (512+512))

# problem5
# print(-21//10)

# problem8
# a = 23
# b = 100
# print((a/b) * 100)

# problem9
# a = 1996
# b = 2022
# print('In 2024, your age will be - ', b - a + 2)

# problem10
# a = (25+75+10+95)
# print(a/205)

# problem14+13
# a = 4
# b = 5
# c = 6.1
# d = 3
# e = 1
# print((a-e**(b/d))%c)

# problem17
# a = 2.1
# b = 2.1
# c = 2.1
# print((a+b)*c)
# ________________________________________
# 1.Поделите 17531 на 3 и узнайте сколько раз оно делится?
# x = 17531
# result = x // 3
# print(result)
# 2.Что больше: Количество троек в числе 17531 или число 5821?
# 3.Если остаток деления 4388 на 7 больше или равно 4 - умножьте остаток на 7.
# 4.Если остаток деления 4292 на 5 меньше или равно 3 - разделите остаток на 3.
# 5.Распишите по порядку шаги исполнения выражения: 7 + 5 * (3 * (27**3))
# 6.Сколько получится если:
#   1. От 183 отнять 17
#   2. Разделить 19
#   3. Добавить 13.6
#   4. Результат умножить на 2
#   5. И всё это поделить по модулю 12

# 1
# print(17531/3)
# 2
# number1 = 17531
# number2 = 5821
# count1 = str(number1).count('3')
# count2 = str(number2).count('3')
# if count1>count2:
#     print('Количество троек в числе',number1,'больше чем в числе',number2)
# else:
#     print('Количество троек в числе',number2,'больше чем в числе',number1)
# 3
# a = (4388%7)
# b = (a >= 4)
# c = a*7
# print(a, b, c)
# 4
# a = 4292%5
# print(a<=3)
# print(a/3)
# 5
# print(((27**3)*3)*5+7)
# 6
# Сколько получится если:
#   1. От 183 отнять 17
# print(183-17)
#   2. Разделить 19
# print(166/19)
#   3. Добавить 13.6
# print(8.7+13.6)
#   4. Результат умножить на 2
# print(22.2*2)
#   5. И всё это поделить по модулю 12
# print(44.4/12)
# либо же
# print(((((183-17)/19)+13.6)*2)%12)