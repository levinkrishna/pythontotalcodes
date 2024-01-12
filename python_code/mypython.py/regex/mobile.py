import re
"""mob=input("enter your mobile number with country code : ")
check=re.search("^91",mob)
if check:
    print("given number is indian")
else:
    print("given number is foregin")"""

# resi=input("enter a residence number :")
# ekm=re.search("^0484",resi)
# irjkda=re.search("^0480",resi)
# tsr=re.search("^0487",resi)
# pkd=re.search("^0492",resi)
# mprm=re.search("^0494",resi)
# ksd=re.search("^04994",resi)
# cct=re.search("^0495",resi)
# if ekm:
#     print('ekm')
# elif irjkda:
#     print("irjkd")
# elif tsr:
#     print("tsr")
# elif pkd:
#     print("pkd")
# elif mprm:
#     print("mprm")
# elif ksd:
#     print("ksd")
# else:
#     print("cct")


import re
mob=input("enter your mobile number with country code : ")
check=re.search("^[+]91",mob)
if check:
    print("given number is indian")
else:
    print("given number is foregin")