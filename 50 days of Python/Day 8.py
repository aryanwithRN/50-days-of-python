# Que (1)
# write a  program to take a number as a input and print sum of its digits.
# ---->


# take_value = int(input ("Enter a Number: "))
# s = 0
# while take_value > 0 :
#     j = take_value % 10 
#     s = s + j
#     take_value = take_value // 10 
# print (s)



# Que ( 2 )
# write a program to print digits of an entered number in reverse.
# ---->
#(soln 1)
# take_value = int(input ("Enter a Number: "))
# while take_value > 1 :
#     j = take_value % 10 
#     print ( j, )
#     take_value = take_value // 10 
# print(take_value)

# (soln 2)
# take_value = int(input ("Enter a Number: "))
# while take_value > 0 :
#     j = take_value % 10 
#     print ( j, end="")
#     take_value = take_value // 10 
    
# Que (3)
#  write a program to take two numbers as a input and print the greatest common diviser.
#  --->
# n1 = int(input("Enter a number : "))
# n2 = int(input("Enter a number : "))

# if n2 % n1 == 0 :
#     print (" GCD Is" , n1)
# else:
#     m = 1
#     for i in range (1 , n1):
#         if (n1 % i) == 0 and n2 % i == 0:
#             m = i
#     print("It is GCD", m )
# Que (4)   
# wirte a program to take a number as a input and print it reverse of the number
# input_1 = int(input("Enter a number you want to reverse: "))
# while input_1 > 0 :
#     j = input_1 % 10 
#     print ( j )
    
# take_value = int(input ("Enter a Number: "))
# n = 0
# while take_value > 0 :
#     j = take_value % 10 
#     n = n * 10 + j
#     print ( j, end="")
#     take_value = take_value // 10  

# Que (5)
# write a program to check the number is palandrom or not. 
# take_value = int(input ("Enter a Number: "))  
# n = 0
# while take_value > 0:
#        j = take_value % 10 
#        n = n * 10 + j
#        print ( j, end="")
#        take_value = take_value // 10  
#        if j == take_value:
#            print("it is plndrm")
#        else:
#            print("Not a Palandrome Number")
#            break
       
# take_value = int(input ("Enter a Number: "))
# rev = 0 
# n1 = take_value
# while take_value > 0 :
#     j = take_value % 10 
#     rev = rev * 10 + j
#     print ( j, end="")
#     take_value = take_value // 10 
# if (rev == n1):
#         print("It is palandrome")
# else:
#         print("Not a palandrome")