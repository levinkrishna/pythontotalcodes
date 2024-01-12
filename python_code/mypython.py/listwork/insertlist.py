#list=[2,3,4,5]
#list.append(6)
#print(list)

#insert is used to add  to a particular position in a value

#list.insert(0,1)  #listname.(position of list,value to be added)
#print(list)


#emplist=[]
#print(emplist)

#get size of list from user,and get each element of a list from user,then add to the list

#emplst=[]
#length=int(input("enter the size of list: "))
#for i in range(0,length):
  #  num=int(input(f"enter{i}th position element :"))
 #   emplst.append(num)
#print(emplst)


#create an empty list and access all the elements

#add new element to the 2nd positionof list-which should be the max of list added by 10
#emplst=[]
#length=int(input("enter the size of list: "))
#for i in range(0,length):
 #   num=int(input(f"enter{i}th position element :"))
 #   emplst.append(num)
#maxim=max(emplst)
#emplst.insert(2,maxim+10)
#print(emplst)


#create a list of student name,then check for a particular name in list given by
#the user if name is present the change that name to anamikaif that paricular position
#name is not present insert amal to lst position



students_name=[]
length=int(input("enter the size of list:"))
for i in range(length):
    name=input(f"enter{i}th name:")
    students_name.append(name)
check_name=input("enter a name:")
for s in range(length):
    if(students_name[s]==check_name):
        students_name[s]="anamika"
        break
    elif(s==(length-1)):
        students_name.insert(1,"amal")
print(students_name)

#ip=abca op=amal b c amal

stud_name=["a","b","c","a"]
flag=0
ch_name=input("enter the name:")
for i in range(len(stud_name)):
    if (ch_name==stud_name[i]):
        stud_name[i]="amal"
        flag=1
if(flag==0):
    stud_name.insert(1,"amal")
print(stud_name)