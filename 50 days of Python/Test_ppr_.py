# 1-
#  Take a list of words as input from the user and then check which of the list elements is/are palindrome
# and then print those elements using lambda.
# Sample Input:
# [“ababa”, “ccdc”, “ana”, “old”]
# Sample Output:
# ababa is palindrome
# ana is palindrome
# check_palindrome = lambda i: "palindrome" if i.lower() == i[::-1] else "Not palendrome"

# ls = ["ababa", "ccdc", "ana", "old"]
# res =[check_palindrome(i.lower() )for i in ls]
# print(res)

# 2- 
# 2- Create a function that merges two dictionaries, but if a key exists in both dictionaries,the values 
# should be combined into a list.
# Sample Input1:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'd': 5}

# Sample Output 1:
# {'a': 1, 'b': [2, 4], 'c': 3, 'd': 5}

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 4, 'd': 5}
# ls = []
# new_dict = {}
# new_dict = d1.copy()
# for key2, value2 in d2.items(): 
#     if key2 in new_dict: 
#         new_dict[key2] = [new_dict[key2],value2] 
#     else:
#         new_dict[key2]=value2
# print(new_dict)


# 3- Write a function fibseq(n) which will create a dictionary of all the fibonacci terms with
# key as their position in the series and value as the term itself up to the specified
# threshold number of terms given by the user.
# Fn-
# def fibseq(n):
#     t1 = 0 
#     t2 = 1
#     position=1
#     for i in range (0, n):
#         d1[position]=(t1)
#         t3 = t1 + t2
#         t1 = t2
#         t2 = t3
#         position += 1
#     return(d1)    
# # Main
# user = 5
# d1 = {}
# print(fibseq(user))
