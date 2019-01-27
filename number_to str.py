#number to String...........

num=123456789
reverse=0
dict1={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
while num>0:
    rem=num%10
    reverse=(reverse*10)+rem
    num=num//10
while reverse>0:
   remainder=reverse%10
   reverse=reverse//10
   print(dict1[remainder],end=' ')
   