class Demo:
    print("In Demo class\n")

    def __init__(self) -> None:
        print("In Demo Constructor")

    def fun(self):
        print("In fun Instance method")

    @staticmethod
    def gun():
        print("In static method")

    @classmethod
    def run(self):
        print("In the class methods")


obj=Demo()
obj.fun()
obj.gun()       #static method called by obj
Demo.gun()       #static method called by class Name
Demo.run()      # class method by class name
obj.run()      # class method by class name

# obj1=Demo()