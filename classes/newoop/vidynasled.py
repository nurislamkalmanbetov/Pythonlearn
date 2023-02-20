# Виды наследование 
# class A():

#     def __init__(self, type):
#         self.type = type

#     #метод это функция объявленная внутри класса 
#     def get_name(self):
#         print("A class")


# class B(A):

#     # метод overwrite - переписывание метода в наслуемом классе
#     def get_name(self):
#         print("B class")

# b = B("Classeeeee")
# b.get_name()
# _______________________________________________________________________
# Множественное наследование 
# MRO - method resolution order
# class A():
    
#     def move(self):
#         print("Method from AAAA")

# class B():

#     def move(self):
#         print("Method from B")

# class C(B):
#     pass

# class D(A,C):
#     pass 

# print(D.mro())

# d = D()
# d.move()
















