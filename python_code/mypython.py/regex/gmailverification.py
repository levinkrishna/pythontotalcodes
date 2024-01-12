#verify a gmail
import re
gmail=input("enter your gmail : ")
g=re.search("@gmail.com$",gmail)
if g:
    print("it is valid.")
else:
    print("it is not valid.")

