
# -------------------------------------------------------------------- QUE 1 -------------------------------------------------------------------------------------------------------
# 1- Write a program that takes a string as input and returns the reverse of that string.
# -->
# user_input = str(input("Enter a string: "))
# print(user_input[::-1])
# # (or)
# print(str(input("Enter a Str: ")[::-1]))

# -------------------------------------------------------------------- QUE 2 -------------------------------------------------------------------------------------------------------
# 2- Write a program that takes a string as input and capitalizes the first letter of each word and prints the new string.
# -->
# user_input = str(input("Enter a string: ")).title()
# print(user_input)
# (or)
# print(str(input("Enter a Str: ").title()))

# -------------------------------------------------------------------- QUE 3 -------------------------------------------------------------------------------------------------------
# 3- Write a program that takes a string as input and compresses it by replacing repeated characters with a number indicating the count (e.g., 'aaabbbccc' becomes 'a3b3c3').
# -->s
# user_input = input("Enter a string : ")

# str_ = ""
# count = 1
# for i in range(1, len(user_input)):
#     if user_input[i] == user_input[i - 1]:
#         count += 1
#     else:
#         str_ += user_input[i - 1] + str(count)
#         count = 1
   
# str_ += user_input[-1] + str(count)   
# print("Output string :", str_)

# -------------------------------------------------------------------- QUE 4 -------------------------------------------------------------------------------------------------------
# 4- Write a Python program that takes a string as input and counts the number of consonants (non-vowel characters) in the string.
# user_input = input("Enter a string: ").lower()
# count = 0
# vowels = 'aeiou'

# for i in user_input:
#     if i not in vowels:
#         count += 1
# print("Number of consonants in the string:", count)


# -------------------------------------------------------------------- QUE 5 -------------------------------------------------------------------------------------------------------
# 5- Write a Python program that takes a string as input and removes duplicate characters, keeping only the first occurrence of each character.
# user_input = input("Enter a string: ")
# result = ""
# rev_char = set()

# for i in user_input:
#     if i not in rev_char:
#         result += i
#         rev_char.add(i)

# print("String after removing duplicates:", result)


# -------------------------------------------------------------------- QUE 6 -------------------------------------------------------------------------------------------------------
# 6- Write a Python program that takes a string as input and finds the longest repeated substring within it.

# user_input = input("Enter a string: ")

# longest_substring = ""
# for i in range(1, len(user_input)):
#     for j in range(len(user_input) - i):
#         substring = user_input[j:j + i]
#         if substring in user_input[j + 1:]:
#             if len(substring) > len(longest_substring):
#                 longest_substring = substring

# if longest_substring:
#     print("Longest repeated substring:", longest_substring)
# else:
#     print("Not found repeated substring .")
