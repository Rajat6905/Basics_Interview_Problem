#first n even or odd number

even=[]
odd=[]
for i in range(1,101):
    if (i%2)==0:
        even.append(i)
    else:
        odd.append(i)
    
print(even)
print(odd)