# num=input("enter number")

# if type(num)==int:
#     print(num**3)
# else:
#     raise Exception("operand must be integer")


num= input("enter number")
try:
    num=int(num)
    print(num**3)
except Exception as e:
    raise Exception ("operand must be integer")