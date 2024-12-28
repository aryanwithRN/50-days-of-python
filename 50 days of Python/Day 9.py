# Qne (1)
# Write a program to take a number as a input and check if the count of digits for that number is prime or not
# ---->
# n = int(input("Enter a Number: "))
# count = 0
# i = 2
# while  n > 0:
#     d = n  % 10
#     count = count + 1
#     n = n // 10
# print(count)

# if (count == 1):
#     print("Not a Prime Number ")
    
# else:
#     t = 0
#     for a in range (2 , count):
#         t = 1
#         if (count % a)== 0:
#             print("Prime")
#             t = 0
#             break
            
#         else:
#             t = 1
#             print("Not a Prime")
#             break


# Qne (2)            
#  write a program to take an input and check if it is an armstrome or not.
# ---->

# number = n1 = n2= int(input("Enter a Number: "))
# count = 0
# s= 0
# while n1:
#     count = count + 1
#     n1 = n1 // 10 
# while number:
#     d = number % 10
#     s = s+ (d ** count)
#     number = number // 10 
# # print (s)
# if (s == n2):
#     print("It is an Armstrome")
# else:
#     print("Not an Armstrome")
    
# Qne (3)
# write a program to print sum of all the prime numbers bwtn 1 - 200
# ----->
# n = 200
# i = 2
# s = 0
# while i <= 200:
#     f=0
#     j=2
#     while j < i :
#         if i % j == 0:
#             f = 1
#             break
#         j=j+1
#     if f==0:
#         s = s +  i
#     i = i + 1
 
# print (" Total Number of sum is , ", s)


#  Qne (4)
# write a program to print factorial of all odd numbers till 20 using while loop 
# ---->
# i = 1
# j = 1
# f = 14
# while i < 21 :
#     if  i % 2  != 0:
#         f = i
#         while j < i:
#             f = f * i
#             j = j + 1
#         print ("Factorial of", i, "=", f)
#     i = i + 1
    