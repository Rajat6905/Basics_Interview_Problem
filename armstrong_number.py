#Armstrong Number
num=int(input("enter any number"))
fnumber=num
sum_=0
reverse=0
while num>0:
    rem=num%10
    num=num//10
    reverse=(reverse*10)+rem
    sum_=sum_+1
  
arm_sum=0
while reverse>0:
    res=1
    remainder=reverse%10
    reverse=reverse//10
    for i in range(1,sum_+1):
        res=remainder*res
    arm_sum=res+arm_sum
   

if(fnumber==arm_sum):
    print("Given number is armstrong")
else:
   print("not an armstrong number")
   


    
    

    
