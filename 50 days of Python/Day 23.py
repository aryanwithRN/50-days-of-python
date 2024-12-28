# --------------------------------------------------------------------QUE 1 ----------------------------------------------------------------------------------------------
# WA-Fn to which has number of terms of a fibonaci serise as parameter and print's all the fibonaci terms with till the specified number of therms  

def fibseq (n:int)->int:
    t1 = 1 
    t2 = 1
    
    for i in range (1, n):
        print(t1)
        t3 = t1 + t2
        t1 = t2
        t2 = t3
    


# main

n = int(input("Enter a Number: "))
fibseq(n)

# --------------------------------------------------------------------QUE 2 ----------------------------------------------------------------------------------------------
# WA-fn which has a list as parameter and returns all the numbers which are even .
# fns
# soln 1
# def Ch_even (ls):
#     for i in ls:
#         if (i % 2 == 0):
#             print(i, "is Even")
#         else:
#             print(i, "Not Even")

# # main
# ls = []
# user_input = int(input("Enter Length of list: "))
# for i in range (0 , user_input):
#     x = int (input("Enter Numbers: "))
#     ls.append(x)
# print(ls)
# Ch_even(ls)


# soln 2

# # Fn
# def check_even (k:int)->int:
#     if k % 2 == 0:
#         return(f"{k} is even ")
#     else:
#         return(f"{k} is odd")
    
# # main
    
# ls = []
# user_input = int(input("Enter Length of list: "))
# for i in range (0 , user_input):
#     x = int (input("Enter Numbers: "))
#     ls.append(x)
# for i in ls:
#     res = check_even(i)
#     print(res)

# --------------------------------------------------------------------QUE 3 ----------------------------------------------------------------------------------------------
# Wa-fn to check the list has prime Number or Not

# Fn-
# def check_prime(x):
#     flag=0
#     for i in range(2,x):
#         if x % i == 0:
#             flag=1
#             break
#     if flag == 0:
#         return(f"{x} is prime")
#     else:
#         return(f"{x} is Not Prime")

# # main
# ls = []
# user_input = int(input("Enter Length of list: "))
# for i in range ( user_input):
#     x = int (input("Enter Numbers: "))
#     ls.append(x)
# print(ls)
# for i in ls:
#     res = check_prime(i)
#     print(res)

# --------------------------------------------------------------------QUE 4 ----------------------------------------------------------------------------------------------
# WA-Fn to check which of the numbers of a given list are prime adam.

# def adams_vala_number(x): 
#     rev = 0
#     rev1=0
#     sq = x ** 2
#     n=x
#     while x > 0:
#         d = x % 10
#         rev = rev * 10 + d
#         x = x // 10
        
#     sq1 = rev ** 2
#     while sq1:
#         d1 = sq1 % 10
#         rev1 = rev1 * 10 + d1
#         sq1 = sq1 // 10
    
#     if (sq == rev1**2):
#        return(check_prime(n))
#     else:
#         return("Not Adam Prime Number")
       
# def check_prime(x):
#         flag=0
#         for i in range(2,x):
#             if x % i == 0:
#                 flag=1
#                 break
#         if flag == 0:
#             return(f"{x} is Adam prime")
#         else:
#             return(f"{x} is Not  Adam Prime")


# # Main 
# ls=[]
# n=int(input("Enter length="))
# for i in range(0,n):
#     x = int(input("Enter a Number: "))
#     ls.append(x)
# for i in ls:
#     res=adams_vala_number(i)
#     print(res)