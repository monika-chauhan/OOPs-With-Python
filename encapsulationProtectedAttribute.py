# Protected members can be accessed within the class and its subclasses. 
# You can designate a member as protected by prefixing its name with an underscore (_).
class Employee:
    def __init__(self,id,name,salary):
        self._id = id 
        self._name = name 
        self._salary = salary 

    def get_name(self):
        return self._name 

    def get_salary(self):
        return self._salary
    
    def set_salary(self,new_salary):
        self._salary = new_salary 

emp = Employee(101,'Monika',5000)
print(emp.get_name())
emp.set_salary(1000)
print(emp.get_salary())