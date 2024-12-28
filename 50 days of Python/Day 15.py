# # Que ( 1 )
# # write a program to take 7 number as a input print the sum of first half of the list and seperate second  half of list
# # -->
# input_number = int(input("Enter a Number: "))
# ls = []
# s = 0
# s = input_number // 2
# print(s)

# for i in range (0, input_number):
#     x = int(input("Enter a Number:"))
#     ls.append(x)

# y = 0
# for j in range (0 , s): 
#     y = y + ls[j]
# print("The sum of First half is,", y)

# d = 0
# for k in range(s, input_number):
#     d = d + ls[k]
# print("The sum of Second half is,", d)


# # Que ( 2 )
# # WTP to take a list of 5 numbers and print the largest among them
# # -->
# user_input = int(input("Enter a  Number: "))
# ls = []
# x = 0
# for i in range (0, user_input):
#     x = int(input("Enter Number's: "))
#     ls.append(x)
#     if (i >= x):
#         x  = i
# print("This is largest value among the input = ", x)


# # Que( 3 )
# # WTP to take 10 values in list as a user input and print largest number in the first half of the list and 
# # second half of list
# # -->

# user_input = int(input("Enter a Number: "))
# ls = []
# d = user_input // 2
# for i in range (0 , user_input):
#     x  = int(input("Enter the Number's: "))
#     ls.append(x)

# max_ = 0
# for j in range (0, d):
#     if (ls[j] >= max_):
#         max_ = ls[j]
# print("The largest value of First half is: ", max_)

# max_1 = 0
# for k in range (d, user_input):
#     if (ls[k] >= max_1):
#         max_1 = ls[k]
# print("The largest value of Second half is: ",max_1)


# Que ( 4 )
# write a program to take 10 numbers as input in a list and check and print which numbers  are armstrong numbers.
# ---->
    
# n = int(input("Enter a Number: "))
# ls = [] 
# for i in range (0, n):
#      x = int(input("Enter Numbers: "))
#      ls.append(x)

# for i in range (0, n):
#     c = len(str(ls[i]))
#     n1=ls[i]
#     s = 0
#     while ls[i]>0:
#         d = ls[i]%10
#         s=s+(d**c)
#         ls[i]=ls[i]//10
#     if s == n1:
#         print("Armstrong = ", n1)

# WTP to take n words in a lists and print the longest word among them. 

# user_input = int(input("Enter a Number of Word you want: "))
# ls=[]
# for i in range (0, user_input):
#     x = str(input("Enter Words: "))
#     ls.append(x)
# max_ = 0
# for i in range (0, user_input):
#     c = len(str(ls[i]))
#     if c > max_ :
#         max_ = c
# print(x)


# WTP to take list of n elements with mixed typed elements i.e string and numerics, add and print the sum of all numeric value and a string 
# containing all the characters of word

# user_input = int(input("Enter a Number: "))
# ls=[]
# s = 0
# s1 = ""
# for i in range (0, user_input):
#     x = input("Enter an elements: ")
#     ls.append(x)
# for i in ls:
#     if i.isdigit():
#         s = s + int(i)
#     else:



#         s1 = s1 + i
# print("Sum of digits is,",s)        
# print("making string from elements, ",s1)

# WTP to take n words of a senetence as input in alist and then generate a string from it consisting of that sentence.

user_input = int(input("Enter a Number: "))
ls=[]
s = ""
for i in range (0, user_input):
    x = str(input("Enter an elements: "))
    ls.append(x)
    s = s + ls[i]+ " "
print(s)





