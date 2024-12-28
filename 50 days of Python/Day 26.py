# LAMBDA Fn-
# sum = lambda a,b: a + b
# print(sum(50,60))

# --------------------------------------------------------------QUE 1----------------------------------------------------------------------------
# Calculator using Lambda Fn-
# ---->
# lambda Fn:
# add = lambda number_1,number_2:number_1+number_2
# Sub = lambda number_1,number_2:number_1-number_2
# Multi = lambda number_1,number_2:number_1*number_2
# Dvd =lambda number_1,number_2:number_1/number_2
# mod =lambda number_1,number_2:number_1 % number_2
# select_power =lambda number_1,number_2:number_1 ** number_2

# number_1 = int(input("Enter a Number:"))
# number_2 = int(input("Enter second Number:"))
# select_operations = input("Enter Operation +, -, *, /, %, ""select Power - # :")
# if select_operations == "+":
#     print(add(number_1,number_2))
# elif select_operations == "-":
#     print(Sub(number_1,number_2))
# elif select_operations == "*":
#     print(Multi(number_1,number_2))
# elif select_operations == "/":
#     print(Dvd(number_1,number_2))
# elif select_operations == "%":
#     print(mod(number_1,number_2))
# elif select_operations == "#":
#     print(select_power(number_1, number_2))

# --------------------------------------------------------------QUE 2-------------------------------------------------------------------------------

# WA-lambda Fn to concatinate 2 string.
# ---->
# concatinate = lambda user_input_1, user_input_2: user_input_1 + user_input_2
# user_input_1 = input("Enter String 1: ")
# user_input_2 = input("Enter String 2: ")
# print(concatinate(user_input_1,user_input_2))

#---------------------------------------------------------------QUE 3-----------------------------------------------------------------------
 
# # check even odd
# ---->
# check_prime_odd = lambda n:"Even" if n % 2 == 0  else "odd"
# print(check_prime_odd(12))

#---------------------------------------------------------------QUE 4 -------------------------------------------------------------------------------- 

# WA Lambda Fn- to check the input is in +ve, -ve or 0:
# ------>
# check_number = lambda n : "Positive" if n > 0  else "Negative" if n < 0 else "0"
# user_input = int(input('Enter a Number: '))
# print(check_number(user_input))

#--------------------------------------------------------------QUE 5-----------------------------------------------------------------------------

# WA Lambda Fn to check if a given string is palendrome or not
# ------->
# check_palendrome = lambda n :"palendrome" if n == n[: : -1]   else "Not palendrome" 
# user_input = input("Enter a Number: ")
# print(check_palendrome(user_input)) 

# -------------------------------------------------------------QUE 6 ------------------------------------------------------------------------------------

# WA Lambda-Fn to check and print the grater value amoung the Two numbers
# -------->
# check_grater = lambda number_1,number_2: "Number 1 is Grater than Number 2" if number_1> number_2 else "Smaller Than Number 2"
# number_1 = int(input("Enter a Number_1: "))
# number_2 = int(input("Enter a Number_2: "))
# print(check_grater(number_1,number_2))

# -------------------------------------------------------------QUE 7 --------------------------------------------------------------------------------------------

# WA Lambda-Fn to check if a string start with "a" and ends with "o"
# ------>
# check_A_O = lambda user_input: "YES it Start with a and end with o "  if user_input[0] == "a" and user_input[-1] == "o" else "Not Start with a and end with o"   
# user_input = input("Enter a String: ")
# print(check_A_O(user_input))

# ----------------------------------------------------------QUE 8 ---------------------------------------------------------------------------------------------------------

# WA lambda-Fn to print avg of all the element present in a list 
# ------->
# AVG = lambda ls: sum(ls)/ len(ls)
# n = int(input("Enter Length of lsit: "))
# ls=[]
# for i in range (0, n):
#     x = int(input("Enter Numbers:"))
#     ls.append(x)
# print(AVG(ls))

# ----------------------------------------------------------QUE 9 -----------------------------------------------------------------------------------------------------------
# WA lambda-Fn to check if the number is prime or not
# ----->
# check_prime = lambda n : "PRIME "if  n > 1 and all(n%i != 0 for i in range (2,n)) else "Not prime"
# n = int(input("Enter a Number: "))
# print(check_prime(n))

# -----------------------------------------------------------QUE 10 ---------------------------------------------------------------------------------------------- 
# WA lambda-Fn to print factorail of user's input
# ----->
# factorail = lambda n: 1 if n ==0 else n * factorail(n-1)
# n = int(input("Enter a Number: "))
# print(factorail(n))

# ----------------------------------------------------------QUE 11----------------------------------------------------------------------------------------------
# WA lambda-Fn to print the squares of all the element present in a list
# ------->
# square_of_all_elements = lambda ls : [x ** 2 for x in ls] 
# n = int(input("Enter Length of lsit: "))
# ls=[]
# for i in range (0, n):
#     x = int(input("Enter Numbers:"))
#     ls.append(x)
# print(square_of_all_elements(ls))