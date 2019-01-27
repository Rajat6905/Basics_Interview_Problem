n=4
k=n

for i in range(0,n+1):
    for sp in range(0,k):
        print(" ",end="")
    for star in range(0,i):
        print("* ",end="")
    k=k-1
    print('\r')  
    #if i==n and k==-1:
        
k=n
for i in range(0,n):
    for sp in range(0,i):
        print(" ",end="")
    for star in range(0,k):
        print("* ",end="")
    k=k-1
    
    print('\r') 