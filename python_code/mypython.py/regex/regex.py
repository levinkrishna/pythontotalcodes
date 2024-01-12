#sen="levin is a very good student in may batch"

#words=sen.split(" ")
#print(sen.startswith("levin"))
"""bol=sen.startswith("levin")
print(bol)
if bol==True:
 print("the sentence is starting with 'levin'")"""


"""if words[0]=="levin":
 print("the sentence is starting with 'levin'")"""




#import package name
import re

sen="levin is avery good student in may batch"
sen2=" levin is avery good student in may batch "
# x=re.search("^is",sen)#for find starting
# y=re.search("^levin",sen)#for find -starting
# end=re.search("levin$",sen)#for find -ending
# print(x)
# print(y)
# print(end)


st_en= re.search("^levin.*batch$",sen)
st_en2=re.search("levin.*batch$",sen2)

print(st_en)
print(st_en2)