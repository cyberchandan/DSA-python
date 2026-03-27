class stack:
    def __init__(self):
        self.list=[]
    def push(self,num):
        self.list.append(num)    

    def is_empty(self):
        if(len(self.list)==0):
            return True
        else :
            return False    
    def pop(self):
        if not self.is_empty():
           return self.list.pop()
        
    def peek(self):
        return self.list[len(self.list)-1]   


s=stack()        
s.push(45)   
s.push(50)
s.push(65)
s.push(67)

# print(s.pop())

# s.pop()
# s.pop()
# print(s.peek())
# print(s.is_empty())
        

        


    