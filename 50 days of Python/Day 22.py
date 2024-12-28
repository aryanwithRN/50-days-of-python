# Functions-->
# def sum (a,b):
#  s = a + b
#  return s
# # main
# a = sum(60,50)
# print(a)

# OQ Question 1 :
# def funct1(a,b):
#     while a<b:
#         print(a+5)
#         a+=1
#         b-=1
#     return b + 2
# # main
# a = 3
# b = 5
# x = funct1(a,b)
# print(x)
# y = funct1(a+1, b+3)
# print(y)

# OQ Question 2 :

# def func(a:int , b:int):
#     if a < b:
#         return a + 10
#     else:
#         return b - 5
    
# # main
# x = 4
# y = 10
# for i in range (x,y):
#     if (i%2==0):
#         x = func(i + 2, y-4)
#     else:
#         print("HELLO")
# print(x)

# ----------------------------------------------------Que(1)----------------------------------------------------------------------
# WAP to build Calculator  (+,-, * ,/)

# function
# def add(a:int,b:int):
#     s = a + b
#     return s

# def sub(a:int,b:int):
#     s = a - b
#     return s

# def multi(a:int,b:int):
#     s = a * b
#     return s

# def div(a:int,b:int):
#     s = a / b
#     return s

# Main
# a = int(input ("Enter a Number: "))
# b = int(input ("Enter a Number: "))
# c = input("Select Operation + , - , * , / : ")
# if (c == "+"):
#     x = add(a,b)
#     print(x)
# elif (c == "-"):
#     x = sub(a,b)
#     print(x)
# elif (c == "*"):
#     x = multi(a,b)
#     print(x)
# elif (c == "/"):
#     x = div(a,b)
#     print(x)






# ----------------------------------------------------Que(2)------------------------------------------------------------------------------------------------
# WAF to take Number as a input form the user and return the factorial of that perticular factorial of the number.
# --->
# function
# def fact (a:int)->int:
#     f=1
#     for i in range ( 1 , a+1):
#         f = f * i
#     return f
# # Main
# a = int(input ("Enter a Number: "))
# x = fact (a)
# print(x)