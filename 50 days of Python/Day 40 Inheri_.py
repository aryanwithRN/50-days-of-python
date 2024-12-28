# Inheritance:
# It is reusable in multiple class

# Types of Inheritance:
# Single
# Multiple
# Multi-Level

# Access Modifire: 
# public :- Accessible in Own class , can be accessed in inherited aslo
# private :- Can't be accessed Directly by it's own objects, can only be access in the class  definations(i.e by member function of that class only)
# class A :
#     def __init__(self):
        
#         self.__x=10
#         self.y = 20


#     def display (self):
#          print(self.__x)
#          print(self.y)


#     def calc(self):

#         print(self.__x + self.y)

# class B (A):

#     def __init__(self):
#         self.__a=20
#         self.b= 50
#     def display_B(self):
#         print (self.__a)
#         print(self.b)

#     def calc_B(self):
#         print(self-self.__a)

# protected :- 

# ------------------------------------------


# class person:
#     def __init__(self):
#         self.person_name = ""
#         self.person_Age = 0
#         self.person_gender = ""
#         self.adhar_id = 0
    
#     def enter_person(self):
#         self.person_name = input("Enter Person Name: ")
#         self.person_Age = int(input("Enter person Age: "))
#         self.person_gender = input("Enter Person Gender: ")
#         self.adhar_id = int(input("Enter adhar Number: "))

#     def display_person(self):
#         print(" Name: " , self.person_name)
#         print(" Age:" , self.person_Age)
#         print("Gender: " , self.person_gender)
#         print("Adhar Number: ", self.adhar_id)

# class Employee(person):
    
#     def __init__ (self):
#         self.emp_id = 0
#         self.emp_dept = ""
#         self.emp_salary = 0

#     def enter_Emp(self):
#         self.emp_id = int(input("Enter Employe ID: "))
#         self.emp_dept = input("Enter Employe Department: ")
#         self.emp_salary = int(input("Enter Employee Salary: "))

#     def display_emp(self):
#         print("Employe Id: ",self.emp_id)
#         print("Employe Dept: ", self.emp_dept)
#         print("Employe Salary: ", self.emp_salary)

# # main 
# e1 = Employee()
# e1.enter_person()
# e1.enter_Emp()
# e1.display_person()
# e1.display_emp()


# --------------------------- Que 1

# Create a base class Animal with attributes like species and habitat. Derive classes like Mammal, Bird, and Reptile from it. 
# Include specific attributes like fur type for mammals, feather color for birds, and scale type for reptiles.
# Implement a method in each animal class to display special characteristics of the animal, such as print_special_characteristics().

class Animal:
    def __init__ (self):
        self.species = ""
        self.habitat = ""

    def enter_(self):
        self.species = input("Enter Species: ")
        self.habitat = input("Enter Habitat: ")
    
    def display_(self):
        print("Species: ", self.species)
        print("Habitat: ", self.habitat)

class mammal(Animal):
    def __init__ (self):
        self.fur = ""
        self.name = ""
        self.milk = ""
    def enter_mammal(self):
        self.name= input("Enter Mammal Name: ")
        self.fur = input(" fur or hair: ")
        self.milk = input("produce milk to feed their young(Y/N): ")
    def display_mammal(self):
        print("Name: ", self.name)
        print("Fur / Hair: ", self.fur)
        print("produce milk to feed their young(Y/N): ", self.milk)
        
class Bird(Animal):
    def __init__ (self):
        self.feather_color = ""
        self.bird_name = ""
    def enter_bird(self):
        self.bird_name = input("Enter Bird Name: ")
        self.feather_color = input("Enter Feather Color: ")

    def display_bird(self):
        print("Bird Name: ", self.bird_name)
        print("Feather color: ",self.feather_color)

class Reptile(Animal):
    def __init__ (self):
        self.scale_type = 0
        self.reptile_name = ""
    def enter_Reptile(self):
        self.reptile_name = input("Enter Reptitle Name: ")
        self.scale_type = int(input("Enter adult grown size: "))    
    
    def display_Reptile(self):
        print("Reptile Name: ",self.reptile_name)
        print("Adult grown size: ",self.scale_type)
# main


print("=============================================")
user = mammal()
user.enter_()
user.enter_mammal()
print("=============================================")
user.display_()
user.display_mammal()
print("=============================================")
user = Bird()
user.enter_()
user.enter_bird()
print("=============================================")
user.display_()
user.display_bird()
print("=============================================")
user = Reptile()
user.enter_()
user.enter_Reptile()
print("=============================================")
user.display_()
user.display_Reptile()
print("=============================================")



