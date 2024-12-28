# -------------------------------------------------------------Que 1-------------------------------------------------------------------------
# Wa-Fn To check where the list is harshad num or not.

# Fn:
# def harshad_number(x):
#     num = x
#     sum = 0
#     while x > 0:
#         sum = sum + x % 10
#         x = x //10

#     if num % sum == 0:
#         return(num,"It's Harshad Number")
#     else:
#         return(num, "Not Harshad Number")

# # # main
# ls = []
# user_input = int(input("Enter Lenght of list: "))
# for i in range (0, user_input):
#     x = int(input("Enter a Number: "))
#     ls.append(x)
# for i in ls:
#     rev = harshad_number(i)
#     print(rev)


# ------------------------------------------------------------OP QUE 1-----------------------------------------------------------------------
# def A(x):
#     j = 5
#     for i in range(x):
#         j = j + i
#         print(j)
#     if j > 10:
#         return(B(j+2))
# def B(Y,Z):
#     if Y % Z >= 5:
#         return(Y + Z)
#     elif Y // Z >= 0 and Y//Z <= 7:
#         return Y
    
# # main
# x = 10
# for i in range(x):
#     res = A(x)
#     print(res)
# if res >= 10:
#     res1 = B(res,x)
#     print(res1)

#-----------------------------------------------------------QUE 2--------------------------------------------------------------------------
# Fn-
def Search_Emp(x):
 for key, values in d1.items():
    if Search_Dept in d1.keys():
         d1[Search_Dept]= Dept
         if Search_Role in d1.keys():
              d1[Search_Role]= Role
 return(key,values)
 
# main
d1={}
user_input= int(input("Enter Length OF Dict: "))
for i in range(0,user_input):
    keys = input("Enter Name:")
    Age = input("Enter Your Age: ")
    Salary = input("Enter your Salary: ")
    Role = input("Enter your Role: ")
    Dept = input("Enter your Dept: ")
    values = {Age, Salary, Role, Dept}
    d1[keys]=values
print(d1)

Search_Dept = input("Search Emp By Dept: ")
Search_Role = input("Search Emp By Role: ")

for i in d1.keys():
        res = Search_Emp(d1[i])
        print(res)


# -------------------------------------------QUE 3----------------------------------------------------------------------------------------
# WA-Fn to generate 2 string from a given string for 1st string use  the charachtes that  occurs only once for the 2nd string use the 
# charachter that occure multiple times.


# Fn-
# def string_(str):
#     st1 = ""
#     st2 = ""
#     for j in str:
#         count = str.count(j)
#         if ( count == 1):
#             st1 += j
#         else:
#             st2 += j        
#     print(st1)
#     print(st2)
        
# # main
# string1 = input("Enter String: ")

# print(string_(string1))