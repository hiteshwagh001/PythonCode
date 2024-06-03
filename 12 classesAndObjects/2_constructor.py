class school:
    def __new__(cls,x,y) :
        print("in new")
        # return super().__new__(cls)
        print(cls)
        return object.__new__(cls)
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(self)
        print(self.x)
        print(self.x)
        print("constructor ")
        
        
obj=school(10,20)
print(obj)
