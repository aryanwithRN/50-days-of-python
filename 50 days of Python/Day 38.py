# # List Of Object

# # -------------------------------------------------------------------QUE-1----------------------------------------------------------------------------------------
# # Create a Python class LibraryBook with the following attributes and methods:
# # Attributes:
# # book_id (a unique identifier for each book)
# # title (title of the book)
# # author (author of the book)
# # is_available (boolean indicating whether the book is available for borrowing)
# # Methods:
# # borrow_book(): Mark the book as not available if it is currently available. Print a message indicating the successful borrowing or the unavailability of the book.
# # return_book(): Mark the book as available for borrowing. Print a message indicating the successful return.
# # display_book_details(): Print the details of the book, including book ID, title, author, and availability.

# class Library:
#     def __init__ (self):
#         self.Book_ID = 0
#         self.Book_Titel = ""
#         self.Book_Author = ""
#         self.is_available = ""

# # Admin
#     def Enter(self):
#         self.Book_ID = int(input("Enter Book ID: "))
#         self.Book_Titel = input("Enter Book Titel: ")
#         self.Book_Author = input("Enter Book Author: ")
#         self.is_available = input("Is Book Available (T/F / True / False ): ").lower()
   
   
#     def Display(self): 
#         print(self.Book_ID)
#         print(self.Book_Titel)
#         print(self.Book_Author)

#     def Borrow_Book (self) :
#         book=input("Enter book Titel You Want to Borrow: ")
#         for i in range(0,len(list_of_books)):
#             if book==list_of_books[i].Book_Titel:
#                 if list_of_books[i].is_available=="true":
#                     print("Issued successfully")
#                     list_of_books[i].is_available="False"
# # Main
# list_of_books=[]
# while True:
#     print("======================= WellCome to Library ===========================")
# # print("\n")
#     print("       Press - 1 for Admin ")
#     print("       Press - 2 for User ")
#     print("       Press - 3 For Exit ")

#     print("=======================================================================")
#     choice1 = int(input("       Enter 1 (Admin) / 2 (user) / 3 (Exit) :"))

# # //
    
#     if choice1 == 1: 
#         print("=======================================================")
#         print(" ADMIN MENU")
#         print("       1 ENTER BOOK DETAILS")
#         print("       2 ADD NEW BOOKS")
#         print("=======================================================")
#         ch1 = int()
#         n=int(input("Enter the number of books you want to add: "))
    
    
#     for i in range(0,n):
#         B=Library()
#         B.Enter()
#         list_of_books.append(B)

#     for i in range(0,n):
#         list_of_books[i].Display()
#         list_of_books[i].Borrow_Book()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a Python class Product with the following attributes and methods:

# Attributes:

# product={product_id:product_name}
# quantity={product_id:qty}
# price_ = {product_name : price}
# Methods:

# update_price(): Update the price of the product.
# update_quantity(): Update the quantity of the product available in stock.
# display_product_details(): Print the details of the all the products
# enter()

# product_ = {}
# qunty_ = {}
# price_ = {}
# class product():
#     def __init__(self):
#         self.product_id = 0
#         self.product_name = ""
#         self.price = 0
#         self.quantity = 0

#     def Enter(self):
#         N_products = int(input("Enter Number of Products: "))
#         for i in range(0, N_products):
#             self.product_id = int(input("Enter Product Id : "))
#             self.product_name = input("Enter Product Name: ")
#             self.product_price = int(input("Enter Product Price: "))
#             self.quantity = int(input("Enter Quantity of the Product: "))
#             product_ [self.product_id] = self.product_name
#             qunty_ [self.product_id] = self.quantity
#             price_ [self.product_id] = self.product_price 
#         print(product_)
#         print(qunty_)
#         print(price_)

#     def update_price(self):
#         print(product_)

#         id = int(input("Enter id to Update Price: "))

#         for i in price_.keys():
#             if i == id:
#              new_price = int(input("Enter Updated Price For product: "))
#              price_ [id] = new_price
#              print(f"This is Updated Price {price_}")

#     def update_quantity(self):
#         print(qunty_)

#         id = int(input("Enter id to Update Quantity: "))

#         for i, j  in qunty_.items():
#             if i == id: 
#                 if j >= 1:
#                     new_qunty = int(input("Enter Updated Price For product: "))
#                     s = j + new_qunty
#                     j = s
#                     print(f"This is Updated quantity {qunty_}")
    
