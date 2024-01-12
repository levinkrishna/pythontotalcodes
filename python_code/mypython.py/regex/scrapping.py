text="luminar techno luminar techno hub"
from re import *

matcher=finditer("luminar",text)
count=0
for m in matcher:
    count+=1
print(count)


# import re 
# text="aabdXYZ$#098"
# matcher=re.finditer("[^a-zA-Z0-9]",text)
# for m in matcher:
#     print(m.group())