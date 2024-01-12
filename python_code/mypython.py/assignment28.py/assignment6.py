ip=int(input("1.Square 2.Triangle > Enter a number:"))
if ip==1:
    s=int(input("Enter the length of one side of the square:"))
    print(f"Area of the square is {s**2}")
elif ip==2:
    base=int(input("Enter the base length of the triangle:"))
    height=int(input("Enter the height of the triangle:"))
    
    print(f"Area of the triangle is {(base*height)/2}")
else:
    print("Invalid input")