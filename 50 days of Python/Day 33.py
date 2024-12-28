# -------------------------------------------------------------------------QUE 1--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Construct a class name employee with attributes EMP_ID, EMP_Name, Dept. ,Salary,Year Of service and Job_Role. create send two fn for entring the details of the emp and displaying 
# them function calc bonus which update the salary of the emp if year of service is grater than 10Y by 8% and print the new salary 
# class employe:
#     def __init__(self): #Constructor
#         self.EMP_name= None
#         self.EMP_ID=0
#         self.Dept=None
#         self.Jrole= None
#         self.salary= 0
#         self.YOS= 0
    
#     def Enter(self):
#          self.EMP_name=input("Enter Employe Name: ")
#          self.EMP_ID=int(input("Enter EMP ID: "))
#          self.Dept= input("Enter Department: ")
#          self.Jrole= input("Enter Job Role: ")
#          self.salary= int(input("Enter Salary: "))
#          self.YOS= int(input("Enter Your Service Year's : "))
    
#     def calc(self):
#         if self.YOS >=10:
#             self.salary = self.salary + self.salary * 0.08
#             return(self.salary)

#     def display(self):
#         print(self.EMP_name)
#         print(self.EMP_ID)
#         print(self.Dept)
#         print(self.Jrole)
#         print(self.YOS)
#         if self.YOS >= 10:
#             print(f"{self.EMP_name}Your Updated Salary{self.salary}")
#         else:
#             print(f"self.salary")
           
# # Main
# emp1 = employe()
# emp1.Enter()
# emp1.calc()
# emp1.display()
# emp2 = employe()
# emp2.Enter()
# emp2.calc()
# emp2.display()
# emp3 = employe()
# emp3.Enter()
# emp3.calc()
# emp3.display()
# emp4 = employe()
# emp4.Enter()
# emp4.calc()
# emp4.display()
# emp5 = employe()
# emp5.Enter()
# emp5.calc()
# emp5.display()

# -------------------------------------------------------------------------QUE 2--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Construct a class Bank with attributes Account Number , name , Balance, and date of Opening of account. create 2 fn enter and display
# the detaials of  a perticullar customer and 3 fn withdraw, dipposite and check balance. 
# class Bank:
#     def __init__(self): #Constructor
#         self.Ac_No= 0
#         self.Ac_Name= None
#         self.Balance= 0
#         self.DOA = 0
#         self.withdraw_ = 0
#         self.dipposite_ = 0

    
#     def Enter(self):
#          self.Ac_N0=int(input("Enter Account number : "))
#          self.DOA= int(input("Enter Your Account Opening Year: "))
#          self.Ac_Name=(input("Enter Account Holder Name: "))
#          self.Balance= int(input("Enter Your Balance: "))
         
    
#     def display(self):
        
#         print("====================================================================== Details ==================================================================================")
#         print(f"Your Account Number - {self.Ac_N0}")
#         print(f"Account Holder Name - {self.Ac_Name}")
#         print(f"Account Balance - {self.Balance}")
    
#     def withdraw(self):
#         self.withdraw_ = int(input("Enter Your Withdraw Amount: "))
#         self.Balance = self.Balance - self.withdraw_
#         print(f"Account balance after withdraw is, {self.Balance}")
    
#     def dipposite(self):
#         self.dipposite_ = int(input("Enter Your Dipposite Amount: "))
#         self.Balance = self.Balance + self.dipposite_
#         print(f"Balance After Dipposited  amount is, {self.Balance}")
    
#     def check_balance(self):
#         print(f"Account Balance is, {self.Balance}")
    
# # main
# print("\n")
# print("=================================================================={ WEll-COME to LAXMI Cheat Funds }===============================================================")
# print("\n")
# user = Bank()
# user.Enter()
# print("\n")
# user.display()
# print("\n")
# print("==============================================================   Withdraw / Dipposite / Check Balance   ===========================================================")
# action = input("To action press key (Withdraw - 1 / Dipposite -2 / check Balance- 3):")
# if action == "1":
#     user.withdraw()
# elif action == "2":
#     user.dipposite()
# elif action == "3":
#     user.check_balance()


# -------------------------------------------------------------------------QUE 3--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, 
#and emp_department and methods like calculate_emp_salary, emp_assign_department,hoursworked, 
#and print_employee_details.
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary': salary and hours_worked, which is the number of hours worked by the employee. 
# If the number of hours worked is more than 50, 
# the method computes overtime and adds it to the salary. 
# Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))

# class employe:
#     def __init__(self): #Constructor
#         self.EMP_name= None
#         self.EMP_ID=0
#         self.Dept=None
#         self.Jrole= None
#         self.salary= 0
#         self.hoursworked=0
#         self.emp_assign_department = None
#         self.YOS= 0
    
#     def Enter(self):
#          self.EMP_name=input("Enter Employe Name: ").upper()
#          self.EMP_ID=int(input("Enter EMP ID: "))
#          self.Dept= input("Enter Department: ").upper()
#          self.Jrole= input("Enter Job Role: ").upper()
#          self.salary= int(input("Enter Salary: "))
#          self.hoursworked = int(input("Enter Work Hour's : "))
        
#     def assign_department (self):
#         self.Dept = input("Enter the Department youu want to assign: ").upper()
    
#     def calc(self):
#         if self.hoursworked > 50:
#             overtime = self.hoursworked - 50
#             s  = (overtime * (self.salary / 50)) 
#             print(f"Employe Over time Money is {s}")
#             self.salary = s + self.salary
#             return(f"Salary after Overtime is, {self.salary}")
#         else: 
#             return(self.salary )
#     def display(self):
#         print("\n")
#         print("====================================================={ Details }======================================= " )
#         print("\n")
#         print(f"Employe Name:- {self.EMP_name}")
#         print(f"Employe ID :- {self.EMP_ID}")
#         print(f"Employe Department:- {self.Dept}")
#         print(f"Empolye Job Role:- {self.Jrole}")
#         print(f"Employe Salary:- {self.salary}")
#         print("\n")
           
# # Main
# emp1 = employe()
# emp1.Enter()
# emp1.calc()
# user =  input("Want to change Employe Department(y/n): ").lower()
# if user == "y":
#     emp1.assign_department()
# elif user == "n":
#     pass
# emp1.display()
