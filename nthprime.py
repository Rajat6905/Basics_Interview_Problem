#print nth prime number

inp=int(input("enter position of number"))
prime=[]
for num in range(1,1000):
    for j in range(2,num):
        if (num%j)==0:
            break
    else:
        prime.append(num)
print(prime[inp-1])
    
        
