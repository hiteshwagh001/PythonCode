class Human:
    def __init__(self,name,age):
        print("In Demo constructor")
        self.name=name
        self.age=age
        
    def information(self):
        print('Name is : ',self.name)
        print('Age is : ',self.age)
        
name=input("enter your name")
age=int(input("enter your age"))

if __name__=='__main__':
    obj1=Human(name,age)
    obj1.information()
