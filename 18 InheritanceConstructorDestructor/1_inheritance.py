class company:
    def __init__(self) :
        print("in constructor")
        self.x=10
        self.y=20
        
    def fun(self):
        print("in fun")
        print(self.x)
        print(self.y)

class employee(company):
    def printData(self):
        print("print data employee")

obj=employee()
obj.fun()
obj.printData()