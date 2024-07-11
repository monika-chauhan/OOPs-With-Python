class Student:
    def __init__(self,id,name,age):
        self.id = id 
        self.name = name 
        self.age = age 
    
stu = Student(101,'Monika',24)

# Build In Class Function 

print(getattr(stu,'name'))
print(getattr(stu,'age'))
print(getattr(stu,'id'))

print(setattr(stu,"age",25))
print(setattr(stu,"name",'shubham'))

print(getattr(stu,'name'))
print(getattr(stu,'age'))

print(hasattr(stu,'id'))
# print(delattr(stu,'age'))
# print(getattr(stu,'age'))


# Built-In class Attribute
print(stu.__doc__)
print(stu.__dict__)
print(stu.__module__)
    
