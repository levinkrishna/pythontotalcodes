fread=open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\fwritenumbers\\data.txt","r")
fwrite=open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\fwritenumbers\\leapyr.txt","w")

for line in fread:
    year=int(line.rstrip("\n"))

    if(year%100==0 and year%400==0):
        fwrite.write(str(year)+"\n")
    elif(year%100!=0 and year%4==0):
        fwrite.write(str(year)+"\n")
    print("process finished")
           