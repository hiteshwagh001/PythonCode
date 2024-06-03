class Employee:
    compName="FaceBook"     # this is the class varible that can be access by using object or by the name of the class

    def __init__(self,empId,empName) :
        self.empId=empId            # this are the instance variables that can access by using only obj
        self.empName=empName
        print("Instance variables are assigned")

    def empInfo(self):
        print(self.empId)
        print(self.empName)

emp1=Employee(10,"Aakash")
emp2=Employee(12,"Sanket")

emp1.empInfo()
emp2.empInfo()

print("\nclass varible")
print(Employee.compName)
print(emp1.compName)