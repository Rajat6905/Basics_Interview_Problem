class Q:
    def __init__(self):
        self.queue=[]
        
    def enqu(self,data):
        return self.queue.insert(0,data)
    
    def deq(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return print("Queue Empty")
    def show(self):
        if len(self.queue)>0:
            return print(self.queue)
        else:
            return print("Queue Empty")
    
    
    
    
obj=Q()
obj.show()
obj.enqu(10)
obj.enqu(20)
obj.enqu(30)
obj.enqu(40)
obj.show()
obj.deq()
obj.deq()
obj.show()


