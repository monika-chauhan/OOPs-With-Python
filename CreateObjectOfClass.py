class Employee:
    def __init__(self,emp_id,emp_name,emp_unit,emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_unit = emp_unit 
        self.emp_age = emp_age 

# creating the object of the class by giving the name as emp and passing 
# the parameter of constructor 
emp = Employee(101,'Monika chauhan','DNA',24)
print(emp) #It will return the object 
print(emp.emp_name) #calling the parameter with object name as emp.emp_name 


# output: 
# <__main__.Employee object at 0x000002956F74AEA0>
#Monika chauhan