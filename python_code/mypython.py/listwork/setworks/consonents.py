text="goodmorning"
#print no of vowels
vowels={"a","e","i","o","u"}
v_count=0
c_count=0
for ch in text:
    if ch in vowels:
        #print(ch) 
        v_count+=1
    else:
        c_count+=1
    
print(f"vowelscount={v_count},conosent count={c_count}")