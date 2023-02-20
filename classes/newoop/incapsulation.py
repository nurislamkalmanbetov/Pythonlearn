# Инкапсуляция
# Виды инкапсуляции:
# 1. Публичный - Public
# 2. Приватный - Privat "__" в начале 2 нижнего пробела
# 3. Зашищенный - Protected "_" 1 защищенный

# class Person():
#     def __init__(self,name,age,salary) -> None:
#         self.name = name # публичный атрибут
#         self.__cash = 0 # "__" в начале 2 нижнего пробела - Приватный \ необязательно указывать в __init
#         self._age = age # защищенный
#         self._salary = salary # защищенный

#     # как добавить деньги, если защищенный метод покрывает?
#     # Приватный метод
#     def __add_cash(self, amount):
#         self.__cash += amount

#     # метод для добавления денег защищенного метода
#     def get_salary(self):
#         self.__add_cash(self._salary)
#         print("Вы получили зарплату!")
#         print("Ваш текущий счет: ", self.__cash)

        
#     # Зашищенный
#     def _get_age_info(self):
#         print(f"{self.name} is {self._age} years old. ")


# person = Person("Askar", 22, 25000)
# print(person.name)
# print(person._age)

# person.get_salary() # Добавление ЗП для защищенного дейтсвия
# person._get_age_info() # Узнать сколько лет у приватной функции 

