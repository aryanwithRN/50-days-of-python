# Base Class: Weather
# display_conditions(self):
# Displays the current weather conditions, including temperature, humidity, and any other relevant information.
# update_conditions(self, new_temperature, new_humidity):
# Updates the temperature and humidity based on new data received from a weather sensor.

# Derived Class 1: DailyWeather
# predict_weather(self):
# Provides a general prediction of the weather for the entire day based on the current conditions and historical data.

# display_sunrise_sunset(self):
# Displays the expected sunrise and sunset times for the day.

# Derived Class 2: HourlyWeather
# predict_hourly_conditions(self, hour):
# Provides a more detailed prediction of the weather conditions for a specific hour of the day.

# display_time_of_day(self, hour):
# Determines and displays the time of day (morning, afternoon, evening) based on the given hour.


# Conditions:

# For DailyWeather:
# If the (temperature) is between 20 and 30 degrees Celsius and (humidity) is between 40% and 60%, predict a mild and pleasant day.
# If the temperature is above 30 degrees Celsius and humidity is less than 40%, predict a hot and dry day with possible heatwaves.
# If the temperature is below 20 degrees Celsius and humidity is above 60%, predict a cool day with a chance of rain.
# If none of the above conditions are met, provide a general daily weather prediction based on current conditions.

# For HourlyWeather:
# If the hour is between 6 AM and 12 PM, predict clear skies with moderate temperatures for the morning.
# If the hour is between 12 PM and 6 PM, predict rising temperatures and a chance of rain for the afternoon.
# If the hour is between 6 PM and 12 AM, predict cooling temperatures with a chance of thunderstorms for the evening.
# If none of the above conditions are met, provide a general hourly weather prediction based on current conditions.



# class Weather:
#     def __init__(self):
#         self.temperature = 0
#         self.humidity = 0

#     def _enter (self):
#         self.temperature = int(input ("Enter Temperature: "))
#         self.humidity = int(input("Enter Humidity: "))
#         # self.hour = int(input("Enter Time (based On 24 hr format): "))

#     def _display(self):
#         print("Temperature:" , self.temperature)
#         print("Humidity:" , self.humidity)

#     # update_conditions(self, new_temperature, new_humidity):
#     def update_(self):
#         self.new_temperature = int(input("Enter New Temperature: "))
#         self.new_humidity = int(input("Enter New Humidity: "))

#     def update_display(self):
#         print("New Temperature: ", self.new_temperature)
#         print("New Humidity: ", self.new_humidity)

# class daily_weather(Weather):
    
#     def predict_weather(self):

# #  If the (temperature) is between 20 and 30 degrees Celsius and (humidity) is between 40% and 60%, predict a mild and pleasant day
#         if self.temperature > 20 and self.temperature < 30:
#             if self.humidity >40 and self.humidity < 60: 
#                 print("It's a mild and pleasant day")

# # If the temperature is above 30 degrees Celsius and humidity is less than 40%, predict a hot and dry day with possible heatwaves.
#         elif self.temperature >= 30 and self.humidity < 40:
#             print("It's a hot and dry day with possible heatwaves.")

# # If the temperature is below 20 degrees Celsius and humidity is above 60%, predict a cool day with a chance of rain.            
#         elif self.temperature < 20 and self.humidity > 60:
#             print("It's a cool day with a chance of rain")

# # If none of the above conditions are met, provide a general daily weather prediction based on current conditions.
#         else:
#             print("Decent Day")

#     def display_sunrise_sunset(self):
#         print("At 6am it's Sunrise")
#         print("At 6:30pm it's Sunset")

# class HourlyWeather(Weather):

#     def predict_hourly_conditions(self, hour):
# # If the hour is between 6 AM and 12 PM, predict clear skies with moderate temperatures for the morning.
#         if hour > 6 and hour < 12:
#             print("clear skies with moderate temperatures for the morning.")

# # If the hour is between 12 PM and 6 PM, predict rising temperatures and a chance of rain for the afternoon.
#         elif hour > 12 and hour < 16:
#             print("Rising temperatures and a chance of rain for the afternoon") 

# # If the hour is between 6 PM and 12 AM, predict cooling temperatures with a chance of thunderstorms for the evening.
#         elif hour > 18 and hour < 24:
#             print("cooling temperatures with a chance of thunderstorms for the evening")

#         else:
#             print("ha hai Accha din ")



# # main
# while True:            
#     print("========================  Weather Menu  ======================== ")
#     print("         1 For Daily Weather ")
#     print("         2 For Hourly Weather ")
#     print("         3 For Exit ")
#     choice = int(input("Enter Choice 1 / 2 / 3 :"))
#     if choice == 1:
#         user = daily_weather()
#         user._enter()
#         user.predict_weather()
#         user._display()
#         user.display_sunrise_sunset()

