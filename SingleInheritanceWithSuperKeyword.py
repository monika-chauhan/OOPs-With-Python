class Infosys:
    def __init__(self,unit):
        self.unit = unit 

class Employee(Infosys):
    def __init__(self,id,name,unit):
        self.id = id
        self.name = name 
        self.unit = unit
        super().__init__(unit)  

emp = Employee(101,'Moni','DNA')
print(emp.name)
print(emp.id)
print(emp.unit)