# print(" ------------------ Python Assignment ------------------")
# ------------------------------------------------------------------------ Que 1 ------------------------------------------------------------------------------------------------------------
# 1. Odd or Even Number

# soln ------------>

# print("Que 1")
# user_input = int(input("Enter Number to check it Odd / Even: "))
# if user_input % 2 == 0:
#     print(f"{user_input} is Even Number")
# else: 
#     print(f"{user_input} is Odd Number")


# ------------------------------------------------------------------------ Que 2 ----------------------------------------------------------------------------------------------
# 2. write a program that prints out all the elements of the list that are less than 5.

# soln ------------>

# print("Que 2")
# ex_list = [1, 2 ,3 ,4 ,5 ,6 ,7]
# for i in ex_list:
#     if i < 5:
#         print(f"{i} is Less than 5")

# ------------------------------------------------------------------------ Que 3 -------------------------------------------------------------------------------------
# 3. Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

# soln ------------>

# print("Que 3")
# user_input = int(input("Enter A Number: "))
# ls=[]
# for i in range (1, user_input + 1 ):
#     if user_input % i  == 0:
#         ls.append(i)
# print(f"Common Divisor of {i} is {ls}")

# ------------------------------------------------------------------------ Que 4 -------------------------------------------------------------------------------------
#
# 4. Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # and write a program that returns a list that contains only  the 
# elements that are common between the lists   (without duplicates). Make sure your program works on two lists # of different sizes.

# soln ------------>

# print("Que 4")
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# ls = []
# for i in b:
#     for j in a:
#         if i == j:
#             ls.append(i)
# print(f"elements that are common between the lists {ls}")       


# ------------------------------------------------------------------------ Que 5 -------------------------------------------------------------------------------------
# 5.Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# soln ------------>

# print("Que 5")
# ls = [1,2,3,4,5,6,6,7,8,9,10]
# print([i for i in ls if i % 2 == 0])


# ------------------------------------------------------------------------ Que 6 -------------------------------------------------------------------------------------
# 6.Take 2 lists and prepare a list with all values of list1 multiplied to list2
# x = [1, 2, 3]
# y = [5, 10, 15]

# soln ------------>

# print("Que 6")
# x = [1, 2, 3]
# y = [1, 2, 3] #[5, 10, 15]
# ls = []
# for i in range (len(y)):
#     s = x[i] * y[i]
#     ls.append(s)
# print(ls)


# ------------------------------------------------------------------------ Que 7 -------------------------------------------------------------------------------------

# 7. Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# soln ------------>

# print("Que 7")
# def duplicate_val(ls):
#     s = set(ls)
#     return(list(s))
# # main
# ls = [11,12,14,12,14,13]
# user=duplicate_val(ls)
# print(user)

# ------------------------------------------------------------------------ Que 8 -------------------------------------------------------------------------------------

# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string,
#  except with the words in backwards order.
# For example, say I type the string:
#       My name is Michele
# Then I would see the string:
#       Michele is name My

# soln ------------>

# print("Que 8")
# def reverse_karo(string):
#     single_word = string.split() 
#     print(single_word)
#     new_string = ""
#     for i  in single_word:
#         new_string = i + " " +new_string
#     print(new_string)

# user_input = input("Enter long String: ")
# reverse_karo(user_input)

# ------------------------------------------------------------------------ Que 9 -------------------------------------------------------------------------------------
# # Design a class called Country with attributes for name, population, and capital. 
# # Implement a method to check if the country is underpopulated, normally populated or 
# # overpopulated and a display function to display information about the country, including its population and capital. 
# # If population less than 1cr   Underpopulated
# # Population greater than 1cr and less than 80 cr Normal
# # Population greater than 80cr Over populated
# # {country name : [pop, cap]}

# soln ------------>

# print("Que 9")
# dict_country = {}
# class country:
#     def __init__ (self):
#         self.country_name = ""
#         self.country_population = 0
#         self.country_Capital = ""

#     def Enter(self):
#         n_country = int(input("Enter Number Of Country Inputs: "))
#         for i in range (0, n_country):
#             self.country_name = input("Enter Country Name : ").capitalize()
#             self.country_population = int(input("Enter Country Population in Cr(must add cr zero's): "))
#             self.country_Capital = input("Enter the Capital Of Country:  ").capitalize()
#             dict_country[self.country_name] = [self.country_population , self.country_Capital]
    
