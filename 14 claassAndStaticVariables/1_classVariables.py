class Employee:
    compName="Meta"

    def __init__(self):
        self.id=12
        self.name="Sanjay"
        print("\nInstance variables are assigned ")

    def info(self):
        print("\nEmployee Data: ")
        print(self.compName)
        print(self.id)
        print(self.name)
        Employee.compName="FaceBook"
        print(Employee.compName)

emp1=Employee()
emp1.info()
emp1.compName="Twitter"
print(emp1.compName)

emp2=Employee()
emp2.info()