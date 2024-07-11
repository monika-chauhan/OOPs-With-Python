class Employee:
    # __init__ method is called constructor in python 
    # passing the self keyword as the first parament to connect the constructor with class 
    # constirctor 1:
    def __init__(self,emp_id,emp_name,emp_unit,emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_unit = emp_unit 
        self.emp_age = emp_age 

    # constructor 2:
    # Constructor overloading 
    def __init__(self,emp_id,emp_name,emp_unit,emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name

# We can create Multiple Constructor but It will be using the last constructor
# Here it will be using the seocnd constructor   