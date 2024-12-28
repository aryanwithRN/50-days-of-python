#---------------------------------------------------------------------------------- Ex-1----------------------------------------------------------------------------------------------------
# Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

# user_input= int(input("Enter a Value: "))
# x = int(input("Enter New Number: "))
# try:
#     user_input.append(x)
# except AttributeError:
#     print("Append Nhi kar sakte list nhi hai apne pass")


# try:
#     x = 10
#     x.append(6)
#     raise AttributeError()
# except AttributeError:
#     print("Attribute Errror encountered ")
# except:
#     print("Alag error mila ")

# --------------------------------------------------------------------------------OP-1---------------------------------------------------------------------------------------------
# Excepted values is 13 1, but 12.0 flot value not possible and string too
# try:
#     value = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# else:
#     print(f"Input accepted: {value}")
# finally:
#     print("Finally block executed.")


# --------------------------------------------------------------------------------OP-2---------------------------------------------------------------------------------------------
# try:
#     number = int("42")
#     result = 10 / number
# except ValueError as ve:
#     print(f"ValueError: {ve}")
# except ZeroDivisionError as zde:
#     print(f"ZeroDivisionError: {zde}")
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print("No exception occurred.")
# finally:
#     print("Finally block executed.")

# --------------------------------------------------------------------------------OP-3---------------------------------------------------------------------------------------------
#IIMP
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

# --------------------------------------------------------------------------------OP-4---------------------------------------------------------------------------------------------
# REAson : A new exception class must inherit from a BaseException. There is no such inheritance here.
# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("someError has not occurred")
# except "someError":
#     print ("someError has occurred")

# --------------------------------------------------------------------------------OP-5---------------------------------------------------------------------------------------------
# Call in Class
# class SomeError(Exception):
#     pass

# try:
#     if '1' != 1:
#         raise SomeError("someError")
#     else:
#         print("someError has not occurred")
# except SomeError:
#     print("someError has occurred")

# --------------------------------------------------------------------------------OP-6---------------------------------------------------------------------------------------------
# def foo():
#     try:
#         print(1)
#     finally:
#         print(2)
# foo()

# --------------------------------------------------------------------------------OP-7--------------------------------------------------------------------------------------------
# def bar():
#     try:
#         print(3)
#         return 5
#     finally:
#         print(4)
#         return 6
# # Main
# result = bar()
# print(result)

# -------------------------------------------------------------------------------OP-8--------------------------------------------------------------------------------------------
# def baz():
#     try:
#         print(7)
#         raise ValueError("Error")
#     except ValueError as e:
#         print(e)
#         return 8
#     finally:
#         print(9)
# # Main
# result = baz()
# print(result)
# -------------------------------------------------------------------------------OP-9--------------------------------------------------------------------------------------------
# def nested_try():
#     try:
#         try:
#             print("A")
#             raise ValueError("B")
#         finally:
#             print("C")
#     except ValueError as ve:
#         print("D:", ve)
#     finally:
#         print("E")
# # Main
# nested_try()

# def multiple_except():
#     try:
#         value = int("abc")
#     except ValueError as ve:
#         print("ValueError:", ve)
#     except Exception as e:
#         print("Exception:", e)
#     finally:
#         print("Finally block")

# multiple_except()

