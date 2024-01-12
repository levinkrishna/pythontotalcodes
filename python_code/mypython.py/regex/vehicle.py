from re import *
rule="[K][L][-][0-9]{0,2}[-][a-z]{2}[-][0-9]{4}"
veh_num="KL-09-av-8952"
matcher=fullmatch(rule,veh_num)
if matcher==None:
    print("invalid")
else:
    print("valid")

