# 1)write a program to create a class by name Students,and initialize attributes like
# name,age and grade while creating an object

class Student:
    name:str
    age:int
    grade:str
    def get_student(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_student(self):
        print(f"Name: {self.name}, Age :{self.age}, Grade :{self.grade}")

obj = Student()
obj.get_student("Levin",25,"A+")
obj.display_student()


# 2. Write a program to create a child class Teacher that will inherit the properties of Parent class Staff

class Staff:
    def create_teacher(self,name,age,post,subject,):
        self.name=name
        self.age=age
        self.post=post
        self.subject=subject
class Teacher(Staff):
    def get_details(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("post:",self.post)
        print("Subject :",self.subject)

obj=Teacher()
obj.create_teacher("nithya",29,"guest lecturer","electronics")
obj.get_details()



# 3.Write a Python class Square, and define two methods that return the square area and perimeter.

class Square:
    side:int

    def __init__(self,side):
        self.side=side
    def square_area(self):
        print("area: ",self.side**2)
    def perimeter(self):
        print("perimeter: ",self.side*4)

obj=Square(3)
obj.square_area()
obj.perimeter()


# 4.define an account class with attributes ac no,ac name,balance.


class Account:
    accno:int
    acname:str
    balance:int

    def __init__(self,accno,accname,balance):
        self.accno=accno
        self.accname=accname
        self.balance=balance

obj=Account("123456","savings",10000)
print("Acc no: ",obj.accno)
print("Acc name: ",obj.accname)
print("Balance amount: ",obj.balance)



# 5.Create classes for a school management system. Have classes like Student, Teacher, and Course. Implement methods to enroll students, assign teachers, and display course details.


class Student:
    roll_no:int
    name:str
    age:int
    def __init__(self,roll_no,name,age):
        self.roll_no=roll_no
        self.name=name
        self.age=age
    def enroll(self):
        print("student details")
        print(f"roll_no :{self.roll_no} student name: {self.name} age :{self.age}")




class Teacher:
    def __init__(self,teacher_id,name,subject):
        self.teacher_id=teacher_id
        self.name=name
        self.subject=subject
    def assign_teachers(self):
        print("teacher details")
        print(f"Id : {self.teacher_id}  teacher name: {self.name}  subject :{self.subject}")

class Course:
    def __init__(self,course_name,course_duration,):
        self.course_duration=course_duration
        self.course_name=course_name

    def display_course_details(self):
        print("course details")
        print("course name:",self.course_name)
        print("course duration:",self.course_duration)



student1=Student(1,"vishnu",25)
student1.enroll()

teacher1=Teacher(11,"amruthra","chemistry")
teacher1.assign_teachers()

course1=Course("chemistry","2yr")
course1.display_course_details()




