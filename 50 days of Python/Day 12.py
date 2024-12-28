# # # write a program to take  a string as input from the user and an integer too. If the entered value of integer 
# # is 1 then print all the vowels in uppercase which are present in the string,if the value is 0 then print all 
# # the consonants present in the string in lower case, and if value is -1 then print all digits and special characters 
# # present in the string.

# stg_input = input("ENter a String: ").lower()
# int_input = int(input("Enter an integer: "))

# for i in stg_input:
    
#     if (int_input == 1) and (i == "a"or i == "e"or i == "i"or i == "o" or i == "u"):
#         print(i.upper())
    
#     elif (int_input == 0)  and not(i == "a"or i == "e"or i == "i"or i == "o" or i == "u"):
#         print(i.lower())
        
#     elif (int_input == -1) and not(i.isalpha()):
#         print(i)
        
    
# # Write a program to take string as a input and replace all digits in the string with "$" and  print the new string
# # input_str = input ("Enter a String: ")
# # for i in input_str:
# #     if i.isdigit():
# #         print("$", end = "")
# #     else:
# #         print(i, end = "")


# # Write a Python program to count occurrences of an entered character in a string.

# str_input = input("Enter a string: ").lower()
# input_Charct = input("Enter a specific Character: ").lower()
# c = 0

# for i in str_input:
#     if i == input_Charct:
#      c=c+1
# print(c)
    
# # Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', 
# #except the first char itself.
# # ---->
    
# # str_input = input("Enter a string: ").lower()
# # a=str_input[0]
# # for i in range(0, len(str_input)):
# #     if i==0:
# #         print(str_input[i], end = "")
# #     else:
# #         if str_input[i] == a:
# #             print("$", end="")
# #         else:
# #             print(str_input[i], end = "")


# # write a program to take two int inputs swap the values of both the them

# # a = int1 = int(input("Enter a value: "))
# # b = int2 = int(input("Enter a value: "))
# # print(int1)
# # print(int2)

# # print("Reverse Value")
# # c = b 
# # b = a
# # a = c

# # print(a)
# # print(b)

# # or
# # a = int1 = int(input("Enter a value: "))
# # b = int2 = int(input("Enter a value: "))
# # a,b=b,a
# # print(a,b)


# # Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# # Sample String : 'abc', 'xyz'
# # Expected Result : 'xyc abz
# a =  (input("Enter a string: "))
# b =  (input("Enter a string: "))
# # a = "abc" 
# # b = "xyz"
# d = a[0:2] 
# d1 = b[0:2]
# d,d1 = d1,d
# c = a.replace(a[0:2], d)
# c1 = b.replace(b[0:2], d1)
# print(c, c1)
