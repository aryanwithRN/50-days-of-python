# Data types 
# Typecasting - it show the type of the given data like int, 


# a=10
# b=20.1
# s=a+b
# print(s)
# print(type(s))


# we can add int in before input also / add before the calculation too. 
# aa = int(input("Enter No:"))
# bb = int (input("Enter No:"))
# eval()(Evaluate)- pre defined function based on users input
# aa = eval(input("Enter No:"))
# bb = eval(input("Enter No:"))
# g=int(aa)+int(bb)
# print (g)


# eval()(Evaluate)- pre defined function based on users input

# Write a program to take 2 input from the user and
# perform basic arithmatic opreations and print there respective result

rn = eval(input("Enter No:"))
aryan = eval(input("Enter No:"))
c=rn+aryan
d=rn-aryan
e=rn*aryan
f=rn/aryan

print("Your + value is",c)
print("Your - value is",d)
print("Your * value is",e)
print("Your / value is",f)


# --->
# %(mod)is print the reminder value
vv = 259948
hh = 100

x= vv% hh
print(x)

# --->

v = 99
h = 5

z= v% h
zz= v / h
zzz= v// h
print(z)
print(zz)
print(zzz)