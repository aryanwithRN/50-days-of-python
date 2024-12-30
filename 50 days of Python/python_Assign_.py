
# -------------------------------------------------------------Que 1 ------------------------------------------------------------------
# 1. WAP to Swap the cases
# input: Www.HackerRank.com
# output: wWW.hACKERrANK.COM
# ------->
# user_input = input("Enter a Sntence: ").swapcase()
# print(user_input)

# -------------------------------------------------------------Que 2 ------------------------------------------------------------------
# 2.Count Even and Odd Numbers in a given list
# user_input = [1,2,3,4,5]
# for i in user_input:
#     if i % 2 == 0:
#         count = user_input.count(i)
#         print(f"Even Number in list: {count}")

#     elif i % 2 !=0 :
#         count = user_input.count(i)
#         print(f"Odd Number in list: {count}")

# -------------------------------------------------------------Que 3 ------------------------------------------------------------------
# 3. Squares of numbers in list
# -------->
# ls = [1,2,3,4,5]
# for i in ls:
#     s = i ** 2
#     print(f"Square of {i}: {s}")

# -------------------------------------------------------------Que 4 ------------------------------------------------------------------
# 4.Sum of numbers in tuple
# ---------->
# t = (1,2,3,4,5)
# s = 0
# for i in t:
#     s = s + i
#     print(f"sum of numbers in tuple , {s}")

# -------------------------------------------------------------Que 5 ------------------------------------------------------------------
# 5. Sum of Keys and Sum of Values
# ---------->
# d1 = {
#         1 : 1,
#         2 : 2,
#         3 : 3,
#         4 : 4,
#      }
# # sum of keys
# keys = sum(d1.keys())
# print(f"sum of keys in dict. is {keys}")

# # sum of values
# value = sum(d1.values())
# print(f"sum of values in dict. is {value}")

# -------------------------------------------------------------Que 6 ------------------------------------------------------------------
# 6.input: "this is a string"
# output: "this-is-a-string
# ------------->
# input = "this is a string"
# s = input.replace(" ", "-")
# print(s)

# -------------------------------------------------------------Que 7 ------------------------------------------------------------------
# 7.Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# ---------->
# user_input = input("Enter filename: ")
# print(f"{user_input}.py")

# -------------------------------------------------------------Que 8 ------------------------------------------------------------------
# 8. Write a python program to find the longest word IN Statement
# ----------> REPEATED

# -------------------------------------------------------------Que 9 ------------------------------------------------------------------
# 9. Write a Python program to read last n elements of a list
# ------> REPEATED
# -------------------------------------------------------------Que 10 ------------------------------------------------------------------
# 10.Write a Python program to count the frequency of words in a statement
# ------> REPEATED

# ------------------------------------------------------------- PART 2 -----------------------------------------------------------------

# -------------------------------------------------------------Que 1 ------------------------------------------------------------------
# 1. Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# --------->
# human_year = 24
# if human_year <= 2:
#     dog_years = human_year * 10.5
# else:
#     dog_years = 21 + (human_year * 4)   # 21 = (10.5 * 2)
# print("Dog's age in dog years:", dog_years)

# -------------------------------------------------------------Que 2 ------------------------------------------------------------------
# 2.Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# -------->
# ls = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# for i in ls:
#     s = type(i)
#     print(f"Type of {i} is {s}")

# -------------------------------------------------------------Que 3 ------------------------------------------------------------------
# 3. Write a Python program which iterates the integers from 1 to 30. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
#               fizzbuzz
#                   1
#                   2
#                   fizz
#                   4 
#                   buzz
# --------->
# for i in range (1 , 31):
#     if i % 3 != 0 and i % 5 != 0:
#             print(f"  {i}")
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"Fizzbuzz")
#     elif i % 3 == 0:
#         print(f" Fizz")
#     elif i % 5 == 0:
#         print(f" buzz")

# -------------------------------------------------------------Que 4 ------------------------------------------------------------------

