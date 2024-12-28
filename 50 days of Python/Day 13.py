# Que ( 1 )
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing', add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# input_str = input("Enter a String: ")
# s = input_str[-3:]

# if len(input_str)>=3:
#     if s == "ing":
#         print(input_str + "ly")
#     elif s != "ing":
#         print(input_str + "ing")
# else:
#     print(input_str)

# Que ( 2 )
# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string instead.
# input_str = input("Enter a String:  ")
# d = input_str[0:2]
# d1 = input_str[-2: ]
# print(d+d1)

# Que ( 3 )
# Write a Python program to find the all the non-repeating character in a given string 
# and create a new string using those
# name = input("Enter a String:  ")
# a=""
# for i in name:
#     c =0
#     for j in name:
#         if i == j:
#             c=c+1
#     if c==1:
#         a=a+i
# print(a)
    
# Que ( 4 ) 
# Write a Python program to find the second most repeated word in a given string.
# ---->
# for i in string:
#     c = 1
#     for j in string:
#         if i == j:
#             a=a+i
#     if c == 0:
#         continue
# print(a)

# string = input("Enter a String:  ")
# string2= ""
# a = 1
# for i in string:
#     c = 0
#     for j in string:
#         if i == j:
#             c=c+1
#     if c > a:
#         a = c
#         string2 = i
# print("highest occuring is", string2, "and it's count is", a)
    
    
# Que ( 5 )        
# Write a Python program to generate two strings from a given string. For the first string,
# use the characters that occur only once, and for the second, use the characters that occur multiple 
# times in the said string.
# ----->
# name = input("Enter a String:  ")
# a=""
# a1=""
# for i in name:
#     c =0
#     for j in name:
#         if i == j:
#             c=c+1
#     if c==1:
#         a=a+i
#     else:
#         a1 = a1 + i
# # print("First repeted string:",a1)
# print("Second remaining String:",a)

# write a program to find the all non repeating characters in a given string and create a new string using those

# name = input("Enter a String:  ")
# a=""
# for i in name:
#     c = 0
#     for j in name:
#         if i == j:
#             c=c+1
#     if c==1:
#         a=a+i
# print("New String is:",a)