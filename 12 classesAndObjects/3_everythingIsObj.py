class demo:
    def __init__(self,x,y) -> None:
        print("I'm constructor") 
        self.x=x
        self.y=y
        print(id(self.x))       #2841501893136
        
    def fun(self):
        print("In the fun")
        
    def fun(self,x):
        print(x)
        print("in the sencond fun")

obj=demo(10,20)
obj.fun(10)
z=10
print(id(z))        #2841501893136