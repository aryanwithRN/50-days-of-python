# Que (1)
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.Take following input from user
# Number of classes held Number of classes attended.And print percentage of class attended Is student is allowed to sit in exam or not.
# ---->
# number_of_classes_held = int(input("Number of classes You Held: "))
# number_of_classes_attend = int(input("Number of classes You Attend: "))
# if (number_of_classes_attend <= number_of_classes_held):
#     percent = (number_of_classes_attend / number_of_classes_held) * 100
#     print(percent)
    
#     if (percent >= 75):
#         print ("You are allow to seat in Exam")
#     else :
#         print ("Come Next Year Bro!")
# else:
#     print ("Ky Enter Ker rahe ho yr, jada kaise Attend kr diya") 


# Que (2)
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
# --->
# year_of_service = int(input("Year of Service: "))
# salary = float(input("Enter Your salary Amount: "))
# bonus = salary * (5 /100) 
# # print(bonus)
# if (year_of_service >= 5):
#     print(bonus)
# else:
#     print("You are Not Able to redeem Bonus")
    
# Que (3)
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity
# Suppose, one unit will cost 100. Judge and print total cost for user.
# --->
# total_units = eval (input("Enter Your Number Of Units: "))
# Cost_of_units = eval (input("Enter Cost of units: "))
# total_cost = (total_units * Cost_of_units)
# print("Your Total Cost is", total_cost)
# discount = (total_cost * 10 / 100)
# if (total_cost > 999):
#  print(" 10% Discount on totall is ", total_cost - discount )
 
# else:
#     print("No Discount Available")

# Que (4)
# Write a program that determines whether a given year is a leap year or not.
# --->
# no_of_year = int (input("Enter Year: "))
# if (no_of_year % 4)== 0:
#  print("It's a leap Year") 
# else:
#     print("Not Leap Year")
 
 
 
    
# Que (5)
# Write a program that asks the user for their age and determines the ticket price for a movie:
# Age 0-5: Free
# Age 6-12: $5
# Age 13-18: $10
# Age 19 and above: $15
# ---->

# age = int (input("Enter Your Age: "))
# if (age <= 5):
#  print("Free")

# elif (age <=12 ):
#  print("Your Ticket  Price is $5")
# elif (age <=18 ):
#  print("Your Ticket  Price is $10")
# elif (age >= 19  ):
#  print("Your Ticket  Price is $15")
 
 
# Que (6)
# Create a program that takes three angles as input and classifies the type of triangle based on the angles:
# Equilateral: All three angles are equal.
# Isosceles: Two angles are equal.
# Scalene: No angles are equal.
# --->

# angle_input_1 = eval (input("Enter Angle One : "))
# angle_input_2 = eval (input("Enter Angle Two : "))
# angle_input_3 = eval (input("Enter Angle Three : "))
# if (angle_input_1 == angle_input_2 == angle_input_3):
#     print ("Equilateral Triangle")
# elif (angle_input_1 == angle_input_2 or angle_input_3):
#     print ("Isosceles Triangle")
# else:
#     print("Scalene Triangle")
    
    
    
    
    
# Que (7)
# Write a program that asks the user to enter the total purchase amount and then calculates the discounted price based on the following conditions:
# If the purchase amount is greater than $100, apply a 10% discount.
# If the purchase amount is between $50 and $100 (inclusive), apply a 5% discount.
# If the purchase amount is less than $50, no discount is applied.
# --- > 
# total_purchase_amount = eval (input ("Enter Your total Purchase Amount in $: "))
# if (total_purchase_amount > 100):
#     final_price =(total_purchase_amount *10)/100
#     print("Your Discounted Value is $",final_price)
#     print("Final Amount is ",total_purchase_amount - final_price )
# elif(total_purchase_amount >= 50 and total_purchase_amount <= 99):
#     final_price = (total_purchase_amount *5)/100
#     print("Your Discounted Value is $",final_price)
#     print("Final Amount is", total_purchase_amount - final_price )
# elif(total_purchase_amount < 50):
#     print("No discount is applied, Your Total is $", total_purchase_amount)
    
    
    
    
# Que (8)
# Write a program that converts temperatures between Celsius and Fahrenheit. 
# Ask the user to enter a temperature and its unit (C or F), then convert and print the result.
# --- >

# temperature = eval (input("Enter Temerature: "))
# unit = (input ("convert to C / F: "))
# if (unit == "C"):
#     c = temperature * 9/5 + 32
#     print ("Celsius",c)
# elif (unit == "F"):
#     f = (temperature-32)*5/9
#     print("Fahrenheit",f)
    
    
    
    
    
# Que (9)
# Create a program that takes a number (1-7) as input and prints the 
# corresponding day of the week (1-Monday, 2-Tuesday, ..., 7-Sunday).
# --->
# take_a_number = int(input("Enter a Number 1-7: "))
# if ( take_a_number == 1):
#     print("Monday")
# elif ( take_a_number == 2 ):
#     print("Tuesday")
# elif ( take_a_number == 3 ):
#     print("Wednesday")
# elif ( take_a_number == 4 ):
#     print("Thursday")
# elif ( take_a_number == 5 ):
#     print("Firday")
# elif ( take_a_number == 6 ):
#     print("Saturday")
# elif ( take_a_number == 7 ):
#     print("Sunday")
    
    
# # elif(take_a_number > 7):
# #     print("Invalid Day")


# else:
#     print("Invalid Day")



