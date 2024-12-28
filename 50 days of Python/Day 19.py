# # t1 = (80,90,85,35,80)
# # t1[0]= 100
# # print(t1)
# # print(t1[2])
# # t2= (10)
# # t1 = t1 + t2
# # print(t1)

# #.append
# print("append")
# l1=[70,90,34,23,78]
# l1.append(78)
# print(l1)

# #.copy
# print("copy")
# l1=[70,90,34,23,78]
# l1.append(78)
# l2=l1.copy()
# print(l2)
# #.count
# print("count")
# l1=[70,90,34,23,78,78]
# l1.append(78)
# print(l2.count(78))
# #.extend
# print("Extend")
# l1=[70,90,34,23,78]
# l2=[20,30,40,50]
# l1.extend(l2)
# print(l1)
# #.index
# print("index")
# l1=[70,90,34,23,78,78]
# print(l1.index(78))
# #.pop
# print("Pop")
# l1=[70,90,34,23,78,78]
# print(l1.index(78))
# print(l1.pop(4))
# #.remove
# print("Remove")
# l1=[70,90,34,23,78,78]
# print(l1.index(78))
# print(l1.pop(4))
# l1.remove(78)
# print(l1)
# #.reverse
# print("Reverse")
# l1=[70,90,34,23,78,78]
# print(l1.index(78))
# print(l1.pop(4))
# l1.remove(78)
# print(l1)
# l1.reverse
# print(l1)
# #.sort
# print("Sort")
# l1=[70,90,34,23,78,78]
# print(l1.index(78))
# print(l1.pop(4))
# l1.remove(78)
# print(l1)
# l1.reverse
# print(l1)
# l1.sort()
# print(l1)
# #.clear
# print("Clear")
# l1.clear()
# print(l1)


# Dictionaries:

# d1= {"A":80,"B":90,"C":47,"D":52,"E":39}
# print(d1["C"])
# d1["F"]= 90
# print(d1)
# d1.popitem()
# print(d1)
# print(d1.keys())
# print(d1.items())
# print(d1.values())


# Write a function that takes a tuple as input and returns a new tuple with the first and last elements swapped.
# l1 = []
# user_input = int(input("Enter numbers Tupel: "))
# for i in range (0, user_input) :
#     x = input("Enter  a Value: ")
#     l1.append(x)
# # print (l1)
# l1[0],l1[-1]=l1[-1],l1[0]

# t1 = tuple(l1)
# print(t1)



# WAP to take list of student scores as input, calculate the average and assign grades (A, B, C, D) based on predefined ranges.
# A: 90 - 100
# B: 80 - 89
# C: 70 - 79
# D: Below 70

# l1 = []
# user_input = int(input("Enter numbers List: "))
# for i in range (0, user_input) :
#     x = int(input("Enter  a Marks: "))
#     l1.append(x)

# for j in range(0 , x) :
    
#         if x <= 100 and x>=90:
#          print ("A")
#         elif x >= 80 and x <= 89:
#             print("B")
#         elif x >= 70 and x <= 79:
#             print("C")
#         else:
#             print("D")
# print (l1)


# WAP to program to take a dictionary where keys are the salary components of an employee and print the total salary of the employee.
# basic, ta, da, hra, bonus, pf

# user_input = int(input("Enter Number Employes: "))
# d1 ={}
# for i in range (0,user_input):
#     key = input("Enter Employe Name: ")
#     value1 = int(input("Enter a Basic: "))
#     value2 = int (input("Enter a ta: "))
#     value3 = int(input("Enter a da: "))
#     value4 = int(input("Enter a hra: "))
#     value5 = int(input("Enter a bonus: "))
#     value6 = int(input("Enter a pf: "))
#     d1 [key]= value1,value2,value3, value4, value5, value6
# # print(d1)
# for j in d1.values():
#     s =  sum(j)
#     print("salary of", d1[key] , "is", s)