text="ABABC"

#Find first recurssive character
wc={}

for ch in text:
    if ch in wc:
        print(ch,"is first recursive character")
        break


    else:
        wc[ch]=1
        