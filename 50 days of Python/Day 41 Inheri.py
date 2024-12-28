# -------------------------------------------------------------------------------------- Que 1 -----------------------------------------------------------------------------------------------------

# Create a base class Employee with attributes like name, employee ID, and salary.
# Derive classes Manager and Developer from it.
# Add specific attributes like bonus for managers and programming language for developers.
# Add a method in the Employee class to calculate the annual salary, including any bonuses or specific attributes for each derived class.

# class Employee:
#     def __init__(self):
#         self.Emp_name = ""
#         self.Emp_ID = 0
#         self.Emp_Salary = 0

#     def emp_enter(self):
#         self.Emp_name = input("Enter Employe Name: ")
#         self.Emp_ID = int(input("Enter Employe ID: "))
#         self.Emp_Salary = int(input("Enter Employe Salary: "))
    
    

#     def emp_display(self): 
#         print("Employe Name: ", self.Emp_name)
#         print("Employe ID: ", self.Emp_ID)
#         print("Employe Salary: ", self.Emp_Salary)

#     def calc_annual(self):
#         s = self.Emp_Salary * 12
#         print("Annual salary: ", s )  

   

# class Manager(Employee):
    
#     def __init__ (self):
#         self.bonus = 0
#     def bonus_ (self):
#         self.bonus = int(input("Enter Bonus Amount: "))
#         self.Emp_Salary = self.Emp_Salary + self.bonus
#     def display_bonus(self):
#         print("Salary With Bonus: ", self.Emp_Salary)


# class Developer(Employee):
#     def __init__(self):
#         self.pro_lang = ""

#     def enter_dev(self):
#         self.pro_lang = input("Enter Developer Programming Language: ")

#     def display_dev(self):
#         print("Programming Language: ", self.pro_lang)


# # main
# user = Manager()
# print("=" * 30)
# user.emp_enter()
# user.calc_annual()
# user.bonus_()

# print("=" * 30)
# user.emp_display()
# user.display_bonus()
# print("=" * 30)

# user= Developer()
# user.emp_enter()
# user.enter_dev()

# print("=" * 30)
# user.emp_display()
# user.display_dev()


# -------------------------------------------------------------------------------------- Que 2 -----------------------------------------------------------------------------------------------------
#Shapes- Base class   dim=[]     enter_dim(n)
#Circle- Inherits Shapes c_area() c_peri()
#Square- "
#Rectangle-"



class Shapes:
    def __init__(self):
        self.ls = []

class Circle(Shapes):
   
    def c_area(self):
        self.ls.append(int(input("Enter Radius > ")))
        print("Area Of Circle >",3.14 * self.ls[0] ** 2,"\n")
   
   
    def c_perimeter(self):
        self.ls.append(int(input("Enter Radius > ")))
        perimeter = 2 * 3.14 * self.ls[0]  
        print("Perimeter of the circle is=",perimeter)

class Square(Shapes):  
    
    
    def Sarea(self):
        self.ls.append(int(input("Enter Dimension For Square : ")))
        print("Area Of Square >",self.ls[0] ** 2,"\n")

    def spare(self):
        self.ls.append(int(input("Enter Dimension For Square : ")))
        print("Paremeter Of Square ", self.ls[0] * 4, "\n")

class Rectangle(Shapes):
    
    
    def Rarea(self):
        user = int(input("Enter Length: "))
        user_ = int(input("Enter Width: "))
        s = user * user_
        print("Area OF Rectangle is" , s)

    def Rpare(self):
        user = int(input("Enter Length:"))
        user_ = int(input("Enter Width:"))
        s = 2 * (user + user_)
        print("Paremeter of Rectangle is ", s)

