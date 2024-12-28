# Que (1)
# WAP Take a dictionary representing a bookstore inventory with book titles as keys and the corresponding 
# quantities as values as user input. Write a program to find the book with the maximum quantity.

# d1= {}
# user_input = int(input("Enter Number of BOOk: "))
# for i in range ( 0 , user_input):
#     keys = input("Enter Book Name: ")
#     values = int(input ("Enter Number of Books: "))
#     d1[keys]=values

# max = 0
# for i in d1.keys():
#     if max < d1[i]:
#         max = d1[i]
# print("Total Numbers of Book is", max, "and Book Name is ", i) 

# Que (2)
# Write a program that takes a string as input and returns a dictionary with the frequency of each word.
# d1 = {}
# user_input = input("Enter a String: ")

# for i in user_input:
#     count = 0
#     for j in user_input:
#         if i == j:
#             count = count + 1
#     d1[i]= count        
    
# print(d1)

# Que (3)
# You have a dictionary containing details of employees, including names and salaries. 
# Write a program to update the salary of a specific employee.

# d1= {}
# user_input = int(input("Enter Number of Employee: "))
# for i in range ( 0 , user_input):
#     keys = input("Enter Employee Name: ")
#     values = int(input ("Enter your Salarie: "))
#     d1[keys]=values
# print(d1)
# name_of_Employe = input("Enter a Employee Name to update: ")
# new_Salarie = int(input("Enter Updated Salarie: "))
# if name_of_Employe in d1.keys():
#     d1[name_of_Employe]=new_Salarie
# print("Updated salaries of ",name_of_Employe,"is",d1[name_of_Employe])
# print(d1)



# Que (4)
# Create a dictionary to store weather forecasts for different cities. Each city has a list of forecasted 
# temperatures for the upcoming week. Write a program to find the city with the most consistent temperatures.

# d1= {}
# ls = []
# user_input = int(input("Enter Number of Citys:  "))
# for i in range ( 0 , user_input):
#     keys = input("Enter a city Name: ")
#     Monday = int(input ("Enter temperature of Monday: "))
#     Tuesday = int(input ("Enter temperature of Tuesday: "))
#     Wednesday = int(input ("Enter temperature of Wednesday: "))
#     Thrusday = int(input ("Enter temperature of Thrusday: "))
#     Friday = int(input ("Enter temperature of Friday: "))
#     Saturday = int(input ("Enter temperature of Saturday: "))
#     Sunday = int(input ("Enter temperature of Sunday: "))
#     values = Monday, Tuesday, Wednesday, Thrusday, Friday ,Saturday, Sunday
#     ls.append(values)
#     d1[keys]= ls
   
#     # const_list=[]
#     max  = 0 
#     for i in ls:
#         count=ls.count(i)
#         if count >= max:
#             max = count
#     ls.append(max)

#     d1[keys] = ls
# # print(d1)

# cityname=""
# max = 0 ():
#     if value [-1]> max:
# for key, value in d1.items
#         max=value[-1]
#         cityname = key

# print(cityname, "consistant with ", max ,"Days")


# Design a nested dictionary representing a database of employees in a company with employee name as the key and 
# value will be another dictionary containing specific details of the employee(emp_ID , age, salary, dept, role). 
# Write a program to search for an employee based on their department and role.
# d1={}
# d2={}
# user_input = int(input('Enter Number Of Employe: '))
# for i in range (0 ,user_input):
#     keys = input("Enter Empolye Name: ")
#     emp_ID = input("Enter Employe ID: ") 
#     Age = input("Enter Employe Age: ")
#     Salary = input("Enter Employe Salary: ")
#     dept = input("Enter Employe Department(IT/HardWare): ")
#     role = input("Enter Employe Role: ")
#     values = {emp_ID, Age, Salary,dept, role }
#     d1[keys]= values
# print(d1)

# Empolye_Dept = input("Enter Empolye Department: ")
# Empolye_Role = input ("Enter Empolye Role: ")

# if Empolye_Dept in d1.keys():
#     d1[Empolye_Dept]=dept
#     if Empolye_Role in d1.keys():
#         d1[Empolye_Role]=role
# print(d1[keys])
    