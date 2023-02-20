# isinstance - проверяет является экземпляр класса 

# class Dog():
#     pass

# dog = Dog()
# isinstance(dog, Dog)
# ________________________________________________________________________________
# Принципы ООП
# Имеется четыре принципа ООП
# 1) Наследование
# 2) Инкапусляция
# 3) Полиморфизм
# 4) Астракция

# Наследование в ООП

# class A():

#     def __init__(self) -> None:
#         self.name = "Class A"

#     def get_something(self):
#         print("I am method from class A")
# # Класс А - это родительский класс от которого унаследовался, класс В
# # Класс В - это подкласс или субкласс, который наследует все от класс

# class B(A):
#     pass 

# b = B()
# b.get_something()
# print(isinstance(b, A))
# ________________________________________________________________________________

# Виды наследование:
# 1) Множественное наследование
# 2) Многоуровневое наследование свыше превышение одного 

# Примеры Многоуровневое наследование 
# class A():
#     pass

# class B(A):
#     pass

# class C(B):
#     pass
# ________________________________________________________________________________
# Примеры Множественное наследование
# class A():
#     pass

# class B():
#     pass

# class C():
#     pass

# class D(A, B, C):
# ________________________________________________________________________________
# Примеры 

# class Animal():

#     def _get_noise(self):
#         pass

#     def get_move(self):
#         pass

# class Cat(Animal):
#     def get_noise(self): #Наследник Animal, родительский метод get_noise может использовать и наследник
#         print("Myow Myow Myow")

#     def move(self):
#         print("Ходит на четверынках")

# cat = Cat()
# cat.get_noise()


# class Bird(Animal):

#     def get_noise(self):
#         print("chik chik")

#     def move(self):
#         print('flying')

# bird = Bird()
# bird.get_noise()
# ________________________________________________________________________________

# class Human():
#     def __init__(self, name, age, type):
#         self.name = name
#         self.age = age
#         self.type = type


#         def say(self):
#             print('Eating')

#         def move(self):
#             print('Moving')

# class Child(Human):
#     def say(self):
#         print("Crying")

#     def move(self):
#         print("running")

#     def play(self):
#         print("playing with toys")

# class Adult(Human):
#     def __init__(self, name, age, type, cash, salary, is_maried):
#         super().__init__(name, age, type)   
#         self.cash = cash
#         self.salary = salary
#         self.is_maried = is_maried

#     def say(self):
#         print(f'Hello! My name is {self.name}!')

#     def move(self):
#         print("going with 2 legs")

#     def earn(self):
#         self.cash += self.salary
#         print("Yor banace now: ", self.cash)

# adult = Adult("Askar",30,"Male",10000, 30000, False)
# adult.earn()
# adult.say()
# child = Child("Osmon",1,"male",)
