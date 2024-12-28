# 25-jan-23
# OOP
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism


# Self : whenever we call a function through object, the defult parameters self represent the object for which the function is being called.
# Constructor: At the time of object creation the constructor (__init__) is called automatically which assigns the defult values to all the data members for that perticullar object .

# class student: #Class Definition
#     def __init__(self): #Constructor
#         self.name="ABC"
#         self.r_No=1
#         self.std=12
#     def Enter(self):
#         self.name=input("Enter Your Name: ")
#         self.r_No=int(input("Enter Your Roll Name: "))
#         self.std= int(input("Enter Standard: "))
#     def Display(self):
#         print(self.name)
#         print(self.r_No)
#         print(self.std)
# # main
# s1=student()
# s2 = student()
# s1.Enter()
# s1.Display()
# s2.Enter()
# s2.Display()


# ------------------------------------------------------------------------------------QUE-1------------------------------------------------------------------------------------
# Construct a class employe with attributs(Data members) like Name, ID, salary, Dept. , and Role . WAP to enter the data for five employee and display them consicatively.


# class employee:
#     def __init__(self):
#         self.name="Abc"
#         self.ID = 123
#         self.salary = 123454
#         self.Dept = "IT"
#         self.Role = "SDE"
    
#     def Enter(self):
#         self.name=input("Enter Employee Name: ")
#         self.ID=int(input("Enter Employee ID: "))
#         self.salary= int(input("Enter Salary: "))
#         self.Dept= input("Enter Dept: ")
#         self.Role= input("Enter Role: ")
#     def Display(self):
#         print(self.name)
#         print(self.ID)
#         print(self.salary)
#         print(self.Dept)
#         print(self.Role)

# # main
# emp_1 = employee()
# emp_2 = employee()
# emp_3 = employee()
# emp_4 = employee()
# emp_5 = employee()

# emp_1.Enter()
# emp_1.Display()
# emp_2.Enter()
# emp_2.Display()
# emp_3.Enter()
# emp_3.Display()
# emp_4.Enter()
# emp_4.Display()
# emp_5.Enter()
# emp_5.Display()

# Construct a class student with attributes as NAme, roll no , std , marks. WAP to define 3 functions enter, display and a function to calculate percentage for each of 3 students 

class student: #Class Definition
    def __init__(self): #Constructor
        self.name= None
        self.r_No=0
        self.std=0
        self.marks= []
    def Enter(self):
        self.name=input("Enter Your Name: ")
        self.r_No=int(input("Enter Your Roll Name: "))
        self.std= int(input("Enter Standard: "))
        N = 5
        for i in range(0,N):
            x = int(input("Enter your Marks : "))
            self.marks.append(x)
    
    def Cal_percent(self):
        sum = 0
        for j in self.marks:
            sum = sum + j
        s = sum /5 
        print(s, "Your Percentage ")
        
   
    def Display(self):
        print(self.name)
        print(self.r_No)
        print(self.marks)
    


# main
s1=student()
s2 = student()
s3 = student()
s1.Enter()
s1.Display()
s1.Cal_percent()
s2.Enter()
s2.Display()
s2.Cal_percent()
s3.Enter()
s3.Display()
s3.Cal_percent()