# Create a Python class ShoppingCart with the following attributes and methods:

# Attributes:
# items={item_id:{name:, price:}}
# coupon={item_id:discount_available}
# qty={item_id:qty}

# Methods:
#Admin
# add_item(): Add a specified quantity of an item to the cart with its price.
# remove_item(): Remove a specified quantity of an item 
#from the cart. If the quantity becomes zero, remove the item from the cart.
#update _items()

#USER
# add_to_cart()- User side function to add items to the cart and calculate the total value of the cart
# display_cart_details(): Print the details of items in the cart,


d2 = {}
class Amart:
    def __init__(self):
        self.item_id = 0
        self.item_name = ""
        self.item_price = 0
        self.item_Quantity = 0
        
        self.ls = []
 
# Admin wala Kam

    def add_item (self):
         for i in range (0, 2):
          self.item_id = int(input("ENter Item ID : "))
          self.item_name = input("ENter Item Name : ")
          self.item_price = int(input("ENter Item Price : "))
          self.itemQuantity =  int(input("enter a Item Quantity : "))
         
          d1 =  {
                        "ID" : self.item_id, 
                        "Item_Name": self.item_name , 
                        "Price": self.item_price, 
                        "Qnty": self.item_Quantity
                }
          
          d2[self.item_id] = d1
        #  print(d2)
    
    
    def remove_item(self):
        print(self.d1)
        print("Select the above if want to delete!")
        remove_item = int(input("Enter Item Id To Remove: "))
        if remove_item in d2.keys():
             print("Item Removed")
             del d2[self.item_id]
             
    def update_item(self):
         n = int(input("Enter Number of Item to Add: "))
         for i in range (0, n):
          self.item_id_1 = int(input("ENter Item ID : "))
          self.item_name_1 = input("ENter Item Name : ")
          self.item_price_1 = int(input("ENter Item Price : "))
          self.itemQuantity =  int(input("enter a Item Quantity : "))
          d2[self.item_id_1] = {self.item_name_1 , self.item_price_1}
    
    
    def display_Item(self):
         print("="*10)
         for i in d2.values():
                print("ID:", i["ID"])
                print("Name:", i["Item_Name"])       
                print("Price:", i["Price"])
                print("Qnty:", i["Qunty"])
 
 # user wala Kam
    
    def add_to_cart(self):
         print(d2)
         user_input = int(input("Enter Item ID to Add To cart: "))
         for k in d2.keys():
          if k in d2.items():
            New_Quantity = int(input("PLease Enter Quantity : "))
            self.ls.append(k["Item_Name"])
            self.ls.append(k["Price"])
            self.ls.append(New_Quantity)
   
        
    def display_cart(self):
         for i in d2:
              print(i)
# Main
user = Amart()
while True:
    print("=================== Amart store =========================")
    print("Menu")
    print("    1 For Admin")
    print("    2 For user")
    print("    3 For Exit ")
    print("=" * 30)
    choice = int(input("Enter 1 / 2 / 3 : "))
    while True:
     if choice == 1: 
        
        print("Wellcome To Admin Menu =================")
        print("         1 For Add Item")
        print("         2 For Remove Item")
        print("         3 For Add More Items")
        print("         4 For Display Items")
        print("         5 For Exit")
        print("=" * 15)
        choice1 = int(input("Enter 1 / 2 / 3 / 4:"))
        
        if choice1 == 1:
                print("Add Items To Store")
                user.add_item()
        elif choice1 == 2:
                print("Remove Item From Store ")
                user.remove_item()
        elif choice1 == 3:
                print("Add / Update More Item To Store ")
                user.update_item()
        elif choice1 == 4:
             print("Display Items ")
             user.display_Item()
        elif choice1 == 5:
             break
     
     elif choice == 2 :

        print(" Wellcome To User Menu ==========================")
        print("         1 For Add To Cart")
        print("         2 For Display Cart Details")
        print("         3 For Exit")
        print("=" * 15)
        choice2 = int(input("Enter 1 / 2 / 3 :"))
        
        if choice2 == 1:
                print("Add To Cart")
                user.add_to_cart()
        elif choice2 == 2:
                print(" Display Cart Details")
                user.display_cart()
        elif choice2 == 3:
                break
     
     elif choice == 3:
        break