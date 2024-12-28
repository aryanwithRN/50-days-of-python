# SUPER
# class A:
#     def __init__(self):
#         self.x = 10
#         self.y = 20
#     def display_a(self):
#         print(self.x)
#         print(self.y)


# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.a = 40
#         self.b = 50
#     def display_b(self):
#         print(self.a)
#         print(self.b)

# # main

# b1 = B()
# b1.display_a()
# b1.display_b()


# NAME MANGLING

# class A:
#     def __init__(self):
#         self.__x=10
#         self.y=20
#     def display_A(self):
#         print(self.__x)
#         print(self.y)
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.a=70
#         self.b=80       
#     def display_B(self):
#         print(self.a)
#         print(self.b)
# #main
# A1=A()
# B1=B()
# A1._A__x = 90
# A1.display_A()
# B1.display_B()


