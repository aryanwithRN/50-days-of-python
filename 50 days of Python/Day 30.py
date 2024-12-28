# ---------------------------------------------------------------  EXCEPTION HANDLING  -----------------------------------------------------------------------------------
# Try Block (1 times)
# Except Block(Multiple times)
# Else Block(1 time)
# Finally(1 time)

# Ex-
# try:
#     x =9
#     y = 0
#     s = x//y
#     print("Good!")
# except:
#     print("Division by 0 is not possible")

# Ex-2 
# try:
#     a = int(input("Input 1: "))
#     b = int(input("Input 1: "))
#     s = a + b
#     print("Here is Your Output", s)
# except:
#     print("Input Not valid You add int with string")


# Ex - 3
# try: 
#     ls = [1,2,3,4]
#     index = int(input("Enter Index You want to print: "))
#     if index in ls:
#      print(ls[index])
# except:
#     print("Index Thoda Kam kar Bhai")


# Ex - 4
# try: 
#     input = int(input("Enter a Number: "))
#     if input < 0:
#      raise ValueError("Ayein Baigan-  Negative value" )
#     f=1
#     for i in range(1,input+1):
#         f = f * i
#     print("Here Is Your Factorial value",f)
# except ValueError as VE:
#         print(VE)
# except:
#     print("Unexpecte Error")

# EX - 5

# try:
#     height = int(input("Enter Height: "))
#     base = int(input("Enter Base: "))
#     s = 1/2 * (height * base)
#     print ("Area Of Triangle is", s)
# except ValueError:
#     print("You Enter Non-Numeric Value")

# EX - 6
# Develop a program that checks whether a given word entered by the user is a palindrome. Handle cases where the user enters something other than a word.
# try: 
#     input = input("Enter a Input: ")
#     if input.isnumeric():
#         raise ValueError("Integer Value Not allow")
#     if input == input[::-1]:
#         print("palendrome")
# except ValueError as VE:
#     print(VE)

# Write a program that converts temperatures between Celsius and Fahrenheit based on user input. Handle cases where the user enters non-numeric values.

# try: 
#     temperatures = int(input("Enter Temperture: "))
#     user_select = input("convert to C/F: ")
#     if user_select != "C" or user_select !="F":
#         raise ValueError("It Must be C/F")
#     if user_select == "C":
#         s = (temperatures * 9/5)+32
#         print(s,"is Your Fahrenheit")
#     elif user_select == "F":
#         s1 = (temperatures-32)* (5/9) 
#         print(s1, "This Is Your Celsius")
# except ValueError as VE:
#     print(VE)
# except:
#     print("You Enter Invalid input and it Look like Non- Numeric value")


# Implement a program that takes a string input from the user and prints its length. Handle cases where the user enters something other than a string.
# try:
#     user_input = input("Enter a String: ").lower()
#     if user_input.isalnum():
#         raise ValueError("You Not enter String")
#     if user_input.isalpha():
#         s = len(user_input)
#         print("Length of string is", s)
# except ValueError as VE:
#     print(VE)
# except:
#     print("Error hai bhai")


# OP-1
# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# else:
#     print(f"Result: {x}")
# finally:
#     print("Finally block executed.")

# # OP-2
    
# try:
#     my_list = [1, 2, 3]
#     value = my_list[5]
# except IndexError:
#     print("Index out of range!")
# except Exception as e:
#     print(f"An error occurred: {e}")

# # OP-3

# try:
#     number = int("abc")
#     result = 10 / number
# except ValueError:
#     print("Invalid conversion to int.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except Exception as e:
#     print(f"An error occurred: {e}")