class Employee:
    def __init__(self,emp_id,emp_name,emp_unit,emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_unit = emp_unit 
        self.emp_age = emp_age 

    # this the static method wr are passing the f string in print statement
    def Greet_Message(self):
        print(f"Hello {self.emp_name}. I am from {self.emp_unit} unit")

# creating the object of the class by giving the name as emp and passing 
# the parameter of constructor 
emp = Employee(101,'Monika chauhan','DNA',24)
emp1 = Employee(102,'Shubham chauhan','DNA',24) # Create multiple object with same class 
emp.Greet_Message() # calling the method using object name emp
emp1.Greet_Message() # calling the different object


# output: 
#Hello Monika chauhan. I am from DNA unit
#Hello Shubham chauhan. I am from DNA unit