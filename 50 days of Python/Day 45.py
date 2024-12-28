# write  a program to find the sum of all the left digonal elements.

# ls = [[1,2,3],[4,5,6],[7,8,9]]
# d1 = {}
# ls1 = []
# for i in ls:
#     index_key = ls.index(i)
#     d1[index_key] = i
# print(d1)
# for k,v in d1.items():
#     if d1[k] == v[k]:
#         ls1.append(v[k])
# print(ls1)

# sum = 0
# for i in range(0, len(ls)):
#     for j in range(0, len(ls)):
#         if i + j == (len(ls)-1):
#             sum += ls[i][j]
# print(f"the sum of digonal list is ,{sum}")

# Write a Python program to find all pairs of elements in a lists that sum up to a given value
# ls = [1,2,3,4,5,6,7,8,9,10]
# new_ls = []
# given_value = int(input("ENter a Number: "))
# for i in range(len(ls)):
#     for j in range(i+1, len(ls)):
#         s = ls[i] + ls[j]         
#         if s == given_value: 
#             new_ls.append((ls[i] , ls[j]))
# print(new_ls)

# Write a program that takes a list of integers and rearranges it so that all even numbers appear before all odd numbers.
# ls = [1,2,3,4,5,6,7,8,9,10,11]
# even = []
# odd = []
# new_ls = []
# for i in ls:
#     if i % 2 == 0:
#         even.append(i)
#     elif i % 2 != 0:
#         odd.append(i)
# new_ls = even + odd
# print(new_ls)


# Write a program that takes a dictionary and returns the key or keys corresponding to the maximum value.
# d1 = {
#     1:10,
#     2:20,
#     3:30,
#     4:40
# }
# for k in d1.keys():
#     s = max(d1)
# print(f"the max value in dictionary is {d1[s]} of {k}")
