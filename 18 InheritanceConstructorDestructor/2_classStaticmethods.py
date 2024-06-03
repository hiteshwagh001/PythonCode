class demo:
    def __init__(self):
        print("in constructor")

    def simple(self):
        print("in parent simple")

    @classmethod
    def classm(cls):
        print("In class parent")

    @staticmethod
    def classstatic():
        print("class static")

class child(demo):
    pass

obj = child()
obj.classm()
obj.simple()
# obj.classstatic()  
p=child.classstatic()


