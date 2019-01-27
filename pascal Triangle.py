#Pascal triangle
n=5
sp=n
pasc=1
l=[]
for i in range(0,n+1):
    for j in range(0,sp+1):
        print(" ",end='')
    sp=sp-1
    for val in range(0,i+1):
        if(val==0):
            pasc=1
        else:
            pasc=pasc*(i-val+1)//val
        
        print(str(pasc)+' ',end='')
    print('\r')
    
    
    
    