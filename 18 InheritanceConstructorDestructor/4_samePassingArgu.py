class parent(object):
    z=10
    def __init__(self):
        print("\nin parent constructor")
        self.x=10
        self.y=20
        
    def m1(self):
        print("\nin m1 parent class")


class child(parent):
    z=1
    print("\nvalue of z : ",parent.z)
    print("\nvalue of z : ",z)
    
    def __init__(self):
        print("\nin child constructor called")
        print("value of z in parent by super() : ",super().z)
        self.x=30
        self.y=40
        self.z=32
        
    def c1(self):
        print("\nin child  class")
        print(self.x)
        print(self.y)
        super().__init__();
        print(self.x)
        print(self.y)


obj=child()
obj.c1()