birds=["peacock","pigeon","duck","hen"]
ch_bird=input("enter a bird : ")

#for i in range(len(birds)-2):
#    print(i)
#    birds.remove(birds[i])
#print(birds)

for i in birds:
    if i==ch_bird:
        birds.remove(i)
print(birds)
