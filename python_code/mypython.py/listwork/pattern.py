arr=[2,3,4]

#o/p=7,6,5
op=[]
total=sum(arr)

for num in arr:
    res=total-num
    op.append(res)
print(op)

