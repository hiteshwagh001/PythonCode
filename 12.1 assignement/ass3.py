class parent:
    
    @classmethod
    def classmethod(self):
        print("parent class method")

    @staticmethod
    def staticmethod():
        print("parent static method")

    def instancemethod(self):
        print("parent instance method")

class child(parent):
    pass

obj=child()
obj.classmethod()
obj.staticmethod()
obj.instancemethod()