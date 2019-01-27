class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
   
    def preorder(self,root):
        #root-left-right
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def finddepth(self,root):
        if root==None:
            return 0
        if self.left==None and self.right==None:
            return 1
        if self.left==None:
            return self.finddepth(root.right)+1
        if self.right==None:
            return self.finddepth(root.left)+1
        return max(self.finddepth(root.left),self.finddepth(root.right))+1
    


#root = Node(1) 
#root.left=Node(2)
#root.right=Node(3)
        
root = Node(1) 
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.right.left=Node(7)
root.right.left.right=Node(8)
#root.right.left.right.right=Node(9)
#root.right.left.right.right.right=Node(10)
#root.right.left.right.right.right.right=Node(11)

print("depth of Tree :-"+str(root.finddepth(root)))