# 4. Write a Python program to convert month name to a number of days. Go to the editor
# Expected Output:
# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                      
# No. of days: 28/29 days
# ----------->
# this_year = {
#             "January" : 31,
#             "February":"28/29", 
#             "March":31, 
#             "April":30, 
#             "May":31, 
#             "June":30, 
#             "July":31, 
#             "August":31,
#             "September": 30, 
#             "October": 31, 
#             "November":30, 
#             "December":31,
#             }
# ls_of_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# print(ls_of_month)

# user_input = input("Enter Month: ").capitalize()
# for k,v in this_year.items():
#     if k == user_input:
#         print(f"{k} have {v} days")

# -------------------------------------------------------------Que 5 ------------------------------------------------------------------
# 5.Write a Python program to extract year, month, date and time using Lambda.
# ---------->

# date_str = "20-08-2023"

# extt_year = lambda date_str: int(date_str.split('-')[2])
# ext_month = lambda date_str: int(date_str.split('-')[1])
# ext_date = lambda date_str: int(date_str.split('-')[0])

# year = ext_year(date_str)
# month = ext_month(date_str)
# date = ext_date(date_str)

# print("Year:", year)
# print("Month:", month)
# print("Date:", date)

# -------------------------------------------------------------Que 6 ------------------------------------------------------------------
# 6.Write a Python program to rearrange positive and negative numbers in a given list using Lambda.  **HOLD
# --------->
# list1 = [-1,-4,-9,0,1,5,2,-22]
# list1.sort()
# print(list1)
# -------------------------------------------------------------Que 7 ------------------------------------------------------------------
# 7. Write a Python program to get the third side of right angled triangle from two given sides.
# ---------->
# Height = int(input("Enter Height: "))
# Base = int(input("Enter Base: "))
# R_angle = (Base**2  + Height **2) **0.5
# print(f"Right angled triangle is: {R_angle} ")
# -------------------------------------------------------------Que 8 ------------------------------------------------------------------
# 8.Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
# --------->
# n = 25
# total = 0
# c = 0
# for i in range(1,n):
#     total = i * (i+1)
# print(total)
# for i in str(total):
#     if i == "0":
#         c += 1
# print("Number of Zero > ", c )

# -------------------------------------------------------------Que 9 ------------------------------------------------------------------
# 9.Write a Python program to Find the number of divisors of a given integer is even or odd.
# --------->
# d = 0
# n = 12
# for i in range(1,n+1):
#     if n % i == 0:
#         d += 1
# if d % 2 == 0:
#     print("Even Divisors ")
# else:
#     print("Odd Divisors")

# -------------------------------------------------------------Que 10 ------------------------------------------------------------------
# 10. Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure.
# -------->
# user_input = 125
# while str(user_input)!=str(user_input)[::-1]:
#     user_input += sum([int(x) for x in list(str(user_input))])
# else:
#     print('palindrome Number is :',user_input)

# -------------------------------------------------------------Que 11 ------------------------------------------------------------------
# 11.Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No".
# -------->
# side1 = 4
# side2 = 4
# side3 = 4

# if (side1**2 + side2**2 == side3**2) or (side1**2 + side3**2 == side2**2) or (side2**2 + side3**2 == side1**2):
#     print("Yes")
# else:
#     print("No")
# -------------------------------------------------------------Que 12 ------------------------------------------------------------------
# 12. Write a Python program to print the number of prime numbers which are less than or equal to a given integer.
# --------->
# check_prime = lambda n : "PRIME "if  n > 1 and all(n%i != 0 for i in range (2,n)) else "Not prime"
# user_input = int(input("Enter a Number: "))
# for i in range(2, user_input+1):
#     s = check_prime(i)
#     if s == "PRIME ":
#         print(f"{i} is prime")

# -------------------------------------------------------------Que 13 ------------------------------------------------------------------
# 13.Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters.
# Note: A word is a sequence of letters which is separated by the spaces.

