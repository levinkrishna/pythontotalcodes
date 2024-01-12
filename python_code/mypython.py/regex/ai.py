violations=["kl-08-av-2794",
            "kl-08-av-4970",
            "kl-01-av-14",
            "kl-01-av-1",
            "kl-01-av-12",
            "TN-01-av-1",
            "ghz-01-avO-1",
            "0kl-01-av-10"

            ]
from re import *
rule="[k][l][-][0-9]{2}[-][a-z]{2}[-][0-9]{1,4}"
for num in violations:
    matcher=fullmatch(rule,num)
    if matcher!=None:
     print(num)