data={
    "django":"framework",
    "react":"library",
    "fastapi":"framework",
    "vue":"framework",
    "ajax":"library"
    }

#o/p={"framework":3,"library":2}

wc={}
for v in data.values():
    if v in wc:
        wc[v]+=1
    else:
        wc[v]=1
print(wc)