#     def display_product_details(self):
#         for i,j in price_:
#             print("Product Name: ", i)
#             print("Product price: ", j)


# # Main

# admin = product()
# admin.Enter()
# while True:
#     print(" Menu ")
#     print("       1 For Update price")
#     print("       2 For Update Quantity")
#     print("       3 For Display Details")
#     print("       4 For Exit")
#     choice = int(input("Enter 1/ 2 / 3 / 4: "))
#     if choice == 1: 
#         print("=====  Update Price =====")
#         admin.update_price()
#     elif choice == 2:
#         print("===== Update  Quantity ====== ")
#         admin.update_quantity()
#     elif choice == 3:
#         print('===== Display All Details ======')
#         admin.display_product_details()
#     elif choice == 4:
#         break        


# # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a Python class School with the following attributes and methods:
# Attributes:

# school_name (name of the school)
# location (location of the school)
# students {Admission number:[student name,standard]}
# teachers {Teacher_id:[Teacher_name,subject_name]}

# Methods:
# admit_student(): Add a student object to the dictioanry of students
# hire_teacher(): Add a new teacher
# expel_student(): Remove a student from the list of students 
# based on their student ID.
# terminate_teacher(): Remove a teacher from the dictionary of teachers 
# based on their teacher ID.
# display_school_details(): Print the details of the school, including school name,
# location, all students, and all teachers.

# {Admission number:[student name,standard]}
# {Teacher_id:[Teacher_name,subject_name]}

student = {}
teacher = {}
class School:
    def __init__ (self):
        self.school_name = ""
        self.location = ""
        self.addmission_number = 0
        self.student_name = ""
        self.std = ""
        self.teacher_ID = 0
        self.teacher_name = ""
        self.subject_name = ""

    def admit_student(self):
        # Student
        self.school_name = input("Enter School Name: ")
        self.location = input("Enter School Location: ")
        n_std = int(input("Enter Number of student to Add in School: "))
        for i in range (0, n_std):
            self.student_name = input("Enter Student Name: ")
            self.addmission_number = int(input("Enter Student Addmission Number: "))
            self.std = int(input("Enter Student Standard : "))
            student[self.addmission_number] = [self.student_name,self.std]
        # students {Admission number:[student name,standard]}

        # Teacher
    def hire_teacher(self):
            self.teacher_name = input("Enter Teacher Name: ")
            self.teacher_ID = int(input("ENter Teacher Id: "))
            self.subject_name = input("Enter Subject Name: ")
            teacher[self.teacher_ID] = [self.teacher_name, self.student_name]
            

    def expel_student(self):
        # Remove a student from the list of students based on their student ID.
        remove_id = int(input("Enter ID of Student You Want To Expel: "))
        if remove_id in student.keys():
             print("Student Expel")
             del student[remove_id]
    
    def terminate_teacher(self):
        remove_teacher = int(input("Enter Teacher Id To terminate: "))
        if remove_teacher in teacher.keys():
            print(f" Terminated this Teacher")
            del teacher[remove_teacher]
    
    def display_school_details(self):
    #  Print the details of the school, including school name, location, all students, and all teachers.
        print("School Name: ", self.school_name )
        print("Location : ", self.location )
        

        print("Students:")
        # {Admission number:[student name,standard]}
        for v  in student.values():
                student_name = v[0]
                print("Student Name:", student_name)

        print("Teachers:")
        # {Teacher_id:[Teacher_name,subject_name]}
        for v  in teacher.values():
            teacher_name = v[0]
            print("Teacher NAme: ",teacher_name)
       


# Main
user = School()
while True:
    print("===================== School Menu ==========================" )
    print("1 For Admit Student")
    print("2 For Hire Teacher")
    print("3 For Expel Student")
    print("4 For Terminate Teacher")
    print("5 For Display School Details")
    print("6 For Exit ")

    
    choice = int(input("Enter Choice 1 / 2 / 3 / 4 / 5 / 6 : "))
    print("\n")
    if choice == 1: 
        
        print("==================== Admit Student ========================")
        user.admit_student()  
    elif choice == 2 :
        print("============== Hire Teacher ========================= ")
        user.hire_teacher()
    elif choice == 3: 
        print("============== Expel Student ========================= ")
        user.expel_student()
    elif choice == 4 :
        print("============== Terminate Teacher ========================= ")
        user.terminate_teacher()
    elif choice == 5: 
        print("============== Display School Details ========================= ")
        user.display_school_details()
    elif choice == 6:
        print("============== Exit ================== ")
        break


