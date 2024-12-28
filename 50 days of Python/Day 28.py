# Fn-
def check_prime(x):
    flag=0
    for i in range(2,x):
        if x % i == 0:
            flag=1
            break
    if flag == 0:
        return("prime")
    else:
        return(f"{x} is Not Prime")
# main
t1 = ()
n = 200
for i in range(2,n+1):
    # res = check_prime(i)
    if check_prime(i) == check_prime(i + 2):
        tuple = (i,i+2)
        print(tuple)
    # print(res)
    # if res == 'prime':
    #     res1 = check_prime(i+2)
    #     if res == res1:
            


