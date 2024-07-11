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
print(isinstance(emp,Employee))
print(isinstance(emp,Infosys)) # return True if we pass this class into Employee class line number 5 
# If we remove Infosys from Employee class it will give False 
