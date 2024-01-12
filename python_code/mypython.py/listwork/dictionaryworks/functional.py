lst=[1,2,3,4,5]

#map

"""squares=list(map(lambda n:n**2,lst))
print(squares)

cubes=list(map(lambda n:n**3,lst))
print(cubes)"""


#filter

evens=list(filter(lambda n:n%2==0,lst))
print(evens)

odds=list(filter(lambda n:n%2!=0,lst))
print(odds)

#print all numbers>3
num=list(filter(lambda n:n>3,lst))
print(num)