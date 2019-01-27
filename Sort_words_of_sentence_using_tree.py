words="Hello this Is an Example With cased letters"
words=words.lower().split()
asc=[]
asc = [[ord(ch) for ch in word] for word in words]
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
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
            self.inorder(root.left)
            for i in root.data:
                a.append(i)
            s=" "
            for cc in a:
                s=s+chr(cc)
            print(s)
            self.inorder(root.right)
root=Node([]) 
for kk in asc:
    root.insert(kk)
root.inorder(root)














