# question 3


from re import *
password=input("Enter Password:")
length=len(password)
rule="[a-zA-Z0-9@#$*&]+"
if length in range(6,16):
    matcher=fullmatch(rule,password)
    if matcher!=None:
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Invalid password")
    