#main
while True:
    print("======================= Shape Menu ===========================")
    print("     1 For Circle")
    print("     2 For Square")
    print("     3 For Rectangle")
    print("     4 For Exit")
    choice = int(input("Enter Choice 1/ 2 / 3 / 4 :"))
    print("=" * 60)
    if choice == 1:
        while True:
            print("========================== Circle Menu ======================= ")
            # nod=int(input("Enter number of dimensions For Circle :  "))
            
            C1=Circle()
            
            print("what do you want to calculate,")
            print("     1 For Area")
            print("     2 For Paremeter")
            print("     3 For Exit")
            
            ch1=int(input("Enter 1 / 2 / 3 : "))
            if ch1==1:
                C1.c_area()
            elif ch1 == 2:
                C1.c_perimeter()

            elif ch1 == 3:
                break

            # else:
            #     print("Entered dimensions Should be 1 For Circle!")


    elif choice == 2:
        while True:
            print("========================== Square Menu ======================= ")
            C1=Square()
            print("what do you want to calculate,")
            print("     1 For Area")
            print("     2 For Paremeter")
            print("     3 For Exit")
            ch1=int(input("Enter 1 / 2 / 3: "))
            if ch1==1:
                C1.Sarea()
            elif ch1 == 2:
                C1.spare()
            elif ch1 == 3:
                break
       
        
    elif choice == 3:
        while True:
            print("========================== Rectangle Menu ======================= ")
            C1=Rectangle()
            print("what do you want to calculate,")
            print("     1 For Area")
            print("     2 For Paremeter")
            print("     3 For Exit")
            ch1=int(input("Enter 1 / 2 / 3: "))
            if ch1==1:
                C1.Rarea()
            elif ch1 == 2:
                C1.Rpare()
            elif ch1 == 3:
                break

    elif choice == 4:
                break
    


# -------------------------------------------------------------------------------------- Que 3 -----------------------------------------------------------------------------------------------------

# # Create a base class Account with attributes like account number and balance. 
# Derive classes SavingsAccount and CurrentAccount from it. 
# Include specific attributes like interest 
# rate for savings accounts and overdraft limit for current accounts.
 
#Include methods in each account class to perform transactions, such as deposit() and withdraw().

class Account():
    def __init__(self):
        self.account_name = ""
        self.account_number = 0
        self.account_balance = 0 

    def enter_details(self):
        self.account_name = input("Enter Account Name: ")
        self.account_number = int(input("Enter Account Number: "))
        self.account_balance = int(input("Enter Account Balance: "))

    def display_details(self):
        print("Account Name: ", self.account_name)
        print("Account Number: ", self.account_number)
        print("Account Balance: ", self.account_balance)

    def withdraw(self):
        withdraw_ammount = int(input("Enter Withdraw Ammount: "))
        withdraw_ammount = withdraw_ammount  - self.account_balance 
        print("Total Balance after Withdraw is ", withdraw_ammount)
    
    def deposite(self):
        deposite_amount = int(input("Enter Deposite Ammount: "))
        deposite_amount = deposite_amount + self.account_balance
        print("Total Balance is", deposite_amount) 

    

class SavingAccount(Account):
    def __init__(self):
        self.intrest_rate = 0

    def enter_intrest(self):
        self.intrest_rate = int(input ("Enter Intrest Rate: "))
        s = self.intrest_rate / 100
        self.account_balance +=  self.account_balance * s

    def display_intrest(self):
        print("Intrest Rate: ", self.intrest_rate)
        print(f"Total Balance with {self.account_balance} with {self.intrest_rate}% intrest Rate")


class CurrentAccount(Account):
        def __init__(self):
            self.intrest_rate = 0

        def enter_draft(self):
            self.enter_draft_ = int(input("Enter OverDraft Limit: "))
        def display_draft(self):
            print("Over Draft Limit: ", self.enter_draft_)



# main
            
print("=" * 40, " Bank of Baner ", "=" * 40)
while True: 
    print(" Menu")
    print("        1 For Saving Account")
    print("        2 For Current Account")
    print("        3 For Exit")
    choice = int(input("Enter 1 / 2 / 3: "))

    print("=" * 80)

    if choice == 1:
        print("========== Saving Account ==========")
        user = SavingAccount()
        user.enter_details()
        user.enter_intrest()
        print('= ' * 80)
        user.display_details()
        user.display_intrest()
        print(" = " * 50 )
        while True:
            print("Saving Account Menu")
            print("       1 For Deposite")
            print("       2 For WithDraw")
            print("       3 For Exit")
            ch1 = int(input("Enter 1 / 2 / 3 :"))
            if ch1 == 1:
                user.deposite()
            elif ch1 == 2:
                user.withdraw()

            elif ch1 == 3:
                break
    elif choice == 2:
        print("======== Current Account ===========")
        user = CurrentAccount()
        user.enter_details()
        user.enter_draft()
        print('= ' * 80)
        user.display_details()
        user.display_draft()
        print('= ' * 80)
        while True:
            print("Current Account Menu")
            print("       1 For Deposite")
            print("       2 For WithDraw")
            print("       3 For Exit")
            ch2 = int(input("Enter 1 / 2 / 3 :"))
            if ch2 == 1:
                user.deposite()
            elif ch2 == 2:
                user.withdraw()
            elif ch2 == 3:
                break

    elif choice  == 3:
        break


