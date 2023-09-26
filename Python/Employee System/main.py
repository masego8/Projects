#Employee System

class Admin:
    def __init__(self, maxWorkers):
        self.maxWorkers = maxWorkers
        self.employees = []

    def addStaff(self, employee):
        if len(self.employees) < self.maxWorkers:
            self.employees.append(employee)
            

    def removeStaff(self, employee):
        if len(self.employees) > 2:
            print("Not enough staff!")
        else:
            self.employees.remove(employee)
            print(employee.name, "has left our team")
    
    def showStaff(self):
        for i in range(len(self.employees)):
            print(self.employees[i].name)

class Staff:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Managers(Staff):
    def __init__(self, name, age):
        super().__init__( name, age)

class Crew(Staff):
    def __init__(self, name, age):
        super().__init__(name, age)


#list of employees
e1 = Staff("masego", 22)
e2 = Staff("Jack", 20)
e3 = Staff("Emma", 24)
e4 = Staff("Lily", 18)
e5 = Staff("Ash", 26)


#FUNCTIONS

#hire new staff
def newStaff():
    #members = Admin(5)
    #members.addStaff(e1)
    print("NEw Hires")
   

#staff leaving 
def staffLeave():
    #members = Admin(5)
    #members.removeStaff(e2)
    print("this is who is leaving")

#show all employees
def showRota(Admin):
    members = Admin(5)
    members.showStaff()



