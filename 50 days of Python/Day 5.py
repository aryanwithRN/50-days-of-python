# for i in range (1, 10, 1):
#     print(i)

# ---->
# n=90 
# for i in range (0,5):
#     print((n+i)%2)
# print(n)    

# Que(1)
# write a program to print sum of all the even numbers till 100
# ---->
# for Even,
# n=0
# for i in range (2 ,101, 2):
#     n = n+ i
#     print(n)

# For Odd,
# n=0
# for i in range (1 ,101, 2):
#      n = n+ i
#      print(n)

#OQ-->
# x = 50
# y = 12
# for i in range (1,10):
#     if (x+y)// 2 > 30 and (x+y)// 2 < 42:
#         x=x-2
#         y= x - y
#         print(x)
#         print(y)
#     elif x % 2 == 0 and y%3 == 0:
#         print (y+10)
#     else:
#         print(x)
#         print(y)
# print(x)
# print(y)
    
        


# Que (3) write a program if a entered number is prime or not.

# entered_number = int(input("Enter a Number: "))
# flag= 0
# for p in range (2, entered_number):
#        if (entered_number % p == 0):
#             flag = 1
# if (flag == 0):
#     print("prime")
# else:
#     print("Not a Prime")
  
  
  
  
    
#Que (4) write a program to take a input from the user and print its factorial(!)

# enter_number = int ( input("Enter a Number: "))
# f = 1
# for i in range (1, enter_number + 1):
#     f = f * i
# print(f)


# write a program to take a number as a input and check if its factorial is prime number or not.

enter_number = int (input("Enter a number: "))
f = 1
for i in range (1, enter_number, -1):
    f = f * i
    print(f)
flag= 0
for f in range (2, f):
    if(enter_number % i == 0 ):
        flag = 1
      
if flag == 0 :
    print ("Prime")

