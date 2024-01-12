text="pycharm is an ide "

#total num of characters

print(len(text))


#total no of vowel

vowels={"a","e","i","o","u"}

c_count=0

v_count=0

for ch in text:
    if ch in vowels:
        # print(ch)
        v_count+=1
    else:
        c_count+=1
print(f"vowels_count={v_count}")

print(f"consents_count={c_count}")