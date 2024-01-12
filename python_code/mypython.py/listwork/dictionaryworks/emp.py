employee={"id":100,"name":"vijay","department":"hr","salary":250000}

#create a funtion for returning employee name

"""def get_name(emp):
    return emp.get("name")
print(get_name(employee))"""

get_name=lambda emp:emp.get("name")
print(get_name(employee))

#create a lambda function for return employee salary

get_salary=lambda emp:emp.get("salary")
print(get_salary(employee))


# *args positional argument takes any number of parameters type tuple
"""def addition(*args):
    return sum(args)
print(addition(10,))
print(addition(10,20))
print(addition(10,20,30))"""

#lambda function

"""addition=lambda *args:sum(args)
print(addition(10,))
print(addition(10,20))
print(addition(10,20,30))"""




max_nums=lambda *args:max(args)
print(max_nums(10,2,3,4,50))