# Input:
# A text is given in a line with following condition:
# a. The number of letters in the text is less than or equal to 1000.
# b. The number of letters in a word is less than or equal to 32.
# c. There is only one word which is arise most frequently in given text.
# d. There is only one word which has the maximum number of letters in given text.
# Input text: Thank you for your comment and your participation.
# Output: your participation.
# ------------>
# string = "Have a good day see you soon."
# lista = string.split()
# max=0
# repeatedword = ""
# maxlen = 0
# maxWord = ""
# for i in lista:
#     count = lista.count(i)
#     lenCount = len(i)
#     if count > max:
#         max = count
#         repeatedword = i
#     if lenCount > maxlen:
#         maxlen = lenCount
#         maxWord = i
# print(repeatedword,maxWord)
# -------------------------------------------------------------Que 14 ------------------------------------------------------------------
# 14.Write a Python program to find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668.
# Input:
# Input an integer created by 8 numbers from 0 to 9.:
# 2345
# Difference between the largest and the smallest integer from the given integer:
# 3087
# ------------->
# input_str = "541"
# sorted_num = []
# for i in input_str:
#     sorted_num.append(int(i))
# sorted_num.sort()
# new_str = ""
# for i in sorted_num:
#     new_str += str(i)

# largest = int(new_str[::-1])
# smallest = int(new_str)
# difference = largest - smallest
# print("Difference between the largest and smallest integer from the given integer:", difference)

# -------------------------------------------------------------Que 15 ------------------------------------------------------------------
# 15. Write a Python program to reverse only the vowels of a given string. Go to the editor
# Sample Output:
# w3resuorce
# Python
# Perl
# ASU
# --------->
# input = "w3resource"
# listString = [*input]
# print(listString)
# for i in range(len(listString)):
#     if listString[i] in "aeiou":
#         for j in range(i+1,len(listString)):
#             if listString[j] in "aeiou":
#                 listString[i], listString[j] = listString[j], listString[i]
# print(listString)
# -------------------------------------------------------------Que 16 ------------------------------------------------------------------
# 16.Write a Python program to compute the largest product of three integers from a given list of integers.
# --------->
# ls = [5, 3, -1, 7, -3, 2, 0, 5]
# ls.sort()
# product = ls[-1] * ls[-2] * ls[-3]
# print("product", product)
# -------------------------------------------------------------Que 17 ------------------------------------------------------------------
# 17.Write a Python program that accept a list of numbers and create a list to store the count of negative number in first element and store the sum of positive numbers in second element.
# ---------->
# ls = [5, 3, -1, 7, -3, 2, 0, 5]
# neg_c = 0
# sum = 0
# for num in ls:
#     if num < 0:
#         neg_c += 1
#     else:
#         sum += num

# print([neg_c, sum])
# -------------------------------------------------------------Que 18 ------------------------------------------------------------------
# 18.Write a Python program to count the number of equal numbers from three given integers.
# -------------->
# num1 = 3
# num2 = 6
# num3 = 9

# equal_count = 0
# if num1 == num2:
#     equal_count += 1
# if num1 == num3:
#     equal_count += 1
# if num2 == num3:
#     equal_count += 1

# print("equal count > ", equal_count)

## -------------------------------------------------------------Que 19 ------------------------------------------------------------------
# 19.Write a Python program to find the middle character(s) of a given string. If the length of the string is odd return 
# the middle character and return the middle two characters if the string length is even.
# ------------>
# user_input = input("Enter a string: ")
# print(len(user_input))
# length = len(user_input)
# mid_index = length // 2

# if length % 2 == 1:
#     result = user_input[mid_index]
#     print("Middle character(s):", result)
# else:
#     if length % 2 == 0:
#         result = user_input[mid_index - 1] + user_input[mid_index]
#         print("Middle character(s):", result)

# -------------------------------------------------------------Que 20 ------------------------------------------------------------------
# 20. Write a Python program to check whether a given number is a narcissistic number or not.
# If you are a reader of Greek mythology, then you are probably familiar with Narcissus. He was a hunter of exceptional beauty that he died because he was unable to leave a pool after falling in love with his own reflection. That's why I keep myself away from pools these days (kidding).
# In mathematics, he has kins by the name of narcissistic numbers - numbers that can't get enough of themselves. In particular, they are numbers that are the sum of their digits when raised to the power of the number of digits.
# For example, 371 is a narcissistic number; it has three digits, and if we cube each digits 33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
# 153 = 13 + 53 + 33
# 370 = 33 + 73 + 03
# 407 = 43 + 03 + 73.
# There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
# 1634 = 14+64+34+44
# 8208 = 84+24+04+84
# 9474 = 94+44+74+44
# It has been proven that there are only 88 narcissistic numbers (in the decimal system) and that the largest of which is
# (115,132,219,018,763,992,565,095,597,973,971,522,401)
# has 39 digits.

