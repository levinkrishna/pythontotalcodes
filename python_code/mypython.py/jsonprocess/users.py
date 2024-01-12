from json import load
with open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\jsonprocess\\data.json","r")as f:
  data=load(f)
names=[u.get("name") for u in data]
# # print(names)   
candidate=max(data,key=lambda s:s.get("total"))
print(candidate)      

#sort all students wrt total order by desc
# out=sorted(data,reverse=True,key=lambda s:s.get("total"))
# print(out)

#print bca students

# bca_students=[u.get("name")for u in data if u.get("course")=="bca"]
# print(bca_students)