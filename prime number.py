#prime number
import math
num=int(input("Enter a Number"))

if num<1:
    print("Please enter valid number")
else:
    for j in range(2,num):
       if(num%j)==0:
          print("non prime")
          break
    else:
       print("prime")




    
    
