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
                    
    def printvalues(self):
        #inorder
        if self.left:
            self.left.printvalues()
        if self.right:
            self.right.printvalues()
        print(self.data)
    
#Inorder Traversal      
    def inorder(self,root):
        #left-root-right
       if root:
           self.inorder(root.left)
           print(root.data)
           self.inorder(root.right)
#Pre-order Traversal   
    def preorder(self,root):
        #root-left-right
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
#Post-order Traversal
    def postorder(self,root):
        #left-right-root
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
#Traversal using BFS or Level order Traversal 
    def levelordertraversal(self,queue):
        if len(queue)==0:
            return
        node=queue[0]
        queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print(node.data)
        self.levelordertraversal(queue)
        
#Search Using DFS
    def dfs(self,root,key=22):
        if root:
            self.dfs(root.left)
            self.dfs(root.right)
            if root.data==key:
                return print("sucess")
#Search Using BFS
    def bfs_search(self,root,key):
        if root is None or root.data==key:
            return root
        if root.data<key:
            return self.bfs_search(root.right,key)
        if root.data>key:
            return self.bfs_search(root.left,key)
        
        
    
            
            
queue=[]
root = Node(15)
queue.append(root)
root.insert(22)
root.insert(3)
root.insert(14)
root.insert(2)
#root.dfs(root)
#if root.bfs_search(root,22):
#    print("sucess")
#else:
#    print("failed")
#
#root.left = Node(3)
#root.right = Node(22)
#root.left.left = Node(2)
#root.left.right = Node(14)


#root.printvalues()
#root.inorder(root)
#root.preorder(root)
#root.postorder(root)s
root.levelordertraversal(queue)



