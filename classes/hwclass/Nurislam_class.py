# ____________________________________________________________________________________________________________________

# Нужно создать класс который примет модель ноутбука(Acer, Asus, ...) и возвращает полную комплектацию ноутбука
# со всеми характеристиками.
# В характеристики должны входить:
# 1 Процессор
# 2 Оперативная Память
# 3 Видео карта
# 4 Жёсткий Диск
# 5 Материнская плата
# 6 Размер экрана
# Для каждой характеристики создайте внутри класса функцию которая добавляет по одной характеристики к Dictionary.
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены: Модель Ноутбука и его Характеристики.
# class Laptop:
#     def __init__(self, model):
#         self.model = model
#         self.add_dict = {}
#
#     def add_processor(self, processor):
#         self.add_dict['Процессор'] = processor
#
#     def add_ram(self, ram):
#         self.add_dict['Оперативная Память'] = ram
#
#     def add_graphics_card(self, graphics_card):
#         self.add_dict['Видео карта'] = graphics_card
#
#     def add_hard_drive(self, hard_drive):
#         self.add_dict['Жёсткий Диск'] = hard_drive
#
#     def add_motherboard(self, motherboard):
#         self.add_dict['Материнская плата'] = motherboard
#
#     def add_screen_size(self, screen_size):
#         self.add_dict['Размер экрана'] = screen_size
#
#     def get_specs(self):
#         return {self.model: self.add_dict}
#
# laptop1 = Laptop('Acer Nitro 5')
# laptop1.add_processor('Intel Core i5-9300H')
# laptop1.add_ram('8 GB DDR4')
# laptop1.add_graphics_card('NVIDIA GeForce GTX 1650')
# laptop1.add_hard_drive('256 GB SSD')
# laptop1.add_motherboard('Acer Nitro AN515-54')
# laptop1.add_screen_size('15.6"')
# print(laptop1.get_specs())
# # Вывод: {'Acer Nitro 5': {'Процессор': 'Intel Core i5-9300H', 'Оперативная Память': '8 GB DDR4', 'Видео карта': 'NVIDIA GeForce GTX 1650', 'Жёсткий Диск': '256 GB SSD', 'Материнская плата': 'Acer Nitro AN515-54', 'Размер экрана': '15.6"'}}
#
# laptop2 = Laptop('Asus ZenBook UX425')
# laptop2.add_processor('Intel Core i7-1165G7')
# laptop2.add_ram('16 GB LPDDR4X')
# laptop2.add_graphics_card('Intel Iris Xe')
# laptop2.add_hard_drive('512 GB PCIe NVMe SSD')
# laptop2.add_motherboard('Asus ZenBook UX425EA')
# laptop2.add_screen_size('14"')
# print('\n\n\n\n',laptop2.get_specs())
# # Вывод: {'Asus ZenBook UX425': {'Процессор': 'Intel Core i7-1165G7', 'Оперативная Память': '16 GB LPDDR4X', 'Видео карта': 'Intel Iris Xe', 'Жёсткий Диск': '512 GB PCIe NVMe SSD', 'Материнская плата': 'Asus ZenBook UX425EA', 'Размер экрана': '14"'}}
# ___________________________________________________________________________________________________________________

# Нужно создать класс который принимет данные в формате dict. Эти данные, вы сможете взять из Classroom Data #1.
# Вам нужно создать 6 методов класса:
# Получить все ключи в TUPLE.
# Получить все значения в TUPLE.
# Получить все ключи в LIST.
# Получить все значения в LIST.
# Получить все ключи в SET.
# Получить все значения в SET.
# Ниже когда вы будете передавать Словарь классу и вызывать из него любой метод Вы должны получать соответсвенно
# нужные типы данных.
# Example: my_class = Parser("DICT") | my_class.get_keys_tuple()

# class ColorData:
#     def __init__(self, colors_dict):
#         self.colors = colors_dict
#
#     def get_keys_tuple(self):
#         return tuple(self.colors.keys())
#
#     def get_values_tuple(self):
#         return tuple(self.colors.values())
#
#     def get_keys_list(self):
#         return list(self.colors.keys())
#
#     def get_values_list(self):
#         return list(self.colors.values())
#
#     def get_keys_set(self):
#         return set(self.colors.keys())
#
#     def get_values_set(self):
#         return set().union(*self.colors.values())
#
#
# colors = {
#     "black": {
#         "category": "hue",
#         "type": "primary",
#         "code": {
#             "rgba": [255, 255, 255, 1],
#              "hex": "#000"
#         }
#     },
#     "white": {
#         "category": "value",
#         "code": {
#             "rgba": [0, 0, 0, 1],
#             "hex": "#FFF"
#         }
#     },
#     "red": {
#         "category": "hue",
#         "type": "primary",
#         "code": {
#             "rgba": [255, 0, 0, 1],
#             "hex": "#FF0"
#         }
#     },
#     "blue": {
#         "category": "hue",
#         "type": "primary",
#         "code": {
#             "rgba": [0, 0, 255, 1],
#             "hex": "#00F"
#         }
#     },
#     "yellow": {
#         "category": "hue",
#         "type": "primary",
#         "code": {
#             "rgba": [255, 255, 0, 1],
#             "hex": "#FF0"
#         }
#     },
#     "green": {
#         "category": "hue",
#         "type": "secondary",
#         "code": {
#             "rgba": [0, 255, 0, 1],
#             "hex": "#0F0"
#         }
#     }
# }
#
# color_data = ColorData(colors)
# keys_tuple = color_data.get_keys_tuple()
# values_tuple = color_data.get_values_tuple()
# keys_list = color_data.get_keys_list()
# values_list = color_data.get_values_list()
# keys_set = color_data.get_keys_set()
# values_set = color_data.get_values_set()
# print('N1-Получить все ключи в TUPLE: ', keys_tuple)
# print('\nN2-Получить все значения в TUPLE: ', values_tuple)
# print('\nN3-Получить все ключи в LIST: ', keys_list)
# print('\nN4-Получить все значения в LIST: ', values_list)
# print('\nN5-Получить все ключи в SET: ', keys_set)
# print('\nN6-Получить все значения в SET: ', values_set)
# ________________________________________________________________________
# 3


