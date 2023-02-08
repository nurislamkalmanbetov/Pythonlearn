# DICT {}
# d = dict{}
# print(type(d))

# .clear()
# Удаляет всё из библиотеки.
# .get("*")
# Получить значение по *.
# .keys()
# Возвращет список всех ключей.
# .values()
# Возвращает список всех значение.
# .items()
# Возвращается список ключей и их значений.
# .update("*")
# Берёт множетсво и обновляет или дополняет к нему ключи из *

# food = {}
# Наполненный словарь:
# food = {
#     "drinks": {
#         'name': 'Pepsi'
#     },
#     "snacks": ['Potato', 'Cheeps'],
#     '[2,4]': 'fvdf',
#     5: 6,
#     4.3: {5,3,7}
# }
# print(len(food))
# print(food.get('snacks'))
# print()
# print(food.get('fvdf'))
# _____________________________________
# Наполненный словарь:
# food = {
#     "drinks": {
#         'name': 'Pepsi'
#     },
#     "snacks": ['Potato', 'Cheeps'],
# }
# print(food)
# print(len(food))
# print(food.update({'drinks': 'drinks'}))
# print(food.get('snacks'))
# print(food.keys()) - # все ключи
# print(food.values()) - # все значения
# print(food.items())  # возвращает ключи и значения
# print()
# print(food)
# print(set(food))
# s1 = set(food)
# print(tuple(s1))
# print(food['snacks']) #food.get('snacks')
# print(food.get('trrrrr'))
# food['newkey'] = 'test value'
# print(food)