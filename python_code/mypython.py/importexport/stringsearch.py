word="supervisor"
input="superior"

wc={}
is_kangaroo=True

for c in word:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1
for ch in input:
    if ch in wc and wc[ch]>0:
        wc[ch]-=1
    else:
        is_kangaroo=False
        break
print(is_kangaroo)

