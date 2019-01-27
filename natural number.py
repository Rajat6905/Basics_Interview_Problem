#First n Natural Number
#sum of all natural number


num=int(input("Enter a limit for natural number"))
sum_=0



if num>0:
   for i in range (1,num+1):
      print(i,end=",")
      sum_=sum_+i
else:
    print("please enter valid number")
    
print('\r')
print("sum of first {} natural number is {}".format(num,sum_))
