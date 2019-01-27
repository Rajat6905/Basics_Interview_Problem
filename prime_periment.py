
lis=[]
for num in range(2,90):
    for j in range(2,int(num**0.5)+1):
        if (num%j)==0:
            break
    else:
        lis.append(num)
k=0
n=7
sp=n
for i in range(1,n+1):
    for j in range(1,sp):
      print(" ",end='')
    sp=sp-1
    for val in range(1,i):
        print(str(lis[k])+" ",end='')
        k=k+1
    print('\r')
    

#k=0
#n=7
#sp=n
#for i in range(1,n+1):
#    for j in range(1,sp):
#      print(" ",end='')
#    sp=sp-1
#    for val in range(1,i):
#        k=k+1
#        #print(str(k)+" ",end='')
#        for kk in range(2,k):
#                if (k%kk)==0:
#                    break
#        else:
#            print(str(k)+' ',end='')
#    print('\r')
#        