# Ref.: //https://bit.ly/2qNYxo2
# Sample Output:
# True
# True
# True
# False
# True
# True
# True
# False

# --------->
# ls = [115,153,132,219,18,1634,763,992,565,9474,95,597,973,971,522,401]

# for num in ls:
#     num_str = str(num)
#     num_digits = len(num_str)
#     total = 0
#     for digit in num_str:
#         total += int(digit) ** num_digits

#     if total == num:
#         print(f"{num}    *Narcissistic")
#     else:
#         print(f"{num}    NOT narcissistic")

# -------------------------------------------------------------Que 21 ------------------------------------------------------------------
# 21. Write a Python program to find the name of the oldest student from a given dictionary containing the names and ages of a group of students.
# ------->
# dict1 = { 'Arayn': 21,  "akshad" : 22 , 'Amit': 23, 'Aditya':28, }
# min = 0
# valueString = ""
# for key,value in dict1.items():
#     if value > min:
#         min = value
#         valueString = key
# print("Oldest Student Age > ", min," Of Student", valueString)


# -------------------------------------------------------------Que 22 ------------------------------------------------------------------

# 22.Write a Python program to check whether two given lines are parallel or not. Go to the editor
# Note: Parallel lines are two or more lines that never intersect. Parallel Lines are like railroad tracks that never intersect.
# The General Form of the equation of a straight line is: ax + by = c
# The said straight line is represented in a list as [a, b, c]
# Example of two parallel lines:
# x + 4y = 10 and x + 4y = 14
# Sample Output:
# True
# False
# Example lines

# ------------>
# line1 = [1, 4, 10]  
# line2 = [1, 4, 14] 
# if line1[0] * line2[1] == line1[1] * line2[0]:
#     print("True line Parallel")
# else:
#     print("False, line not parrallel")

# -------------------------------------------------------------Que 23 ------------------------------------------------------------------

# 23.Write a Python program to create a list of the accumulating sum from a given list.
# ----------->
# given_list = [5,10,19,22,33,44,5,12,66]
# sum_list = []
# current_sum = 0
# for num in given_list:
#     current_sum += num
#     sum_list.append(current_sum)
# print("sum list:", sum_list)

# -------------------------------------------------------------Que 24 ------------------------------------------------------------------

# 24.Write a Python program that takes three integers and check whether the last digit of first number * the last digit of second number = the last digit of third number.
# ---------->

# num1 = 15
# num2 = 18
# num3 = 19

# last_digit_num1 = num1 % 10
# last_digit_num2 = num2 % 10
# last_digit_num3 = num3 % 10

# if last_digit_num1 * last_digit_num2 == last_digit_num3:
#     print("the multiplcation is same as third number")
# else:
#     print("Not same")

# -------------------------------------------------------------Que 25 ------------------------------------------------------------------

# 25.Write a Python program to remove two duplicate numbers from a given number of list.
# ------------->
# list1 = [1,2,5,9,4,5,5,6]
# list1.sort()
# set1 = set()
# for i in list1:
#     if list1.count(i) == 1:
#         set1.add(i)
# print(list(set1))


# -------------------------------------------------------------Que 26 ------------------------------------------------------------------
# 26.write a program to print number of time the sub-string is in the give string.eg-string:'abcdcdc ,sub-string: 'cdc'.
# -------------->

# stringg = "cdcdcdccdcd"
# count = 0
# for i in range(len(stringg)-2):
#     if(stringg[i] + stringg[i+1] + stringg[i+2] == "cdc"):
#         count+=1
# print("Substring Count > ",count)
