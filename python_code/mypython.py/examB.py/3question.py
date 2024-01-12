lst=[10,11,10,11,12,13]
duplicates=[]
for num in lst:
    if num in duplicates:
        print(num)
    else:
        duplicates.append(num)
