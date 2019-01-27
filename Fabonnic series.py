#Fabonnic series
num=int(input("Enter number"))
first=0
second=1
count=0
print(first)
print(second)
while count<num-2:
    third=first+second
    first=second
    second=third
    count+=1
    print(third)
    
