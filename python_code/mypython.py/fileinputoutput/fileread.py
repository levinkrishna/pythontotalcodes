f=open("C:/Users/Admin/Desktop/python_code/mypython.py/fileinputoutput/data.txt","r")
# for line in f:
#     print(line) #print lines

#print all words
words=set()
for line in f:
    line=line.rstrip("\n")
    text=line.split(" ")
    for w in text:
        words.add(w)
print(words)
    


