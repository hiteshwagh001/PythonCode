class parent():
    def __init__(self):
        self.name="Munna bhai"
        self.age="21"
        print("parent constructor")

    def home(self,add):
        self.add=add
        
        
class child(parent):
    
    def __init__(self,name,age):
        print("child constructor")
        self.name=name
        self.age=age
        print("parent constructor")

    def home(self,add):
        self.add=add
        
    def printdata(self):
        print("\nDetails of person \n")
        print(self.name)
        print(self.age)
        print(self.add)
        
obj=child("Hero",21)
obj.home("Pune")
obj.printdata()
obj.printdata()
