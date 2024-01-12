words=["hello","good","aanncccdef","morning"]

def get_len(w):
    return len(w)

print(max(words,key=lambda w:len(w)))

print(min(words,key=lambda w:len(w)))


lst=[1,56,27,2]
print(sorted(lst))
print(sorted(lst,reverse=True))



# sorting by length of words

out=sorted(words,reverse=True,key=lambda w:len(w))
print(out)

