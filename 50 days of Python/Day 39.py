# Design a class called Country with attributes for name, population, and capital. 
# Implement a method to check if the country is underpopulated, normally populated or 
# overpopulated and a display function to display information about the country, including its population and capital. 
# If population less than 1cr   Underpopulated
# Population greater than 1cr and less than 80 cr Normal
# Population greater than 80cr Over populated
# {country name : [pop, cap]}

dict_country = {}
class country:
    def __init__ (self):
        self.country_name = ""
        self.country_population = 0
        self.country_Capital = ""

    def Enter(self):
        n_country = int(input("Enter Number Of Country Inputs: "))
        for i in range (0, n_country):
            self.country_name = input("Enter Country Name : ").capitalize()
            self.country_population = int(input("Enter Country Population in Cr(must add cr zero's): "))
            self.country_Capital = input("Enter the Capital Of Country:  ").capitalize()
            dict_country[self.country_name] = [self.country_population , self.country_Capital]
    
    def display_country_details(self):
        for k,v in dict_country.items():
            print("Country Name:", k )
            pop = v[0]
            print("Country Population: ", pop)
            cap = v[1]
            print("Country Capital: ", cap)
    
    
    def c_underpop(self):
            for k,v in dict_country.items():
                if v[0] < 10000000: 
                    pop = v[0]
                    print(f"{k} is under Populated with {pop}")

    def c_overpop(self):
            for k,v in dict_country.items():
                if v[0] > 800000000: 
                    pop = v[0]
                    print(f"{k} is Over Populated with {pop} of population")

    def c_normalpop(self):
            for k,v in dict_country.items():
                if v[0] > 10000000 and v[0] < 800000000: 
                    pop = v[0]
                    print(f"{k} is normal Populated with {pop} of population")

# main
user = country() 
user.Enter()
while True:
    print("================ Country menu ================== ")
    print("     1 For Country Details")
    print("     2 For Country Under - Populated ")
    print("     3 For Country Over - Populated ")
    print("     4 For Country Normal - Populated ")
    print("     5 For Exit")
    choice = int(input("Enter Choice 1 / 2 / 3 : "))
    if choice == 1:
        print(" ===================== Country Details =================== ")
        user.display_country_details()
    elif choice == 2:
        print(" ===================== Country Under-Populated =================== ")
        user.c_underpop()
    elif choice == 3:
        print(" ===================== Country Over - Populated =================== ")
        user.c_overpop()
    elif choice == 4:
        print(" ===================== Country Normal - Populated =================== ")
        user.c_normalpop()
    elif choice == 5:
        break
    

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