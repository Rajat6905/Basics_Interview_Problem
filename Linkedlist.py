class Node:
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,next_new):
        self.next_node=next_new
        
class LinkedLsit:
    def __init__(self,head=None):
        self.head=head
        
    def insert(self,data):
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node
        
    def printlist(self):
        temp=self.head
        count=0
        while temp:
            count +=1
            print(temp.get_data(),end=',')
            temp=temp.get_next()
        return print("size:-"+str(count))
           
    def search(self,ele):
        h=self.head
        found=False
        while h and found is False:
            if h.get_data()==ele:
                found=True
                return True
            else:
                h=h.get_next()
        return False
        
        
        
if __name__=="__main__":
    obj=LinkedLsit()
    obj.insert(10)
    obj.insert(23)
    obj.insert(33)
    obj.insert(66)
    obj.printlist()
    
    if obj.search(66):
        print("found")
    else:
        print("Data not in the list")
    
    
    
    


        
        
