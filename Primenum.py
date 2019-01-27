
#prime number in a given range
import math
lower=int(input("enter first number"))
upper=int(input("enter last number"))

for num in range(lower,upper):
    for j in range(2,num//2+1):
        if (num%j)==0:
            break
    else:
        print(num)
    
