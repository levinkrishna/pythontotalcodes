f=open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\user\\data.txt","r")
users=[]
for line in f:
    text=line.rstrip("\n")
    name,followers,followings=text.split(",")
    print(name,followers,followings)
   