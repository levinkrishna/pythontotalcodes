word=input("enter a string : ")
out=input("enter another word : ")
#fats
#fast
srt_word=sorted(word)
srt_out=sorted(out)
if srt_word==srt_out:
    print("anagram")
else:
    print("not anagram")


