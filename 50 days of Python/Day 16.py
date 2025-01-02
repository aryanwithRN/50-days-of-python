# WTP to take a list of n numbers check and print all the prime Numbers present number is in list

# user_input = int(input("Enter a Number: "))
# ls=[]

# for i in range (0, user_input):
#     x = int(input("Enter Numbers: "))
#     ls.append(x)

# c = 0
# for i in ls:
    
#     for j in range(2,i):
#         if i % j == 0:
#             c = 1
#             break
#     # print(i)
#     if c == 0:
#         print (i, "it a Prime Number")
        
#     else:
#         print("No prime Number Found")


# WTP to take a list of n numbers check and print all the Adams Numbers present number is in string

user_input = int(input("Enter a Number: "))
ls=[]

for i in range (0, user_input):
    x = int(input("Enter Number: "))
    ls.append(x)

for j in ls:
    sq = j ** 2
    n1 = j
    rev = 0 
    while n1:
        rev = rev * 10+(n1 % 10)
        n1 = n1 //10
    revsq = str (rev**2)
    if revsq[::-1]==str(sq):
        print(j, "It is an Admas Number") 
    else:
        print(j, "Not an Adam Numbers")           







# WTP to take n words in a list and swap first 2 characters of the first word with the first 2 charcter of last word similarly 
# replace first 2 charecter of seccond word with first 2 charector of second last 2 words/

# user_input = int(input("Enter Number of dtring you want: "))
# ls= []

# for i in range (0, user_input):
#     x = input ("Enter words:")
#     ls.append(x)
# print(ls)
# for i in range(0,user_input//2):
#     j = user_input - i -1 
#     s1 = ls [i][:2]
#     s2 = ls [j][:2]
#     ls[i] = s2 +ls[i][2:]
#     ls[j] = s1 + ls[j ][2:]
            

# print(ls)


# WTP to take a list of words which contains alphabets and numerics ,create a new list with only numeric
# part of the words and join all the words from the string and form a new string . 

# user_input =int(input("Enter a length of list: "))
# ls = []
# for i in range (0,user_input):
#     x = input("Enter inputs (Words + Num. ): ")
#     ls.append(x)
# str1 = ""
# ls1 = []
# for i in ls:
#     digit = ""
#     for j in i:
#         if j.isdigit():
#             digit = digit + j  
#         else:
#            str1 = str1 + j
#     ls1.append(digit)  
# print("Lits Is", ls1)
# print("String is ", str1 )    


# Write a Python program to generate and print a list of the first and last 5 elements where the values are 
# square numbers between 1 and 30 (both included).

# l1 = [ ]
# for i in range (1,31):
#     x = i ** 2 
#     l1.append(x)
# l2= []
# l2 = l1 [:5]
# print (l2)
# # Extend use for continue the list with the existing list
# l2.extend(l1[-5:])
# print(l2)



# Write a Python function that takes two lists and returns True if they have at least one common member.
# user_input= int(input("Enter Numbers of lists: "))
# ls=[]
# ls1=[]
# for i in range (0,user_input):
#     x = int(input("List First:  "))
#     ls.append(x)
#     y  = int(input ("List Second:"))
#     ls1.append(y)

# for i in ls:
#     for j in ls1:
#         if i == j:
#             print("True")
