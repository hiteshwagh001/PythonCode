#private access specifiers can access in only same class 

class parent:
    x=10
    
    def __init__(self):
        print("parent constructor \n")
        self._y=20   #this is the protected
        self.__z=30  #this is the private
        
    def printData(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        
class child(parent):
    a=45
    def __init__(self):
        super().__init__()
        print("in child constructor")
    
    def printData(self):
        # super().printData()
        print("x : ",self.x)
        print("_y : ",self._y)
        print("__z : ",self._parent__z)         # acess the private key in child class by changing the name of the variable
        # print("__z : ",self.__z)
        
print(dir(child))
obj= child()
obj.printData()
print(obj.x)
print(obj._y)
print("Access by key :",obj._parent__z)
# print(obj.__z)  # private can not access outside the class with the same name   It throws AttributeError

print()

print(dir(child))
print(dir(obj))