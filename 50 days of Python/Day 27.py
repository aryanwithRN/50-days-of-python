
# --------------------------------------------------------------------OP-1-----------------------------------------------------------------------------------
# a = [1, 2, 3]
# b = [x for x in a if x > 1]
# print(b)

# --------------------------------------------------------------------OP-2----------------------------------------------------------------
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# closure = outer(10)
# result = closure(5)
# print(result)

# --------------------------------------------------------------------OP-3-------------------------------------------------------------------------------
# def modify_list(lst):
#     lst.append(4)
#     lst = [1, 2, 3]
#     return lst

# my_list = [5, 6, 7]
# result = modify_list(my_list)
# print(my_list)

# ---------------------------------------------------------------------OP-4--------------------------------------------------------------------
# def add_numbers(a, b=0, c=0):
#     return a + b + c

# result = add_numbers(1, c=2)
# print(result)

# ---------------------------------------------------------------------OP-5------------------------------------------------------------------------------
# def process_data(data):
#     data[0] = "Processed"
#     return data

# my_data = ["Raw", 2, 3]
# result = process_data(my_data)
# print(result)

# --------------------------------------------------------------------OP-6---------------------------------------------------------------------------
# def operate(a, b, operation="+"):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b

# result = operate(5, 3, operation="*")
# print(result)

# --------------------------------------------------------------------OP-7---------------------------------------------------------------------------
# def modify_tuple(tup):
#     tup = (4, 5, 6)
#     return tup

# my_tuple = (1, 2, 3)
# result = modify_tuple(my_tuple)
# print(my_tuple)
# --------------------------------------------------------------------OP-8---------------------------------------------------------------------------
# def modify_dict_values(d):
#     d = {'a': 1, 'b': 2}
#     for key in d:
#         d[key] *= 2
#     return d

# my_dict = {'x': 10, 'y': 20}
# result = modify_dict_values(my_dict)
# print(result)
# --------------------------------------------------------------------OP-9------------------------------------------------------------------------------
# def func(a, b, c=0, *args):
#     return a + b + c + sum(args) 

# result = func(1, 2, 3, 4, 5, 6, 7)
# print(result)

# -----------------------------------------------------------QUE-1-----------------------------------------------------------------------------------------
# WA Lambda-Fn which of the list elements is even or odd
# "odd" if user_input== 1 "Even" if user_input % 2 == 0 else "Odd"
# Check_even_odd = lambda j: "Even" if j % 2 == 0 else "Odd"  
# user_input= int (input("Enter Length: "))
# ls=[]
# for i in range (0, user_input):
#     x = int(input("Enter Numbers:"))
#     ls.append(x)
# res = [Check_even_odd(j)for j in ls]
# print(res)