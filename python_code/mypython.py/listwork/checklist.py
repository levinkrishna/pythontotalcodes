element=int(input("enter the value for element:"))
list=[1,2,3,4]
for n in list:
    if element in list:
        print("element found")
        break
    else:
        print("element not found")
        break