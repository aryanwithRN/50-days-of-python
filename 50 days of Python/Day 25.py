# ----------------------------------------------------------------QUE 1 --------------------------------------------------------------------

# WA-Fn that takes a tuple as input and return a  new tuple with the first and last element swapped.
# Fn-
# def swap_tuple (x):
#     t1= ()
#     s = ls[0],ls[-1]=ls[-1],ls[0]
#     t1=tuple(ls)
#     return(t1)

# # Main
# ls=[]
# user_input= int(input("Enter Length Of Tuple: "))
# for i in range (0, user_input):
#     x = input("Enter a Number: ")
#     ls.append(x)
# print(ls)
# res = swap_tuple(ls)
# print(res)


# --------------------------------------------------------------QUE 2 ------------------------------------------------------------------------

# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. WAF to ask user for their salary 
# and year of service and print the net bonus amount.
# Fn-
# def Discount(Emp_Salary,Emp_Service):
#     if Emp_Service >= 5:
#         s = Emp_Salary * 5 / 100
#         y = Emp_Salary + s
#         return ("Your Incremented Salary is", y)
#     else:
#         return("5 saal baad aana")

# # Main
# Emp_Salary= int(input("Enter Your Salary: "))
# Emp_Service= int(input("Enter Year Of Your Services: "))
# res = Discount(Emp_Salary, Emp_Service)
# print(res)

# --------------------------------------------------------------QUE 3 ---------------------------------------------------------------------
# WA-Fn To ask the user to enter the Totall purchase amount and calculate the discounted price base on the conditions:
# Conditions:-
# If the purchase amount is greater than $100, apply a 10% discount.
# If the purchase amount is between $50 and $100 (inclusive), apply a 5% discount.
# If the purchase amount is less than $50, no discount is applied.

# Fn-
# def Discount_(x):
#     if Total_Purchase_Amount > 100:
#         s = Total_Purchase_Amount * 10 / 100
#         y = Total_Purchase_Amount - s
#         return ("Congrats! Your Discounted Total 10 %, is", y)
#     elif Total_Purchase_Amount <100 and Total_Purchase_Amount > 50: 
#         s = Total_Purchase_Amount * 5 / 100
#         a = Total_Purchase_Amount - s
#         return("Congrats! Your Discounted Total 5 %, is",a)
#     elif Total_Purchase_Amount < 50:
#         return("No Discount For You, Your Total Is ", Total_Purchase_Amount)

# # Main
# Total_Purchase_Amount = int(input("Enter Your Total Amount: "))
# res = Discount_(Total_Purchase_Amount)
# print(res)

# -------------------------------------------------------------QUE 4-------------------------------------------------------------------------------
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not

# # Fn-
# def class_attended (class_attended, classes_held):
#     s = classes_held * 75 / 100
#     if class_attended > 75 :
#         return("You are Eligible to attend Exam")
#     else:
#         return("Come Next Year ")

# # Main
# classes_held = int(input("Enter Number of classes held: "))
# classes_attended = int(input("Enter Number of classes attended: "))
# res = class_attended(classes_attended,classes_held)
# print(res)

# -------------------------------------------------------------OP_QUE_1------------------------------------------------------------------------
# Fn-
# def X (a,b):
#     j = 0 
#     s = a + b
#     for i in range (a,b,2):
#         j = j + i
#         return y(j)
# def y (x):
#     if x % 5 > 4:
#         y(x-1)
#     else:
#         return (x + 5)

# # main
# res= X(10,16)
# print(res)
# if res > 8:
#     res1 = y(res+5)
#     print(res1)


