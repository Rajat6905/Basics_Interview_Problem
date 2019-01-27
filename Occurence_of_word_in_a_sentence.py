#Occurence of each world and sort words alphabetically

words="Hello hello this Is an Example With cased letters"
words=words.lower().split()

count={}
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

asc=[]
asc = [[ord(ch) for ch in word] for word in words]


class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        self.freq=1
        

        
    def insert(self,data):
        
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data      
      
    def inorder(self,root):
        a=[]
        if root:
#            count={}
            self.inorder(root.left)
            for i in root.data:
                a.append(i)
            s=" "
            for cc in a:
                s=s+chr(cc)
            print(s)
#            if s in count:
#                count[s]+=1
#            else:
#                count[s]=1
#            print(count)
            self.inorder(root.right)
root=Node([]) 
for kk in asc:
    root.insert(kk)
root.inorder(root)
















