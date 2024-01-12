#nestedlist
lst=[
    [1,2],
    [4,50],
    [50,45],
]
#print all numbers

for sublist in lst:
    for num in sublist:
        print(num)


# allnumbers=[num for sublist in lst for num in sublist]
# print(allnumbers)

#print all numbers >5

"""for sublist in lst:
    for num in sublist:
        if num>5:
            print(num)"""

# num_gt_five=[num for sublist in lst for num in sublist if num>5]
# print(num_gt_five)