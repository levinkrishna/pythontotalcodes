years=[2000,2024,1991,1995,1200,1400,1234]
f=open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\leapyr\\data.txt","w")
for y in years:
    if y%100==0 and y%400==0:
        f.write(str(y)+"\n")
    elif y%100!=0 and y%4==0:
        f.write(str(y)+"\n")



