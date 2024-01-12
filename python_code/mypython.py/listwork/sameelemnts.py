
# lst1=[10,14,15,20,21]
# lst2=[8,9,20,21,22]
# for n1 in lst1:
#     for n2 in lst2:
#         if(n1==n2):
#           print(n1)
        

    #by using algorithm

lst1=[10,14,15,20,21]
lst2=[8,9,20,21,22]
p1=0
p2=0
while(p1<len(lst1)and p2<len(lst2)):
    if(lst1[p1]==lst2[p2]):
        print(lst1[p1])
        p1+=1
    elif(lst1[p1]<lst2[p2]):
        p1+=1
    elif(lst1[p1]>lst2[p2]):
        p2+=1

        #lst=[1,3,4,6]
#find the least +ve missing integer from the given list(assignmenet)
"""lst=[1,2,3,4,6]
for i in range(0,len(lst)):
    elem1=lst[i]
    elem2=lst[i+1]
    if elem2-elem1!=1:
     print(elem1+1,"is missing")
     break"""


"""lst=[1,2,4,5,8]
for i in range(0,len(lst)):
    if lst[0]!=1:
        print(1,"is missing")
        break
    else:
        elem1=lst[i]
        elem2=lst[i+1]
        if elem2-elem1!=0:
         print(elem1+1,"is missing")
         break"""


#lst=[2,3,4,4,5,5,6,7]
#find duplicate element from lst




