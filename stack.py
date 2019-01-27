class stack:
    def __init__(self):
        self.st=[]
        
    def push(self,data):
        return self.st.append(data)
    
    def show(self):
        if len(self.st)>0:
            return print(self.st)
        else:
            return print("Stack is empty")


    def pop(self):
        if len(self.st)>0:
            return self.st.pop()
        else:
            return print("Stack is empty")
    def size(self):
        return len(self.st)
    
    def peek(self):
        if len(self.st)>0:
            return self.st[len(self.st)-1]
        else:
            return ("Stack is empty")
      
        

obj=stack()
obj.push(10)
obj.show()

obj.show()
print(obj.size())
print(obj.peek())