#     def display_country_details(self):
#         for k,v in dict_country.items():
#             print("Country Name:", k )
#             pop = v[0]
#             print("Country Population: ", pop)
#             cap = v[1]
#             print("Country Capital: ", cap)
    
    
#     def c_underpop(self):
#             for k,v in dict_country.items():
#                 if v[0] < 10000000: 
#                     pop = v[0]
#                     print(f"{k} is under Populated with {pop}")

#     def c_overpop(self):
#             for k,v in dict_country.items():
#                 if v[0] > 800000000: 
#                     pop = v[0]
#                     print(f"{k} is Over Populated with {pop} of population")

#     def c_normalpop(self):
#             for k,v in dict_country.items():
#                 if v[0] > 10000000 and v[0] < 800000000: 
#                     pop = v[0]
#                     print(f"{k} is normal Populated with {pop} of population")

# # main
# user = country() 
# user.Enter()
# while True:
#     print("================ Country menu ================== ")
#     print("     1 For Country Details")
#     print("     2 For Country Under - Populated ")
#     print("     3 For Country Over - Populated ")
#     print("     4 For Country Normal - Populated ")
#     print("     5 For Exit")
#     choice = int(input("Enter Choice 1 / 2 / 3 : "))
#     if choice == 1:
#         print(" ===================== Country Details =================== ")
#         user.display_country_details()
#     elif choice == 2:
#         print(" ===================== Country Under-Populated =================== ")
#         user.c_underpop()
#     elif choice == 3:
#         print(" ===================== Country Over - Populated =================== ")
#         user.c_overpop()
#     elif choice == 4:
#         print(" ===================== Country Normal - Populated =================== ")
#         user.c_normalpop()
#     elif choice == 5:
#         break
    

# ------------------------------------------------------------------------ Que 10 -------------------------------------------------------------------------------------
# Create a Python class Course with the following attributes and methods:
# Attributes:
# course_code (a unique identifier for each course)
# course_name (name of the course)
# instructor (name of the instructor)
# students_enrolled (a list to store student names enrolled in the course)
# Methods:
# add_student(student_name): Add a student to the list of students enrolled in the course.
# remove_student(student_name): Remove a student from the list of students enrolled in the course.
# display_course_details(): Print the details of the course, including course code, course name, instructor, and students enrolled.

# soln ------------>

# print("Que 10")
# students_enrolled = []
# class course:
#     def __init__ (self):
#         self.course_code = 0
#         self.course_name = ""
#         self.instructor = ""
#         self.students_name = ""
    
#     def Enter(self):
#         self.course_code = int(input("Enter Course Code: "))
#         self.course_name = input("Enter Course NAme: ")
#         self.instructor = input("Enter Instructor Name: ")
        

#     def add_student(self):
#         n_std = int(input("Enter Number Of student Who Enrolled: "))
#         for i in range (0, n_std):
#             self.students_name = input("Enter Student Name: ").lower()
#             students_enrolled.append(self.students_name)

#     def remove_student(self):
#         remove_name = input("Enter Student Name tO remove : ").lower()
#         for i in students_enrolled:
#             if remove_name == i:
#                 students_enrolled.remove(i)
#                 print("Student Removed")

#     def display_course_details(self):
#         print("Course Code: ", self.course_code)
#         print("Course Name: ", self.course_name)
#         print("Instructor",self.instructor)
#         for i in students_enrolled:
#          print("Student Enrolled:", i)
        
# user = course()
# user.Enter()
# while True:
#     print("============== Menu =================== ")
#     print("         1 For Add Student")
#     print("         2 For Remove Student")
#     print("         3 For Display Course")
#     print("         4 For Exit")
#     choice = int(input("Enter Choice 1 / 2 / 3 / 4 :"))
#     if choice == 1:
#         print("=================== Add Student ===================== ")
#         user.add_student()
#     elif choice == 2: 
#         print("================== Remove Student ====================")
#         user.remove_student()
    
#     elif choice == 3:
#         print("=================== Display Students Detials ==================== ")
#         user.display_course_details()

#     elif choice == 4:
#         print("bye bye Exit")
#         break