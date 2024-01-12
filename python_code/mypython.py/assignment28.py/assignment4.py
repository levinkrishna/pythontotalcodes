# question 4


x=int(input("enter a number for height:"))
y=int(input("enter a number for base length:"))
z=int(input("enter a number:"))
peri=x+y+z
area=x*y/2
print(f"Area={area},Perimeter={peri}")
if x==y==z:
    print("Equilateral Triangle")
elif x==y or y==z or z==x:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")