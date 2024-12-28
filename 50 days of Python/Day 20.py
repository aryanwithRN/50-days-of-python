# Que ( 1 )
# Write a Python function that takes a dictionary and returns a new dictionary with the keys and values swapped.
# Input 1:
# {'a': 1, 'b': 2, 'c': 3}
# Output 1:
# {1: 'a', 2: 'b', 3: 'c'}
# -->

# d1 = {}
# d2 = {}
# user_input = int(input("Enter the Length: "))
# for i in range (0, user_input):
#     keys = input("Input: ")
#     value = input("Input Values: ")
#     d1[keys] = value
#     d2 [ value]= keys
# print (d1)
# print (d2)

# Que ( 2 )
# Write a function that takes a list of tuples, where each tuple contains a name and a score, and returns two lists:
# one containing the names and another containing the scores.
# Input:
# scores = [("Alice", 95), ("Bob", 88), ("Carol", 92)]
# Output:
# names = ["Alice", "Bob", "Carol"]
# scores = [95, 88, 92]

# l1 = []
# l2 = []
# t1 = ()
# user_input = int(input("Enter Length: "))
# for i in range (0, user_input) :
#     x = input("Enter  a Name: ")
#     y = input("Enter  a Score: ")
#     t1 = t1 + (x, y)
#     l1.append(x)
#     l2.append(y)
    
# print(t1)
# print(l1)
# print(l2)


# WAP to create a dictionary using user input which has fruit name and the cost, then take a threshold cost as 
# input from the user print all the fruits which have cost is greater then threshold cost.
# 
# d1 = {}
# user_input = int(input("Enter Length: "))
# for i in range (0, user_input):
#     keys = input("Enter Fruits Name: ")
#     values = int(input("Enter Fruits Price: "))
#     d1[keys] = values
# threshold_cost = int(input("Enter a Threshold Cost: "))
# print(d1)

# for i in d1.keys():
#     if d1[i] > threshold_cost:
#         print(i,d1[i])

# WAP to take a dictionary as a user input consisting of students name as keys and list of subject marks as values calculate 
# and print percentage obtain by each student and also print the hightest scorer among them>
# ---->

# d1 = {}
# user_input = int (input("Enter Number of Students: "))
# for i in range (0, user_input):
#     keys = input("Enter Student Name: ")
#     value1 = int(input("Enter Engilsh Marks:"))
#     value2 = int(input("Enter Hindi Marks:"))
#     value3 = int(input("Enter Maths Marks:"))
#     value4 = int(input("Enter Histroy Marks:"))
#     value5 = int(input("Enter Geography Marks:"))
#     d1[keys]= value1, value2, value3, value4, value5

# mark_list=[]
# for i in d1.keys():
#     sum = 0 
#     for j in d1[i]:
#         sum = sum + j
#     mark_list.append(sum/5)
    
#     # s1 = s = sum(d1[i]) / 5
# print("percentage of", i ,"is", sum)
# max = 0
# for i in range(user_input):
#     if max < mark_list[i]:
#         max = mark_list[i]
# print("The hightest Scorer is",i,"with", max, "%")


# WAP to take a dictinary from the user contaning product name as keys and a tupel containing cost price and selling price of that 
# perticular product calculate and print all the products which have a profit margin.
        
# d1 = {}
# t1 = ()
# user_input = int(input("Enter Length: "))
# for i in range  ( 0, user_input):
#     keys = input("Enter Product Name: ")
#     cost_price = int(input("Enter Cost Price "))
#     selling_price = int(input("Enter Selling Price: "))
#     t1= t1 + (cost_price, selling_price)
#     d1[keys]= t1
    
# # print(t1)
# for i in d1.keys():
#     if d1[i][1] > d1[i][0]:
#         print(i , " is profitable")
        
# WAP to take a dictionary of students and their scores as user input and filter out students who scored less than a certain threshold.
        
d1= {}
user_input = int(input("Enter Number OF students: "))
for i in range ( 0 , user_input):
    keys = input("Enter Name Of Students: ")
    values = int(input ("Enter Your Scores:  "))
    d1[keys]=values
thrushold_value = (75)

for i in d1.keys():
    if d1[i] < thrushold_value:
        print(i, "You have less score")