class Employee:
    def __init__(self,ID=None,Salary=None,Department=None):
        super().__init__()
        self.ID = ID
        self.Salary = Salary
        self.Department = Department

    def tax(self):
        return self.Salary*0.2

    def salaryPerDay(self):
        return (self.Salary/30)

    def displayInfo(self):
        print("ID" + str(self.ID))
        print("Department: " + self.Department)
        print("Salary: " + str(self.Salary))
        print("Tax: " + str(self.tax()))
        print("Salary per Day: " + str(self.salaryPerDay().__round__(2)))

    def overloadIt(self,a=None,b=None,c=None):
        print(a,b,c)

Steve = Employee(25,25000,"Data Science")
Steve.displayInfo()
Steve.overloadIt()
Steve.overloadIt("Adnan")
Steve.overloadIt("Adnan","Şenses")