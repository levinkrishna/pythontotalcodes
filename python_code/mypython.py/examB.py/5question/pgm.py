from re import *
f1=open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\examB.py\\5question\\tyre.txt","r")
f2=open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\examB.py\\5question\\valid.txt","w")

validtyre_code=set()
rule="[0-9]{3}[\][0-9]{2}[\][a-z][0-9]{2}[\][0-9]{2}[k-y]{1}"
for id in f1:
    id=id.rstrip("\n")
    matcher=fullmatch(rule,id)
    if matcher!=None:
        validtyre_code.add(id)
# print(validtyre_code)

for val in validtyre_code:
    f2.write(val+"\n")





