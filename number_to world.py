#number to world
num=int(input("ENTER ANY NUMBER:"))

reverse=0
length=0

lis=[]
dict1={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
dict2={0:" ",1:" ",2:"Twenty",3:"Thirty",4:"Fouty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninty"}

while num>0:
    rem=num%10
    reverse=(reverse*10)+rem
    num=num//10
    length=length+1
   

re=0
while reverse>0:
   remainder=reverse%10
   re=(re*10)+remainder
   reverse=reverse//10
   lis.append(remainder)   
if length==3:
    print(dict1[lis[0]]+" Hundred "+dict2[lis[1]]+" "+dict1[lis[2]])
elif length==2:
    print(dict2[lis[0]]+" "+dict1[lis[1]])

