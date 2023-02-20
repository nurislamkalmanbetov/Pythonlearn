# Дандер методы и перезагрузка методов

# Дандер - методы, которые контролируют поведенеи класса и его объекта
# __init__ - dander method  "главное обозначение, это двойные подчеркивания с двух сторон"__" "

# class A():

#     def __init__(self,name) -> None:
#         self.name = name
    
#     def __str__(self) -> str: # Возвращает Имя объекта \ можем давать имена объектов
#         return self.name
    
#     def __len__(self):
#         return len(self.name) # Изменяет поведение объекта при применении к объекту функции len()
    
#     def __iter__(self): # __iter__ - всегда рабоает вместе с yield \ мдает возможность итерацию к объекту
#         for i in self.name:
#             yield i 

#     def __eq__(self, other) -> bool: # если объекты равны одному тому же классу - то будет True 
#         if isinstance(other, A):
#             return True
#         return False

# a = A('Nurislam')

# # for i in a:  # __str__
# #     print(i)
# # print(a)
# # print(len(a))  #__len__

# # a2 = A("Abdurachkami-Abdulla")
# # print(len(a2))

# a2 = A('Aaaaaaaaaaaaaa') # __eq__ - проверка класса, относится ли к тому классу равно ( == )
# print(a == a2)
# _____________________________________________________________________________________________________

# class Number():

#     def __init__(self,n) -> None:
#         self.n = n

#     def __add__(self, other): # поменяли поведения объекта через дандер __add__ - метод
#         if isinstance(other, Number):
#             return self.n + other.n
#         elif type(other) == int:
#             return self.n + other 
#         else:
#             raise TypeError("Invalid Data!")
        
# n1 = Number(150)
# print(n1 + 250)

# n2 = Number(500)
# print(n1 + n2)

# print(n1 + 5,5) 
# _____________________________________________________________________________________________________

# class Students():

#     def __init__(self, students_list) -> None:
#         self.student_list = students_list

#     def __contains__(self, student): # Bool values - True or False/ проверяет есть ли ил нет
#         if student in self.student_list:
#             return True
#         return False
    
# students = Students(["Ermek", "Tilek","Muslim","Temirlan"])
# print("Ermek" in students)
# _____________________________________________________________________________________________________

# class B():
#     def __init__(self, name) -> None:
#         self.name = name

#     def __call__(self): # *args 
#         return "Я объект класса, меня вызвали через ()"
    
#     def __add__(self, other):
#         if isinstance(other,B):
#             return self.name + other.name
#         raise TypeError()
    

# b = B("Barsbek")
# print(b())
# print(b.__call__())

# b2 = B("Bektur") # __add__ - добавление
# print(b2+b)
# print(b.__add__(b2))




















