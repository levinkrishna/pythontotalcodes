sent="hi hello hi hi hello good 13,afternoon hi hello hide 13,39"
#print(sent.count("hi"))
import re
ct=re.findall("hi",sent)
print(len(ct))

nums=re.findall("[0-5][0-9]","sent")
print(nums)