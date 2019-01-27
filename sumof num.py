#sum of all numbers
num=int(input("enter number"))


sum_=0
while num>0:
    rem=num%10
    num=num//10
    sum_=sum_+rem
    
print(sum_)
