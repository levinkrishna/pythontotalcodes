from re import *
f=open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\vehicles\\data.txt","r")
# for line in f:
#     print(line)
kerala_nums=set()
tn_nums=set()
tn_rule="[T][N]-[0-9]{1,2}-[A-Z]{2}-[0-9]{4}"
kl_rule="[K][L]-[0-9]{1,2}-[A-Z]{2}-[0-9]{4}"
for line in f:
    veh_num=line.rstrip("\n")
    tmatcher=fullmatch(tn_rule,veh_num)
    if tmatcher!=None:
        tn_nums.add(veh_num)
    kmatcher=fullmatch(kl_rule,veh_num)
    if kmatcher!=None:
        kerala_nums.add(veh_num)
print("tamil_nadu_numbers",tn_nums)
print("kerala_nums",kerala_nums)