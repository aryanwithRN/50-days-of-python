
#----------------------------------------------------- Que - 1 -------------------------------------------------------------------------------------------

# 1.Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# ------>
# user_input = str(input("Enter File Name: ")).split(".") 
# print(user_input[1])

#----------------------------------------------------- Que - 2 -----------------------------------------------------------------------------------------
# 2.Write a Python program which accepts the radius of a circle from the user and compute the area
# ------->
# user_input = int(input("Enter Radius of circle: "))*3.14 ** 2
# print("Area Of circle: ", user_input)

# ----------------------------------------------------- Que - 3 ------------------------------------------------------------------------------------------
# 3.write python program to display unique no from the the comma-separated numbers given by user
# -------->
# user_input = input("Enter Numbers: ").split(",")
# for i in user_input:
#     print(i, end="")

# ----------------------------------------------------- Que - 4 -------------------------------------------------------------------------------------------
# 4.Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
# input=1,2,3,4,5,6...
# output=[1,2,3,4,5,6]
# --------->
# ls = []
# for i in range (6):
#     user_input = int(input("Enter Number:"))
#     ls.append(user_input)
# print("Tuple : ",tuple(ls))
# print("List : ", ls)


# ----------------------------------------------------- Que - 5 -------------------------------------------------------------------------------------------
# 5.Write a Python program to count the frequency of words in a list.
# -------->
# ls = ["aryan" , "amit", "aditya", "akshad", "aryan"]
# s = set(ls)
# for j in s:
#        count = ls.count(j)
#        print(f"{j} is repeted {count} times")

# ----------------------------------------------------- Que - 6 -------------------------------------------------------------------------------------------
# 6. Write a python program to find the longest word IN list.
# ------>
# ls = []
# for i in range(3):
#     user_input = input("Enter Names: ")
#     ls.append(user_input)
# print(ls)
# max=0
# for j in ls:
#     x = len(j)
#     if x > max:
#         max = x
# print(f"longest word in list is: {j}")


# ----------------------------------------------------- Que - 7 -------------------------------------------------------------------------------------------
# 7. Write a Python program to read last n lines of a list.
# ------->
# ls = [1,2,3,4,5,6,7,8]
# print(ls[-1])

# ----------------------------------------------------- Que - 8 -------------------------------------------------------------------------------------------
# 8. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
# ------>
# ls=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# max = 0
# for i in ls:
#     s = sum(i)
#     if s > max:
#         max = s
#         j = i
# print(j)

# ----------------------------------------------------- Que - 9 -------------------------------------------------------------------------------------------
# 9. Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
# ------->
# ls = [1,2,3,4]
# new_ls = []
# for i in ls:
#      s=(f"emp{i}")
#      new_ls.append(s)
# print(new_ls)

# ----------------------------------------------------- Que - 10 -------------------------------------------------------------------------------------------

# 10. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
# -------->
# x = {
#     'key1': 1, 
#     'key2': 3, 
#     'key3': 2}
# y = {
#     'key1': 1, 
#     'key2': 2} 

# for i,j in x.items():
#     for k,v in y.items():
#         if k == i and v == j:
#             print(f"{i} is present in both dict X and Y" )

# ----------------------------------------------------- Que - 11 -------------------------------------------------------------------------------------------

# 11-Write a function to take a list as an input (Containing mix of strings plus numbers) and return 2
# values 
# i. Appended String 
# ii.Sum of numbers
# input=[1,2,'AB',6,'7','N']
# Output=(9,'AB7N')
# ------>
# input=[1,2,'AB',6,'7','N']
# s = 0
# a =""
# for i in input:
#     t = (type(i))
#     if t == int:
#         s += i
#     elif t == str:
#         a += i
# x =(s,a)
# print(x)

# ----------------------------------------------------- Que - 13 -------------------------------------------------------------------------------------------

# 13. Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
# Input : 48
# Output : 3
# For example given number is 59, the result will be 5.
# Step 1: 5 + 9 = 14
# Step 1: 1 + 4 = 5
# ----------->
# user_number = int(input("Enter a Number: "))
# while user_number >= 9:
#     s = 0
#     for i in str(user_number):
#         s += int(i)
#     user_number = s
# print(f"Output: {user_number}")


