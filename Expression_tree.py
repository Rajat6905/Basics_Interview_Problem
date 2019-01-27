class ExpTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            
    def postorder(self,root):
         if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
            
def drawTree(exp):
    ope=['+','-','*','^','/']
    stack=[]
    for i in exp:
           if not i in ope:
               t=ExpTree(i)
               stack.append(t)
           else:
               t=ExpTree(i)
               t1=stack.pop()
               t2=stack.pop()
               
    
               t.left=t1
               t.right=t2
               stack.append(t)
    t=stack.pop()
    return t
    #A B * C D / +
    #A B C D / + *
postfix="ABCD/+*" 
r=drawTree(postfix)
r.inorder(r)

#r.postorder(r)#prefix
    #Infix
    
    
    
    
   



    





    
                







        