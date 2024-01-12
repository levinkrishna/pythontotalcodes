from abc import ABC,abstractmethod

class Employee(ABC):
    name=str
    salary=str
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @abstractmethod    
    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_salary(self):
        return self.salary+25000
    
class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_salary(self):
        return self.salary+10000
obj=Developer("hari",24000)
print(obj.calculate_salary())
        