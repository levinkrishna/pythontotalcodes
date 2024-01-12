lst=[2,3,4,5,6,7,8]

element=6
is_found=False
for i in range (0,len(lst)):
    if element==lst[i]:
        is_found=True
        break
print("found" if is_found==True else "not found")


# lst=[2,3,4,5,6,7,8]
# element=8
# is_found=False
# low=0
# upp=len(lst)-1
# while(low<upp):
#     mid=(low+upp)//2
#     if element==lst[mid]:
#         is_found=True
#         break
#     elif element>lst[mid]:
#         low=mid+1
#     elif element<lst[mid]:
#         upp=mid-1
# print("elements found" if is_found==True else "element note found")

