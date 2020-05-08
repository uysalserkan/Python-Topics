class Employee:
    ID = None
    Salary = None
    Department = None
    def __init__(self,par_id=0,par_sal=0,par_dept=None):
        super().__init__()
        self.ID = par_id
        self.Salary=par_sal
        self.Department = par_dept

    def displayInfo(self):
        print("Department: " + self.Department + "\n" +"ID: " +str(self.ID) + "\n" +"Salary: "+ str(self.Salary))

    

def main():
    Steve = Employee()
    Mark = Employee(8,5000,"Standart Human")
    Steve.Department = "Computer Engineering"
    Steve.ID = 25
    Steve.Salary = 8000
    Steve.displayInfo()
    Steve.Lastname = "NoneFound404" #! This notation is outside propert, and only avaible for Steve object.
    print(Steve.Lastname)

    Mark.displayInfo()
    
if __name__ == "__main__":
    main()