#methods inside dictionary
student={"roll":1234,"name":"hari","age":25,"course":"mca"}
print(student.values())

print(student.keys())


for k,v in student.items():
    print(k,v)
#get(key) fetching value wrt key

print(student.get("name"))



#pop(key)

student.pop("course")
print(student)