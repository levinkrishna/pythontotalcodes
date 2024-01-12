for row in range(1,5):
    for col in range(1,8):
        if(row+col==0) or (col+row==7 and row>1) or (row+col==11 and row>3):
            print("*",end="")
        else:
            print(end=" ")
    print()