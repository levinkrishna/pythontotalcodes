# class Student:
#     rolno:int
#     name:str
#     course:str

#     def add_student(self,rol,name,course):
#         self.rolno=rol
#         self.name=name
#         self.course=course

#     def get_student(self):
#         print(self.rolno,self.name,self.course)


class Student:
    rolno:int
    name:str
    course:str

    def __init__(self,rol,name,course):
        # INITIALISING INSTANCW VAIABLE =>CONSTRUCTOR
        self.rolno=rol
        self.name=name
        self.course=course

    def get_student(self):
        print(self.rolno,self.name,self.course)
        
obj=Student(1000,"hari","django")
obj.get_student()

obj2=Student(1001,"ravi","mearn")
obj2.get_student()