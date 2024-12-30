# Nested Loops in python

# OQ Que --->
# x = 20
# y = 25
# for i in range (1,5):
#  if (x + y)% 10 == 5 or y % 5 == 0:

#     for j in range (0,3):
#         y = y + 5
#     print(y)
    
#  elif x % 5 == 0 and y % 5 == 0:
#      x = x + i
#      print(x)
     
# print(x + y)

#  Que (2)
#  write a program to print factorial of every number till 15.
# ---->

# for i in range (1, 16):
#     f = 1
#     for j in range (1, i+1):
#        f = f * j
#     print("Your Factorial of", i, "is :",f)
    
    
# Que (3)
# write a program to print sum of all the prime number's from 1 to 100
# ---->

# f = 0
# s = 0
# for i in range (1, 101, 1):
#     if i == 1 :
#         continue
#     else:
#         for j in range (2, i):
#             if i % j == 0:
#                 f = 1
#                 break
#         if f== 0:
#             s = s +  i
#         f = 0
# print ( "Total sum of all prime number till 100 is :", s)

# Que (4)
#  write a program to print a pattern
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    
# ---->

# for i in range (0, 6):
#     for j in range ( i + 1):
#         if (i == 1):
#             print ( "*" )
#             break
        
#         elif (i == 2):
#             print("* *")
#             break
#         elif (i == 3):
#             print("* * *")
#             break
         
#         elif (i == 4):
#             print("* * * *")
#             break
         
#         elif (i == 5 ):
#             print("* * * * *")
#             break
         
for i in range (0, 6):
     for j in range (1, i + 1):
         print ("*", end=" ")
         
print(end = "/n")
         
         
        
