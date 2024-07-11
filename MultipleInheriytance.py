class Infy:
    def __init__(self,unit,job_designation):
        self.uni = unit 
        self.Job_designation = job_designation 

class CG:
    def __init__(self,job_level):
        self.job_level = job_level

class Employee(Infy,CG):
    def __init__(self,id,name,unit,job_design,job_level):
        self.id = id 
        self.name = name 
        self.unit = unit 
        self.job_design = job_design 
        self.job_level = job_level
        #super().__init__(job_level) # Its giving Error Beacuse We provide the Infy class first then CG but passing 
        # parameter for CG class 
        super().__init__(unit,job_design)
    
    def display(self):
        return f"""Employee Details :
                    Employee Id : {self.id}
                    Employee Name: {self.name}
                    Employee Unit : {self.unit}
                    Employee Job Designation : {self.job_design}
                    Employee Job Level : {self.job_level}
                    """

emp = Employee(101,'Monika','DNA','Senior System Engineer','JL3')
print(emp.display())