# ----------------------------------------------------- Que - 14 -------------------------------------------------------------------------------------------
# 14. Write a Python program to print all unique values in a dictionary
# -------->
# d1 =    {
#         "aryan": 21,
#         "amit": 23,
#         "akshad":22,
#         "aditya": 22,
#         }
# s = set()
# for v in d1.values():
#     s.add(v)
# print(f"{s} this are unique values in dictionary ")

# ----------------------------------------------------- Que - 15 -------------------------------------------------------------------------------------------
# 15.Write a Python script to concatenate following dictionaries to create a new one
# dic1={'a':101, 'b':201}
# dic2={'c':301, 'd':401}
# dic3={'e':501,'f':601}

# --------->
# dic1={'a':101, 'b':201}
# dic2={'c':301, 'd':401}
# dic3={'e':501,'f':601}
# d1 = {}
# d1.update(dic1)
# d1.update(dic2)
# d1.update(dic3)
# print(f"{d1} is concatenated Dictionaries")



# ----------------------------------------------------- Que - 16 -------------------------------------------------------------------------------------------
# 16. Write a Python script to check if a given key already exists in a dictionary.
# ------>
# d1 =    {
#         "aryan": 21,
#         "amit": 23,
#         "akshad":22,
#         "aditya": 22,
#         }
# check_key = input("Enter Name To check is in Dict or not:  ").lower()
# for key in d1.keys():
#     if check_key == key:
#         print("Yes It is in Dictionary on key", check_key)

# ----------------------------------------------------- Que - 17 -------------------------------------------------------------------------------------------
# 17.WAP to print all the keys of dict.
# ------>
# d1 =    {
#         "aryan": 21,
#         "amit": 23,
#         "akshad":22,
#         "aditya": 22,
#         } 
# for key in d1.keys():
#     print(f"This are the keys of dictionary:- {key}")

# ----------------------------------------------------- Que - 18 -------------------------------------------------------------------------------------------
# 18.WAP to print TRUE or FALSE based on if key given by user exists in precreated dict
# --------->
# d1 =    {
#         "aryan": 21,
#         "amit": 23,
#         "akshad":22,
#         "aditya": 22,
#         } 
# user_input = input("Enter key in dictionary: ").lower()
# for i in d1.keys():
#     if i == user_input:
#       k = True   
#       break  
#     else:
#      k = False
# print(k)

# ----------------------------------------------------- Que - 19 -------------------------------------------------------------------------------------------
          
# 19.Write a Python program to sum all the values in a dictionary
# -------->
# d1 =    {
#         "aryan": 21,
#         "amit": 23,
#         "akshad":22,
#         "aditya": 22,
#         }
    
# s = sum(d1.values())
# print(s)

# ----------------------------------------------------- Que - 20 -------------------------------------------------------------------------------------------

# 20. One liner : Take a sentence from user and print it removing vowels from it
# ------>
# print("".join(i for i in input("Enter a sentence: ").lower() if i not in 'aeiou'))

# ----------------------------------------------------- Que - 21 -------------------------------------------------------------------------------------------

# 21. One liner : Prapre a list contains multiplication of all combinations
# L1=[1, 2, 3, 4, 5] Output =[1, 2, 3, 4, 5,2,4,6,8,10,3,6,9.....]
# --------->
# print([i * j for i in [1, 2, 3, 4, 5] for j in [1, 2, 3, 4, 5]])

# ----------------------------------------------------- Que - 22 -------------------------------------------------------------------------------------------

# 22. One liner : Take n from user and Print Table of 1 to n numbers
# Output : [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3.....30]]
# print([[i * j for j in range(1, 11)] for i in range(1, int(input("Enter a number (n): ")) + 1)])
# --------->
# print([[j * i  for i in range (1, 11)]for j in range (1, int(input("Enter a Number: ")) + 1)])


# -------------------------------------------------- Que-23 ---------------------------------------------------------------------
# 23. Take input as a list and return dictionary with keys as 0,1,2.....
# input =['A','B','C'] Output={1:'a',2:'b',3:'b'}
# ---------->
# ls =['A','B','C']
# d1 = {}
# for i in range(len(ls)):
#         d1[i+1]= ls[i]
# print(d1)

# ----------------------------------------------------------------------------------------------------------------------------------------
