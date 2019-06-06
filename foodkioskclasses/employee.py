class Employee():
    def __init__(self, empID, empName, empTitle):
        self.empID = empID
        self.empName = empName
        self.empTitle = empTitle

    def getEmpID(self):
        return self.empID

    def getEmpName(self):
        return self.empName

    def getempTitle(self):
        return self.empTitle

    def __str__(self):
        return self.empID + "," + self.empName