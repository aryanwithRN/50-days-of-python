# Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal to the other number. 
# For example 220 and 284 are amicable numbers. Proper divisors of a number are those numbers by which the number is divisible, 
# except the number itself.


# def ambicable(n):
#     sum = 0
#     for i in range(1,n):
#         if n % i == 0:
#             sum+=i
#     return sum

# input1,input2 = 220, 284
# if ambicable(input1) ==  input2 and ambicable(input2) == input1:
#     print("Amicable number")
# else:
#     print("Not amicable numbers")


# Write a function to print twin primes less than 1000. If two consecutive odd numbers are both prime then they 
# are known as twin primes

# check_prime = lambda n : "prime" if  n > 1 and all(n%i != 0 for i in range (2,n)) else "Not prime"

# def twin_prime():
#     for i in range(2,1000):
#         if check_prime(i) == "prime":
#             if check_prime(i+2) == "prime":
#                 print(i, i+2)

# twin_prime()

# Write a function to find out the prime factors of a number. Example: prime factors of 56 - 2,  7

check_prime = lambda n : "prime" if  n > 1 and all(n%i != 0 for i in range (2,n)) else "Not prime"
def prime_factor(n):
    for i in range(1,n):
        if n % i == 0 and check_prime(i)== "prime":
            print(i, end =" ")
n  = 56 
prime_factor(n)