#     elif choice == 2: 
#         user = HourlyWeather()
#         user._enter()
#         hour = int(input("Enter Time (Based on 24hr Format): "))
#         user.predict_hourly_conditions(hour)
#         user._display()
        
#     elif choice == 3:
#         break




# Design a base class Product with attributes like product ID, name, and price. 
# Derive classes ElectronicProduct and ClothingProduct from it.
# Include specific attributes like brand and warranty for electronic products, and size and material for clothing products.
# add_to_cart(self, quantity):

# Adds a specified quantity of the product to the user's shopping cart.
# calculate_discount(self, discount_percentage):

# Calculates and applies a discount to the product's price based on the given percentage.

# elec = []
# cloth = []
# ls1 = []
# ls = []
# class Product:
#     def __init__(self):
#         self.product_id = 0
#         self.product_name = ""
#         self.product_price = 0
        
#     def _enter(self):
#         self.product_id = int(input("Enter Product ID: "))
#         self.product_name = input("Enter Product Name: ")
#         self.product_price = int(input("Enter Product Price : "))

#     def _display(self):
#         print("Product ID: ", self.product_id)
#         print("Product Name: ", self.product_name)
#         print("Product Price: ", self.product_price)

# class ElectronicProduct(Product):
    
#     def brand_and_warranty(self):
#         self.brand = input("Enter Product Brand: ")
#         self.warranty = input("Enter Warranty On that Product: ")

#         elec.append(self.product_id)
#         elec.append(self.product_name)    
#         elec.append(self.product_price)

#     def  add_to_cart_elect(self):
#         ID = int(input("Enter Product ID: "))
#         if ID  in elec:
#             quantity = int(input("ENter The Quantity: "))
#             ls1.append(quantity)  
#             elec.append(ls1)
#             print(f"Your Cart, {elec}") 
    
    
#     def display_brand_and_warranty(self):
#         print("Brand: ", self.brand)
#         print("Warranty: ", self.warranty)
        

# class ClothingProduct(Product):
#     def size_and_material(self):
#         self.size = input("Enter Size (s / m / L / xL / xxL): ")
#         self.material = input("ENter Material (cotton/ slik): ")

#     def  add_to_cart_cloth(self):
#         cloth.append(self.product_id)
#         cloth.append(self.product_name)
#         cloth.append(self.product_price)
#         ID = int(input("Enter Product ID: "))
#         if ID  in cloth:
#             quantity = int(input("ENter The Quantity: "))
#             ls.append(quantity)  
#             cloth.append(ls)
#             print(cloth)
    
#     def display_size_matterial(self):
#         print("Cloth Size: ", self.size)
#         print("Cloth Material: ", self.material)
#         # print("Your Cart", ls)

    

# # main

# while True:
#     print("================== Ali baba Express =========================")
#     print("     1 For Electronic Products")
#     print("     2 For Cloth Product")
#     print("     3 For Exit")
#     choice = int(input("Enter Choice 1 / 2 / 3 :"))
#     if choice == 1:
#         user= ElectronicProduct()
#         user._enter()
#         user.brand_and_warranty()
#         user._display()
#         user.display_brand_and_warranty()
#         user.add_to_cart_elect()
#     elif choice == 2:
#         user= ClothingProduct()
#         user._enter()
#         user.size_and_material()
#         user._display()
#         user.display_size_matterial()
#         user.add_to_cart_cloth()

#     elif choice == 3:
#         break




# ----------------------------------------------------------------------- flight ticket Que ---------------------------------------------------------------------------------------------------

#Flight

#Attributes= flight_no,start_city,destination,airlines, flight_type=(domestic/international), 
#baggage_allowed(in kgs), fare_type={"Business":fare,"Economy":fare},
#refreshements={"Name of the item":},seat_fare={"Middle":350,"Aisle":400,"Window":500}

#Functions
#flight_enter()- to take entries for  all flight attributes
#flight display()- to display all flight details

#Customer(Flight)

#Attributes= c_name, c_id,ticket_class=(Business/economy), baggage=in kgs,
# if baggage is greater the allowed baggage weight( for every 5 kgs extra add 700 to the fare)
# seat_type=(window,middle,aisle), total_payable_amount

#Functions:
#cus_enter()- to take input for all customer attributes
#cus_display()- to display all the customer details
#assign_ticket_class()
#assign_seat_type()
#calc_baggage_cost()
#amount()- display the total payable amount for booking the flight

# d1 = {}
# fare_type = {}
# menu_dict = {}
# menu_dict["ref"]  = {
#                                 "Soft Drink" : 120,
#                                 "Water Bottel" : 80,
#                                 "Veg-Meal Box" : 300,
#                                 "non-veg Meal Box" : 400,
#                                 "High- Protine Veg SandWich" : 180,
#                                 "Cup Noodel" : 150
#                             }
# sum_of_ref_bus = sum(menu_dict["ref"].values())

