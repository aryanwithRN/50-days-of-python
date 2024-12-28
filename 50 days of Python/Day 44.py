# 1-  Develop a Python program to check if two given strings are anagrams of each other. An anagram of a string is another string that contains
#  the same characters, only the order of characters can be different. For example, "listen" and "silent" are anagrams.
# first_input = input("Enter a string: ")
# Second_input = input("Enter a string: ")

# if len(first_input) == len(Second_input):
#     for i in first_input :
#         if i in Second_input:
#             continue
#         else:
#             print("Given String is Not anagrams")
#     print("The give inputs are anagram")

# else:
#     print("Given String is Not anagrams")

# 2-Write a Python program to count the frequency of each word in a given string. For example, if the input string is "the quick brown fox jumps 
# over the lazy dog", the output should display the count of each word.
    
# user_input = input("Enter a String: ")

# x = user_input.split(" ")
# print(x)
# for i in x:
#     count = 0
#     for j in x:
#         if i == j:
#             count +=1 
#         print(f"{i} is repetaed {count} times")

# 3-Develop a Python program that takes a string input from the user and reverses it. However, if the length of the string is greater than 10, 
# reverse only the first 10 characters; otherwise, reverse the entire string. Print the reversed string.

# user_input = input("Enter a String: ")
# if len(user_input) > 10:
#     print(user_input[:-11:-1])
# else:
#     print(user_input[::-1])


# 4- Create a Python program that prompts the user to enter a string and checks if it starts with the prefix "Hello". Print "String starts with 
# 'Hello'" if it does, otherwise print "String does not start with 'Hello'" using if-elif-else statements.
# user_input = input("Enter a String: ").lower()
# ls = user_input.split(" ")
# if ls[0] == "hello":
#     print("string start with Hello")

# elif ls[0] != "hello":
#     print("String does not start with 'Hello'")

# else:
#     print("Invalid input")

# or
    
# user_input = input("Enter a String: ").lower()
# s2 = ""
# for i in range(0,len(user_input)):
#     if user_input[i] == " ":
#         s2 = user_input[:i]
#         break
# if s2 == "hello":
#         print("string start with Hello")
    




# 5- Create a Python program to slice a given string into equal parts of a specified length given by the user. If the length of the string 
# is not evenly divisible by the specified length, the last part should contain the remaining characters.

# Input:
# abcde
# 2
# Output:
# ab
# cd
# e

# user_input = input("Enter a String: ")
# length = int(input("Enter length to devide: "))
# for i in range (0, len(user_input), length):
#     print(user_input[i:i+length])

# WAP to take list of lists containing n number of elements find the sublist with second largest sum.(2d array)
# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# d1 = {}
# for i in ls:
#     index_key = ls.index(i)
#     s = sum(i)
#     d1[index_key] = s
# max = 0
# s_max = 0
# for k in d1.keys():
#     if d1[k] > max:
#         s_max = max
#         max = d1[k]

#     elif d1[k] != max and d1[k] > s_max:
#         s_max = d1[k]
# pos = list(d1.values()).index(s_max)
# print(f"sublist having second largest sum is {ls[pos]}, with sum as {s_max}")




