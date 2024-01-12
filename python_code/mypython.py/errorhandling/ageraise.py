age=int(input("enter age"))
# raise
if age<18:
    raise Exception("invalid age")
else:
    print("valid")