# menu_eco = {}
# menu_eco["food"] = { 
#                     "Soft Drink" : 80,
#                     "Water Bottel" : 40,
#                     "Veg-Meal Box" : 200,
#                     "non-veg Meal Box" : 300,
#                     }
# sum_of_ref_eco = sum(menu_eco["food"].values())

# seat_fare = {}
# seat_fare["Seat Fare"]  =  {
#                                 "Middle":350,   
#                                 "Aisle":400,    
#                                 "Window":500
#                                 }
# class Flight_Booking:
#     def __init__(self):
#         self.flight_number = "" 
#         self.flight_name = ""
#         self.takeoff_city = ""
#         self.Landing_city = ""
#         self.flight_type = ""
#         self.fare_1 = 10000
#         self.fare_2 = 5000
#         self.kg = 0

#         # PAssenger Info >
#         self.passanger_name = ""
#         self.passanger_id = ""
#         self.ticket_class =  ""
#         self.kg = 0
#         self.seat_type = ""
#         self.extra_cost = 0
#         self.extra_cost1 = 0
#         self.cost = 0
#         self.cost1 = 0

#     def _enter(self):
#         self.flight_number = input("Enter Flight Number : ").upper()
#         self.flight_name = input("Enter Flight Name : ").upper()
#         self.takeoff_city = input("Enter Take-Off City :  ").upper()
#         self.Landing_city = input("Enter Landing City: ").upper()
#         self.flight_type = input("Enter Flight Type( Domestic / International ) : ").upper()
#         d1[self.flight_number] =  { 
#                                     "Flight Number" : self.flight_number,
#                                     "Airline" : self.flight_name,
#                                     "Take-Off City": self.takeoff_city , 
#                                     "Landing City" : self.Landing_city,
#                                     "Flight Type" : self.flight_type
                                    
#                                     }
    
   
    
#     def display_flight(self):
#         print(" ==================== FLIGHT DETAILS ============================ ")
#         print("Flight Number : ", self.flight_number)
#         print("Airline : ", self.flight_name)
#         print("Take-Off City : " , self.takeoff_city)
#         print("Destination City :" , self.Landing_city)
#         print("Flight Class: ", self.flight_type)


#     def fare_type(self):
#         fare_type["Fare Type"] = {
#                         "Business": self.fare_1,
#                         "Economy": self.fare_2,
#                         }
  
#     def display_refreshment(self):
#             print("================ ON BOARD MENU ======================= ")
#             print("     Soft Drink price:", "₹",menu_dict["ref"]["Soft Drink"])
#             print("     Water Bottel price:", "₹",menu_dict["ref"]["Water Bottel"])
#             print("     Veg-Meal Box price:", "₹",menu_dict["ref"]["Veg-Meal Box"])
#             print("     Non-veg Meal Box price:", "₹",menu_dict["ref"]["non-veg Meal Box"])
#             print("     High- Protine Veg SandWich price:", "₹",menu_dict["ref"]["High- Protine Veg SandWich"])
#             print("     Cup Noodel price:", "₹",menu_dict["ref"]["Cup Noodel"])
#             print(f"You Get this all above menu Just at ₹{sum_of_ref_bus} and it added to your Ticket" )

#     def display_refreshment_eco(self):
#             print("================ ON BOARD MENU ======================= ")
#             print("     Soft Drink price:", "₹",menu_eco["food"]["Soft Drink"])
#             print("     Water Bottel price:", "₹",menu_eco["food"]["Water Bottel"])
#             print("     Veg-Meal Box price:", "₹",menu_eco["food"]["Veg-Meal Box"])
#             print("     Non-veg Meal Box price:", "₹",menu_eco["food"]["non-veg Meal Box"])
#             print(f"You Get this all above menu Just at ₹{sum_of_ref_eco} and it added to your Ticket" )




# class passenger(Flight_Booking):
#     def passenger_enter(self):
#         self.passanger_name = input("Enter Passanger Name: ").upper()
#         self.passanger_id = input("Enter Passanger ID: ").upper()
#         self.ticket_class =  input("Enter Travel Class (Business/economy): ").upper()
#         self.seat_type = input("Enter Seat Choice (Aisle / Middle / Window ): ").upper()
#         self.kg = int(input("Enter Totall Baggage Weight: "))
    
   
    

#     def display_passenger(self):
#         print(" ==================== PASSENGER DETAILS ============================ ")
#         print("         Passenger Name: ", self.passanger_name)
#         print("         Passenger ID : ", self.passanger_id)
#         print("         Flight Class : ", self.ticket_class)
#         print("         Baggage Weight :", self.kg)

    
#     #baggage_allowed(in kgs)   
        
#     def baggage_allowed_Eco(self):
        
