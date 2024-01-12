from re import *
rule="[k-m][369][a-zA-Z0-9]*"
var_name="k6aB1"
matcher=fullmatch(rule,var_name)
if matcher!=None:
    print("valid")
else:
    print("invalid")