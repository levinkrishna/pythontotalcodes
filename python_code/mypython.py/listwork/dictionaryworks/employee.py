#{key:value,key:value..........,key:value}

emp={"id":100,"name":"levin","desig":"executive","salary":20000}
print(emp)
#print emp name
print(emp["name"])

#print salary
print(emp["salary"])

for key in emp:
    print(key, emp[key])
    

#adding new key value pair
emp["gender"]="male"
print(emp)

#updating a value
#dictname["key"]=value

emp["salary"]=27000
print(emp["salary"])
#update employee salary with current salary+2000
emp["salary"]+=2000
print(emp["salary"])

#check existance of a key
#key in dictionary
if("name" in emp):
    print("present")
else:
    print("notpresent")