#         if self.kg > 30 :
#             s = self.kg - 30
#             if s >= 5 or s <=10:
#                 self.extra_cost = 1000
#             elif s < 5:
#                 self.cost = 500

#     def baggage_allowed_bussines(self):

#         if self.kg > 40 :
#             s = self.kg - 40
    
#             if s >= 5 or s <=10:
#                 self.extra_cost = 1000
#             elif s < 5:
#                 self.cost = 500


#     # def ticket_price(self):
                
#     def food_menu(self):
#         if self.ticket_class == "BUSINESS":
#             pass


#     def calc_Ticket(self):
#         if self.seat_type == "AISLE":
#             if self.ticket_class == "BUSINESS":
#                 t_price = seat_fare["Seat Fare"]["Aisle"] + self.fare_1 + sum_of_ref_bus + self.extra_cost1 or self.cost1
#                 print("Your Total Business class cost is, ₹", t_price, "only for AISLE Seat ")
            
#             elif self.ticket_class == "ECONOMY":
#                 t_price1 = seat_fare["Seat Fare"]["Aisle"] + self.fare_2 + sum_of_ref_eco + self.extra_cost or self.cost
#                 print("Your Total Economy class cost is, ₹", t_price1, "only for AISLE Seat" )
        
#         elif self.seat_type == "MIDDLE":
#             if self.ticket_class == "BUSINESS":
#                 t_price = seat_fare["Seat Fare"]["Middle"] + self.fare_1 + sum_of_ref_bus + self.extra_cost1 or self.cost1
#                 print("Your Total Business class cost is, ₹", t_price, "only for MIDDLE Seat ")

#             elif self.ticket_class == "ECONOMY":
#                 t_price1 = seat_fare["Seat Fare"]["Middle"] + self.fare_2 + sum_of_ref_eco + self.extra_cost or self.cost
#                 print("Your Total Economy class cost is, ₹", t_price1, "only for MIDDLE Seat" )

#         elif self.seat_type == "WINDOW":
#             if self.ticket_class == "BUSINESS":
#                 t_price = seat_fare["Seat Fare"]["Window"] + self.fare_1 + sum_of_ref_bus + self.extra_cost1 or self.cost1
#                 print("Your Total Business class cost is, ₹", t_price, "only for WINDOW Seat ")

#             elif self.ticket_class == "ECONOMY":
#                 t_price1 = seat_fare["Seat Fare"]["Window"] + self.fare_2 + sum_of_ref_eco + self.extra_cost or self.cost
#                 print("Your Total Economy class cost is, ₹", t_price1, "only for WINDOW Seat" )
# # main
# # admin.display_refreshment()


# while True: 
#     print("============================ FLIGHT MENU ============================= ")
#     print("        1 For Admin")
#     print("        2 For Passanger")
#     print("        3 For Exit")
#     choice = int(input("Enter Choice 1 / 2 / 3 : "))
#     if choice == 1:
#         admin = Flight_Booking()
        
        
#         print("========================== ADMIN MENU ==========================")
#         print("     1 For Enter Flight Details")
#         print("     2 For Flight Details")
#         print("     3 For Exit")
#         admin_choice = int(input("Enter 1 / 2 / 3 : "))
#         while True:
#             if admin_choice == 1:
#                 print("=============== Enter Flight Details ===================== ")
#                 admin._enter()
#             elif admin_choice == 2:
#                 admin.display_flight()
#             elif admin_choice == 3:
#                 break


#     elif choice == 2:
#         user = passenger()
        
#         print("========================== PASSENGER MENU ==========================")
#         print("     1 For Enter Passenger Details")
#         print("     2 For Display Passenger Details")
#         print("     3 For Ticket Details")
#         print("     4 For Exit")
#         User_choice = int(input("Enter 1 / 2 / 3 / 4: "))
#         while True:
#             if User_choice == 1:
#                 print("====================== Enter Passenger Details ================================ ")
#                 user.passenger_enter()
#                 if (user.ticket_class) == "BUSINESS":
#                     print("========== BUSINESS CLASS FOOD MENU ============== ")
#                     user.display_refreshment()
#                 elif (user.ticket_class) == "ECONOMY":
#                     print("=========== ECONOMY CLASS FOOD MENU =============== ")
#                     user.display_refreshment_eco()
#             elif User_choice == 2:
#                 user.display_passenger()

#             elif User_choice == 3:
#                 user.calc_Ticket()

#             elif User_choice == 4:
#                 break

#     elif choice == 3:
#         break
            

# user = Flight_Booking()
# user._enter()
# kg = int(input("Enter Totall Baggage Weight: "))
# user.baggage_allowed_Economy(kg)
# user.baggage_allowed_bussines(kg)
# user.refreshment()
# user.fare_type()
            
            # print("     3 For Refreshment Menu")
            # print("     4 For Ticket Fair(base price)")
