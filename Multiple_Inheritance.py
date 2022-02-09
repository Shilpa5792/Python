class Employee:
    def getEmp(self):
        self.id = input("Enter Employee Id: ")
        self.name = input("Enter Name: ")


class Department():
    def getDept(self):
        self.DeptName = input("Enter Department Name: ")
        self.Designation = input("Enter Designation: ")


class Admin(Department, Employee):

    def display(self):
        super().getEmp()
        super().getDept()

        print("\n\n ============Employee Details=============\n")

        print("Id is: ", self.id)
        print("Name is: ", self .name)
        print("Department is: ", self.DeptName)
        print("Designation is: ", self.Designation)



A = Admin()
A.display()