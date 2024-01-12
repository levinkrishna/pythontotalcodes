list=[12,13,15,16,17]
x=15
# if x in list:
#    print("15 is present")
# else:
#    print("15 is not present")

#if 20 not in list:
#    print("20 is not in list")
#else:
#    print("20 is in list")


#cars=["lamborgini","maruthi800","porshe","bmw"]
#car_o=[]
#for c in cars:
#    if "o" in c:
#        car_o.append(c)
#print(car_o)


#remove 1st,3rd,4th elements from a list
# list=[2,5,7,10,15]
# list.pop(0)
# print(list)
# list.pop(2-1)
# print(list)
# list.pop(3-2)
# print(list)



#create a new list from a given list of integers
#of the new list should be odd and multiples of 5
#list=[5,10,11,15,12,10]
#newlist=[]
#for n in list:
#    if n%5==0 and n%2!=0:
#        newlist.append(n)
#print(newlist)



# find greatest value from the given list without using max()function
#list=[2,6,10]
#maxim=list[0]
#for l in list:
#    if maxim<l:
#        maxim=l
#print("maximum in list :",maxim)

# find the min value in the list without using min function and remove the value from the list

list=[2,6,4,7]
minimum=list[0]
for l in list:
    if minimum>l:
        minimum=l
print(minimum)
list.remove(minimum)
print(list)