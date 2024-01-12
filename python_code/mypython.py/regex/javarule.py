from re import *
rule="[a-zA-Z][a-zA-Z0-9_$]{0,10}"
var_name="num_onemhh"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")