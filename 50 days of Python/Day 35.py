# -------------------------------------------------------------------QUE-1----------------------------------------------------------------------------------------
# Create a Python class LibraryBook with the following attributes and methods:
# Attributes:
# book_id (a unique identifier for each book)
# title (title of the book)
# author (author of the book)
# is_available (boolean indicating whether the book is available for borrowing)
# Methods:
# borrow_book(): Mark the book as not available if it is currently available. Print a message indicating the successful borrowing or the unavailability of the book.
# return_book(): Mark the book as available for borrowing. Print a message indicating the successful return.
# display_book_details(): Print the details of the book, including book ID, title, author, and availability.

# books={}  {id:title}
# author={}   {title:author}
# {'Life': 'Me', 'Job': 'They', 'Coding': 'Jason'}
is_available = {}
class Library_in_Book:
    def __init__ (self):       
        # User issued
        self.book_id = 0
        self.titel = None
        self.author = None
        self.d1 = dict({}) 
        self.d2 = dict({})
        self.number = 0
        self.is_available = None

    def Enter(self):
        self.number = int(input("Enter number of Books in Library: "))
        for i in range (1 , self.number + 1):
         self.book_id = int(input("Enter Book Id: "))
         self.titel = input("Enter Book Title: ").capitalize()
         self.author = input ("Enter Book Author:").capitalize()
         self.is_available = True
         self.d1[self.book_id] = self.titel
         self.d2[self.titel] = self.author
         is_available[self.titel] = self.is_available
    

    def borrow_book(self):
        borrow_input = input("Enter Book title You want to borrow: ").capitalize()
        if borrow_input in self.d2.keys():
            if is_available[borrow_input] == True:
                print("Book Issued !\nThank You :)")
                is_available[borrow_input] = False
            else:
                print("Book is issued to SomeOne else. ")
        else:
            print("Book is Not Available in Library")

    def return_book(self):
        return_input = input("Enter Book Title You Want to Return: ").capitalize()
        if return_input in self.d1.values():
            print(f"{return_input}: Book is returned. ")
   
    def update_book(self):
        new_book = input("Enter New Book Titel: ").capitalize()
        new_book_author = input("Enter Author of New Book: ").capitalize()

        if new_book not in self.d1.values():
            id = int(input("Enter Book ID: "))
            while id in self.d1.keys():
                id = int(input("Enter New Book ID : "))
                self.d1[self.book_id] = new_book
                is_available[new_book] == True
                self.d2[new_book] = new_book_author
                print("Great Success !! \n Library is updated with the new books\n\n")
                break
                       

    def display(self):
        print(f"Books In Lab:- {self.d2}")
       
# Main :
admin = Library_in_Book() 
while True:
    print("======================= WellCome to Library ===========================")
# print("\n")
    print("       Press - 1 for Admin ")
    print("       Press - 2 for User ")
    print("       Press - 3 For Exit ")

    print("=======================================================================")

    choice1 = int(input("       Enter 1 (Admin) / 2 (user) / 3 (Exit) :"))
    if choice1 == 1:
        print("=======================================================")
        print(" ADMIN MENU")
        print("       1 ENTER BOOK DETAILS")
        print("       2 ADD NEW BOOKS")
        print("=======================================================")
        menu_Admin = int(input("Enter your choice from the above menu :"))
        if menu_Admin == 1:
            admin.Enter()
        elif menu_Admin == 2:
            admin.update_book()   
    elif choice1 == 2:
        print("=======================================================")
        print(" User MENU")
        print("      1 For Borrow Book")
        print("      2 For Return Book")
        print("      3 For Display All Book Details")
        print("=======================================================")
        menu_Admin_1 = int(input("Enter your choice from the above menu :"))
        
        if menu_Admin_1 == 1:
            admin.borrow_book()
        elif menu_Admin_1 == 2:
           admin.return_book()
        elif  menu_Admin_1 == 3:
            admin.display()
    
    elif choice1 == 3:
        break
    # admin.display()

